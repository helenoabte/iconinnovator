# IconInnovator

## Overview
IconInnovator is a Python program that allows users to customize and animate desktop icons on Windows, providing a personalized interface. The application enables the creation of animated icons from a static icon file, and temporarily sets these animations on the desktop.

## Features
- Customize desktop icons by adding animations.
- Create animated sequences from static icon files.
- Personalize your Windows desktop experience.
  
## Requirements
- Python 3.x
- Pillow library for image manipulation
- Administrative privileges on Windows

## Installation
1. Ensure Python 3.x is installed on your system.
2. Install the Pillow library using pip:
   ```bash
   pip install Pillow
   ```

## Usage
1. Place your icon file in the same directory as the script or provide the path to your icon file.
2. Update the `icon_path` variable in the `icon_innovator.py` script with the path to your icon file.
3. Run the script:
   ```bash
   python icon_innovator.py
   ```

## Limitations
- This program currently targets the Windows platform.
- Requires administrative privileges to change desktop icons.
- Icon animations are temporary and revert to the original after the animation period.

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.