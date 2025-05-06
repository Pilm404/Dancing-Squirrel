# Dancing Squirrel ASCII Animation  

This repository contains a program that displays an animated ASCII art from a dancing squirrel GIF.  

## Description  

The program loads a GIF image from a URL, converts each frame into ASCII art, and displays the animation in the console at a given frame rate.  

## Features  

- Loads a GIF image from a URL  
- Converts each frame into ASCII art using the `ascii_magic` library  
- Customizable parameters:  
  - Number of ASCII art columns  
  - Delay between frames  
- Smooth animation running in a separate thread  
- Cross-platform support (screen clearing for Windows and Unix systems)  

## Dependencies  

- Python 3.x  
- Required libraries:  
  - `requests`  
  - `Pillow` (PIL)  
  - `ascii_magic`  

## Installation  

1. Install the required libraries:  
```bash
pip install requests pillow ascii_magic
```  

2. Run the program:  
```bash
python squirrel_animation.py
```  

## Usage  

By default, the program uses a dancing squirrel GIF. You can change the URL to any other GIF by passing it to the `DancingSquirrel` class constructor.  

Example:  
```python
squirrel = DancingSquirrel("https://example.com/your-animation.gif", columns=120, frame_delay=0.05)
```  

## License  

This project is licensed under the MIT License.
