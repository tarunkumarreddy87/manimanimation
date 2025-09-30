# Contributing to Manim Animation Generator

Thank you for your interest in contributing to the Manim Animation Generator! This document provides guidelines and information to help you contribute effectively.

## How to Contribute

### Reporting Bugs

If you find a bug, please open an issue on GitHub with:

1. A clear and descriptive title
2. Steps to reproduce the bug
3. Expected behavior
4. Actual behavior
5. Screenshots if applicable
6. Your environment information (OS, Python version, etc.)

### Suggesting Enhancements

To suggest a new feature or enhancement:

1. Check if there's already an open issue for your suggestion
2. If not, open a new issue with:
   - A clear description of the enhancement
   - Use cases for the feature
   - Any implementation ideas you might have

### Code Contributions

#### Development Setup

1. Fork the repository
2. Clone your fork:
   ```bash
   git clone https://github.com/your-username/manim-animation-generator.git
   cd manim-animation-generator
   ```
3. Create a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```
4. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

#### Making Changes

1. Create a new branch for your feature or bugfix:
   ```bash
   git checkout -b feature/your-feature-name
   ```
2. Make your changes
3. Test your changes thoroughly
4. Commit your changes with a clear message:
   ```bash
   git commit -m "Add feature: brief description of your changes"
   ```
5. Push to your fork:
   ```bash
   git push origin feature/your-feature-name
   ```
6. Open a pull request

#### Code Style

- Follow PEP 8 for Python code
- Use meaningful variable and function names
- Write docstrings for functions and classes
- Keep functions small and focused
- Comment complex logic

#### Testing

- Test your changes locally before submitting
- Ensure the application starts without errors
- Verify that existing functionality still works
- Test with different types of input

## Project Structure

Understanding the project structure will help you contribute more effectively:

```
manim-animation-generator/
├── app.py                 # Main Flask application
├── manim_executor.py      # Manim code execution module
├── manim.cfg              # Manim configuration
├── requirements.txt       # Python dependencies
├── README.md              # Project overview
├── LICENSE                # License information
├── .gitignore             # Git ignore rules
├── docs/                  # Documentation files
│   ├── setup.md           # Setup guide
│   ├── usage.md           # Usage instructions
│   ├── architecture.md    # Architecture overview
│   └── contributing.md    # This file
├── templates/             # HTML templates
│   └── index.html         # Main web interface
├── anim_generated/        # Generated animations (gitignored)
└── static/                # Static files (gitignored)
```

## Areas for Contribution

### Frontend Improvements

- UI/UX enhancements
- Additional editor features
- New example animations
- Mobile responsiveness
- Accessibility improvements

### Backend Enhancements

- Performance optimizations
- Additional error handling
- New API endpoints
- Better file management
- Enhanced security features

### Documentation

- Improving existing documentation
- Adding new guides and tutorials
- Translating documentation
- Creating video tutorials

### Integration Features

- Additional webhook integrations
- Support for other AI services
- Export options (GIF, different video formats)
- Cloud storage integration

## Pull Request Guidelines

1. **One Feature Per Pull Request**: Keep changes focused on a single feature or bugfix
2. **Clear Description**: Explain what your changes do and why
3. **Reference Issues**: Link to any related issues
4. **Pass Tests**: Ensure all tests pass
5. **Code Review**: Be open to feedback and changes

## Community

### Communication

- GitHub Issues for bug reports and feature requests
- GitHub Discussions for general questions and community interaction
- Be respectful and constructive in all interactions

### Code of Conduct

By participating in this project, you agree to:

- Be respectful and inclusive
- Provide constructive feedback
- Welcome newcomers
- Focus on what's best for the community
- Show empathy towards others

## Recognition

Contributors will be recognized in:

- The GitHub contributors list
- Release notes for significant contributions
- The documentation (for major contributions)

Thank you for helping make the Manim Animation Generator better for everyone!