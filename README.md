# Manim Animation Generator

A web-based application that generates mathematical animations using Manim through natural language queries. This tool connects to an n8n webhook to convert user requests into Manim code, which is then executed to create animations.

## Features

- Natural language to animation conversion
- Web-based code editor with syntax highlighting
- Real-time animation preview
- Example animations library
- Integration with n8n workflow automation

## Architecture

The application consists of three main components:

1. **Frontend**: Web interface built with Flask and CodeMirror
2. **Backend**: Python Flask server that handles code execution
3. **n8n Integration**: Webhook connection for natural language processing

## Prerequisites

- Python 3.8+
- Manim
- Flask
- n8n (configured webhook)
- FFmpeg (for video processing)

## Installation

1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd manim-animation-generator
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Configure your n8n webhook URL in `app.py`

4. Run the application:
   ```bash
   python app.py
   ```

5. Access the application at `http://localhost:5000`

## Usage

1. Enter a description of the animation you want to create in the input field
2. Click "Ask" to generate the Manim code via the n8n webhook
3. Review and edit the generated code in the editor if needed
4. Click "Generate Animation" to create the animation
5. View the generated animation in the output section

## File Structure

```
manim-animation-generator/
├── app.py                 # Main Flask application
├── manim_executor.py      # Manim code execution module
├── manim.cfg              # Manim configuration
├── requirements.txt       # Python dependencies
├── README.md              # This file
├── .gitignore             # Git ignore rules
├── anim_generated/        # Generated animations directory
└── templates/             # HTML templates
```

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License - see the LICENSE file for details.