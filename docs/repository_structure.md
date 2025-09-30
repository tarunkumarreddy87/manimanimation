# Repository Structure

This document provides an overview of the organized file structure for the Manim Animation Generator repository, ready for GitHub upload.

## Root Directory

```
manim-animation-generator/
├── .gitignore              # Git ignore rules for excluding unnecessary files
├── LICENSE                 # MIT License file
├── README.md               # Project overview and quick start guide
├── app.py                  # Main Flask application entry point
├── manim.cfg               # Manim configuration file
├── manim_executor.py       # Manim code execution module
├── requirements.txt        # Python dependencies
├── architecture.md         # Architecture overview and component interactions
├── contributing.md         # Guidelines for contributing to the project
├── setup.md                # Detailed setup and installation instructions
└── usage.md               # Usage guide and examples
```

## Directories

### docs/
Contains comprehensive documentation for users and contributors:
- `architecture.md` - System design and component interactions
- `contributing.md` - Guidelines for contributing to the project
- `setup.md` - Detailed installation and configuration instructions
- `usage.md` - Comprehensive usage guide with examples

### templates/
Contains HTML templates for the web interface:
- `index.html` - Main web interface with CodeMirror editor

### anim_generated/ (gitignored)
Directory for storing generated animations. Each animation is stored in a separate subdirectory with a unique ID.

### static/ (gitignored)
Static files directory. Currently contains:
- `output/` - Video files served to the frontend
- `videos/` - Additional video storage (currently empty)

### manimations/ (deprecated)
Legacy directory from earlier development. Can be removed for a cleaner repository.

### vrt/ (deprecated)
Previous version of the web application. Can be removed for a cleaner repository.

## File Descriptions

### Core Application Files

**app.py**
- Main Flask application
- Serves the web interface
- Handles API endpoints for code generation and video streaming

**manim_executor.py**
- Executes Manim scripts
- Manages temporary directories and file cleanup
- Handles error reporting and logging

**manim.cfg**
- Manim configuration file
- Configurable FFmpeg path
- Other Manim settings

### Documentation Files

**README.md**
- Project overview
- Quick start instructions
- Basic usage information

**LICENSE**
- MIT License terms

**requirements.txt**
- Python package dependencies
- Version specifications for reproducible installations

### Documentation Directory Files

**docs/architecture.md**
- Detailed system architecture
- Component interactions
- Data flow diagrams
- API specifications

**docs/contributing.md**
- Contribution guidelines
- Development setup instructions
- Code style guidelines
- Pull request process

**docs/setup.md**
- Prerequisites and installation
- Environment configuration
- Troubleshooting common issues

**docs/usage.md**
- Detailed usage instructions
- Example workflows
- Best practices and tips

### Configuration Files

**.gitignore**
- Comprehensive ignore rules for:
  - Virtual environments
  - IDE files
  - OS generated files
  - Log files
  - Generated content
  - Distribution files

## Recommended Git Workflow

1. **Initial Clone**
   ```bash
   git clone <repository-url>
   cd manim-animation-generator
   ```

2. **Environment Setup**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   pip install -r requirements.txt
   ```

3. **Running the Application**
   ```bash
   python app.py
   ```

## Cleanup Recommendations

For a cleaner repository, consider removing these directories before uploading:

1. **manimations/** - Legacy development files
2. **vrt/** - Previous version of the application
3. **.venv/** - Virtual environment (should not be committed)
4. **__pycache__/** - Python cache files (covered by .gitignore)

## Deployment Considerations

### Production Deployment

For production deployment, consider:

1. Using a production WSGI server (Gunicorn, uWSGI) instead of Flask's development server
2. Setting up proper logging
3. Configuring environment variables for sensitive settings
4. Implementing proper error handling and monitoring
5. Using a CDN for static assets
6. Setting up automated backups for generated content

### Environment Variables

Consider using environment variables for:

1. n8n webhook URL
2. FFmpeg path
3. Logging configuration
4. Security settings

## Version Control Best Practices

1. **Commit Messages**: Use clear, descriptive commit messages
2. **Branching**: Use feature branches for development
3. **Pull Requests**: Review code before merging
4. **Tagging**: Tag releases with semantic versioning
5. **Documentation**: Keep documentation in sync with code changes

This structure provides a clean, organized, and maintainable codebase that follows standard practices for Python web applications.