# Usage Guide

## Getting Started

After setting up the application, open your browser and navigate to `http://localhost:5000`. You'll see the main interface with three sections:

1. **Animation Request** - Where you describe what animation you want
2. **Code Editor** - Where you can view and edit the generated code
3. **Output** - Where the generated animation will be displayed

## Creating Your First Animation

### Method 1: Using Natural Language

1. In the input field, type a description of the animation you want:
   ```
   Create an animation showing a circle transforming into a square
   ```

2. Click the "Ask" button
3. Wait for the n8n webhook to process your request and generate the code
4. Review the generated code in the editor
5. Click "Generate Animation"
6. View the animation in the output section

### Method 2: Using Example Animations

1. Scroll down to the "Example Animations" section
2. Click on one of the examples:
   - "Simple Animation" - Shows basic shape transformations
   - "Text Animation" - Demonstrates text animations
3. The code for the selected example will appear in the editor
4. Click "Generate Animation"
5. View the animation in the output section

### Method 3: Writing Your Own Code

1. Clear the editor using the "Clear" button if needed
2. Write your own Manim code directly in the editor
3. Click "Generate Animation"
4. View the animation in the output section

## Working with the Code Editor

The code editor uses CodeMirror with Python syntax highlighting:

- **Syntax Highlighting**: Python keywords, strings, and comments are color-coded
- **Line Numbers**: Helps with navigation and debugging
- **Auto-indentation**: Maintains proper code formatting
- **Undo/Redo**: Ctrl+Z and Ctrl+Y for editing history

### Editor Features

- You can edit any generated code before execution
- Syntax errors in your code will be reported during generation
- The editor preserves your work between sessions

## Understanding the Output

### Successful Generation

When an animation is successfully generated:

1. The loading message will disappear
2. The video player will appear in the output section
3. The animation will start playing automatically
4. You can use the video controls to pause, rewind, or replay

### Error Handling

If there's an error during generation:

1. An error message will appear in the error section (red text)
2. The output section will remain empty
3. Common errors include:
   - Invalid Manim syntax
   - Missing dependencies
   - Resource limitations
   - n8n webhook issues

## Advanced Usage

### Customizing Animations

You can modify any aspect of the generated code:

1. Change colors: `circle = Circle(color=RED)`
2. Adjust timing: `self.play(Create(circle), run_time=2)`
3. Add more objects: Create multiple shapes and animate them together
4. Modify transformations: Use different animation types like `Transform`, `FadeIn`, `GrowFromCenter`, etc.

### Combining Examples

You can combine code from different examples:

1. Load one example
2. Copy part of the code
3. Load another example
4. Paste and integrate the copied code
5. Generate the combined animation

## Tips and Best Practices

### For Better Results with n8n

1. **Be Specific**: Instead of "create an animation", try "create an animation of a red circle moving in a square pattern"
2. **Use Mathematical Terms**: Include terms like "sine wave", "parabola", "derivative" when relevant
3. **Specify Colors**: Mention colors when you want specific visual elements
4. **Describe Timing**: Include terms like "slowly", "quickly", "step by step" for timing cues

### For Manual Code Writing

1. **Start Simple**: Begin with basic shapes and simple animations
2. **Test Frequently**: Generate animations often to catch errors early
3. **Use Documentation**: Refer to Manim documentation for available classes and methods
4. **Build Incrementally**: Add complexity gradually

### Performance Considerations

1. **Keep Animations Short**: Long animations take more time to generate
2. **Use Low Quality for Testing**: The `-ql` flag makes generation faster
3. **Avoid Complex Scenes**: Very complex scenes may fail to render
4. **Clear Old Animations**: Periodically clear the `anim_generated` directory

## Troubleshooting Common Issues

### n8n Webhook Not Responding

1. Check your internet connection
2. Verify the webhook URL in `templates/index.html`
3. Ensure your n8n workflow is active
4. Check n8n logs for errors

### Animation Generation Fails

1. Check the error message for specific details
2. Review the code in the editor for syntax errors
3. Simplify the code to isolate the issue
4. Try one of the example animations to verify the system works

### Video Not Playing

1. Check if the video file was generated in `anim_generated/`
2. Verify FFmpeg is properly installed
3. Try refreshing the page
4. Check browser console for errors

### Slow Performance

1. Ensure you're using the low quality setting (`-ql`)
2. Close other resource-intensive applications
3. Simplify your animation code
4. Check system resources (CPU, memory)

## Example Queries for n8n

Here are some example queries that work well with the n8n integration:

1. "Create an animation of a sine wave with a moving dot along the curve"
2. "Show the Pythagorean theorem with a right triangle and squares on each side"
3. "Animate the derivative of x squared as 2x with tangent lines"
4. "Create a growing bar chart showing data over time"
5. "Show matrix multiplication with animated transformations"
6. "Animate the Fibonacci sequence with squares and a spiral"
7. "Create a pendulum animation with physics equations"
8. "Show the unit circle with trigonometric functions"

These examples help the AI understand what kind of animation you're looking for and generate appropriate Manim code.