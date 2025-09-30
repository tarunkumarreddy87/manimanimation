import os
import tempfile
import subprocess
import sys
import uuid
from typing import Tuple, Optional
import logging

# Set up logging
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

# Directory to store generated videos
VIDEO_DIR = os.path.join(os.path.dirname(__file__), "anim_generated")
os.makedirs(VIDEO_DIR, exist_ok=True)

def execute_manim_script(script: str) -> Tuple[Optional[str], Optional[str]]:
    """
    Executes a Manim script and returns the path to the generated video or an error message.
    
    Args:
        script (str): The Manim Python script to execute
        
    Returns:
        Tuple[Optional[str], Optional[str]]: (video_path, error_message)
    """
    # Create a temporary directory for this execution
    run_id = str(uuid.uuid4())
    temp_dir = os.path.join(VIDEO_DIR, run_id)
    os.makedirs(temp_dir, exist_ok=True)
    
    try:
        logger.info(f"Executing script in directory: {temp_dir}")
        
        # Write the script to a temporary file
        script_path = os.path.join(temp_dir, "scene.py")
        with open(script_path, "w", encoding="utf-8") as f:
            f.write(script)
        
        logger.info(f"Script written to: {script_path}")
        
        # Extract scene class name from the script
        scene_class = "Scene"  # Default fallback
        for line in script.split("\n"):
            if line.strip().startswith("class ") and "(Scene)" in line:
                scene_class = line.split()[1].replace("(Scene):", "").replace("(Scene)", "").strip()
                logger.info(f"Found scene class: {scene_class}")
                break
        
        # Run Manim command with optimized settings for speed
        cmd = [
            sys.executable, "-m", "manim",
            script_path,
            scene_class,
            "-ql",  # Low quality for faster rendering
            "--media_dir", temp_dir,
            "--disable_caching",  # Disable caching for faster rendering
            "--progress_bar", "none",  # Disable progress bar for faster output
            "--flush_cache"  # Flush cache to avoid memory issues
        ]
        
        logger.info(f"Executing command: {' '.join(cmd)}")
        
        # Execute the command
        result = subprocess.run(
            cmd,
            cwd=temp_dir,
            capture_output=True,
            text=True,
            timeout=120  # Timeout after 2 minutes
        )
        
        logger.info(f"Command completed with return code: {result.returncode}")
        logger.info(f"Stdout: {result.stdout}")
        logger.info(f"Stderr: {result.stderr}")
        
        if result.returncode != 0:
            error_msg = f"Manim execution failed (exit code {result.returncode}):\nSTDERR: {result.stderr}\nSTDOUT: {result.stdout}"
            logger.error(error_msg)
            return None, error_msg
        
        # Find the generated video file
        import glob
        video_files = glob.glob(os.path.join(temp_dir, "**", "*.mp4"), recursive=True)
        logger.info(f"Found video files: {video_files}")
        
        if not video_files:
            error_msg = f"No video file was generated. Check the script for errors.\nSTDERR: {result.stderr}\nSTDOUT: {result.stdout}"
            logger.error(error_msg)
            return None, error_msg
        
        # Return the first video file found
        video_path = video_files[0]
        logger.info(f"Successfully generated video at: {video_path}")
        return video_path, None
        
    except subprocess.TimeoutExpired:
        error_msg = "Manim execution timed out after 2 minutes"
        logger.error(error_msg)
        return None, error_msg
    except Exception as e:
        error_msg = f"Error executing Manim script: {str(e)}"
        logger.exception(error_msg)
        return None, error_msg