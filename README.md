# Manim Animation Generator

A web-based application that generates mathematical animations using Manim through natural language queries. This tool connects to an n8n webhook to convert user requests into Manim code, which is then executed to create animations.

## 🌐 GitHub Pages Landing Page

Visit the static landing page: https://tarunkumarreddy87.github.io/manimanimation

**Note**: This is a static informational page only. The actual application requires server-side processing and cannot run on GitHub Pages.

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

3. Configure your n8n webhook URL in `templates/index.html`

4. Run the application:
   ```bash
   python app.py
   ```

5. Access the application at `http://localhost:5000`

## Deployment

This application can be deployed in several ways:

### Docker Deployment (Recommended)

1. Build the Docker image:
   ```bash
   docker build -t manim-animation-generator .
   ```

2. Run the container:
   ```bash
   docker run -p 5000:5000 manim-animation-generator
   ```

### Docker Compose

1. Use docker-compose:
   ```bash
   docker-compose up
   ```

### Cloud Platforms

The application can be deployed to cloud platforms like:
- Heroku
- Render
- AWS Elastic Beanstalk
- Google Cloud Run
- Azure App Service

### GitHub Actions

The repository includes a GitHub Actions workflow for deployment to Render. To use it:
1. Set up secrets in your GitHub repository:
   - `RENDER_SERVICE_ID`
   - `RENDER_API_KEY`
2. Push to the main branch to trigger deployment

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
├── LICENSE                # License information
├── index.html             # Static landing page for GitHub Pages
├── .gitignore             # Git ignore rules
├── .dockerignore          # Docker ignore rules
├── Procfile               # Heroku deployment configuration
├── runtime.txt            # Heroku Python runtime version
├── Dockerfile             # Docker image configuration
├── docker-compose.yml     # Docker Compose configuration
├── .github/workflows/     # GitHub Actions workflows
│   └── deploy.yml         # Deployment workflow
├── anim_generated/        # Generated animations directory
├── static/                # Static files
└── templates/             # HTML templates
```

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License - see the LICENSE file for details.