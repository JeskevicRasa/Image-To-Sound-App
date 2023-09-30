import pytesseract
from PIL import Image
from gtts import gTTS
import pygame
import subprocess
import threading

pygame.init()


def perform_ocr(image_path):
    image = Image.open(image_path)
    text = pytesseract.image_to_string(image)
    return text


def text_to_speech(text):
    if text:
        tts = gTTS(text)
        tts.save("output.mp3")
        pygame.mixer.music.load("output.mp3")
        pygame.mixer.music.play()


def open_image_play_sounds(image_path, forest_sound_path):

    forest_sound = pygame.mixer.Sound(forest_sound_path)
    forest_sound.play()

    try:
        subprocess.Popen(["start", image_path], shell=True)
    except Exception as e:
        print(f"Error opening image: {e}")

    extracted_text = perform_ocr(image_path)

    text_to_speech(extracted_text)

    while pygame.mixer.get_busy():
        pygame.time.Clock().tick(10)


if __name__ == "__main__":

    image_path = "forest_image.jpg"
    forest_sound_path = "forest_sound.mp3"

    open_image_thread = threading.Thread(target=open_image_play_sounds, args=(image_path, forest_sound_path))
    open_image_thread.start()

    input("Press Enter to quit...")

    pygame.mixer.quit()
