# Image to Sound App

## Overview

The "Image to Sound" app is a Python program that allows you to create sound from image files. It combines Optical Character Recognition (OCR) and text-to-speech synthesis to play back the text extracted from an image as audio. Additionally, it can play a background sound (e.g., forest sound) to enhance the overall experience.

## Requirements

Before running the app, ensure you have the following installed:

- Python (3.7 or higher): [Python Official Website](https://www.python.org/downloads/)
- Tesseract OCR: [Tesseract Installation](https://github.com/tesseract-ocr/tesseract)
- PyTesseract: Install using pip: `pip install pytesseract`
- Pillow (PIL): Install using pip: `pip install pillow`
- gTTS (Google Text-to-Speech): Install using pip: `pip install gtts`
- pygame: Install using pip: `pip install pygame`

## Usage

1. Clone or download this repository to your local machine.

2. Make sure you have your image file (e.g., "image.jpg") and a background sound file (e.g., "forest_sound.wav") ready in the project directory.

3. Open a terminal or command prompt and navigate to the project directory.

4. Create and activate a virtual environment (optional but recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
