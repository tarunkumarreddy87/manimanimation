# Setup Guide

## Prerequisites

Before you begin, ensure you have the following installed on your system:

1. **Python 3.8 or higher**
2. **Git** (for cloning the repository)
3. **FFmpeg** (for video processing)
4. **Manim** (installed automatically with requirements)

## Installation Steps

### 1. Clone the Repository

```bash
git clone <repository-url>
cd manim-animation-generator
```

### 2. Create a Virtual Environment (Recommended)

```bash
python -m venv venv
# On Windows
venv\Scripts\activate
# On macOS/Linux
source venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Install FFmpeg

#### Windows:
1. Download FFmpeg from https://ffmpeg.org/download.html
2. Extract the archive to a folder (e.g., `C:\ffmpeg`)
3. Add the `bin` directory to your system PATH

#### macOS:
```bash
# Using Homebrew
brew install ffmpeg
```

#### Ubuntu/Debian:
```bash
sudo apt update
sudo apt install ffmpeg
```

### 5. Configure n8n Webhook

1. Set up your n8n workflow with the appropriate Manim code generation
2. Update the webhook URL in `templates/index.html`:
   ```javascript
   const response = await fetch('YOUR_N8N_WEBHOOK_URL', {
       method: 'POST',
       headers: { 'Content-Type': 'application/json' },
       body: JSON.stringify({ question: input })
   });
   ```

### 6. Run the Application

```bash
python app.py
```

The application will start on `http://localhost:5000`.

## Troubleshooting

### Common Issues

1. **FFmpeg not found**: Ensure FFmpeg is installed and added to your system PATH
2. **Manim installation issues**: Try installing Manim separately with `pip install manim`
3. **Port already in use**: Change the port in `app.py` or stop the process using the port

### Manim Configuration

If you have a custom FFmpeg installation, update the `manim.cfg` file:

```ini
[CLI]
ffmpeg_executable = /path/to/your/ffmpeg
```

## Usage

1. Open your browser and navigate to `http://localhost:5000`
2. Enter a description of the animation you want to create
3. Click "Ask" to generate the Manim code via the n8n webhook
4. Review and edit the generated code if needed
5. Click "Generate Animation" to create the animation
6. View the generated animation in the output section