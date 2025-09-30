from flask import Flask, request, jsonify, send_file, render_template
from flask_cors import CORS
import os
import logging
from manim_executor import execute_manim_script, VIDEO_DIR
from typing import Dict, Optional

# Set up logging
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

app = Flask(__name__, template_folder='templates')
CORS(app)  # Enable CORS for all routes

# Store latest video file path (in-memory for simplicity)
LATEST_VIDEO: Dict[str, Optional[str]] = {"path": None, "error": None}

# Create directory for generated animations
os.makedirs('anim_generated', exist_ok=True)

@app.route("/")
def index():
    # Serve the HTML frontend
    return render_template('index.html')

@app.route("/api/generate", methods=["POST"])
def generate():
    """
    Receives Manim script (from n8n), executes it, and returns video URL or error.
    """
    try:
        logger.info("Received request to /api/generate")
        data = request.get_json()
        logger.debug(f"Request data: {data}")
        
        script = data.get("script") if data else None
        if not script:
            logger.warning("No script provided in request")
            return jsonify({"error": "No script provided"}), 400
        
        logger.info(f"Received script (first 200 chars): {script[:200]}...")
        
        video_path, error = execute_manim_script(script)
        if error:
            LATEST_VIDEO["path"] = None
            LATEST_VIDEO["error"] = error
            logger.error(f"Execution error: {error}")
            return jsonify({"error": error}), 400
        
        # Save latest video path
        LATEST_VIDEO["path"] = video_path
        LATEST_VIDEO["error"] = None
        # Return endpoint for video
        video_url = "/video/latest"
        logger.info(f"Successfully generated video at: {video_path}")
        return jsonify({"video_url": video_url})
    
    except Exception as e:
        logger.exception("Error in generate endpoint")
        return jsonify({"error": f"Server error: {str(e)}"}), 500

@app.route("/video/latest")
def get_latest_video():
    """
    Streams the latest generated video.
    """
    try:
        logger.info("Received request to /video/latest")
        video_path = LATEST_VIDEO.get("path")
        logger.debug(f"Video path from LATEST_VIDEO: {video_path}")
        
        if not video_path or not os.path.exists(video_path):
            logger.warning(f"Video not found at path: {video_path}")
            return "No video available.", 404
            
        logger.info(f"Serving video from: {video_path}")
        return send_file(video_path, mimetype="video/mp4")
    except Exception as e:
        logger.exception("Error serving video")
        return f"Error serving video: {str(e)}", 500

@app.errorhandler(Exception)
def handle_error(e):
    logger.exception("Unhandled error occurred")
    return jsonify({"error": f"Unhandled server error: {str(e)}"}), 500

if __name__ == "__main__":
    import os
    # Check if we're running in a production environment
    if os.environ.get('FLASK_ENV') == 'production':
        # In production, don't use debug mode
        app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 5000)))
    else:
        # In development, use debug mode without reloader
        app.run(debug=True, host='0.0.0.0', port=5000, use_reloader=False)
