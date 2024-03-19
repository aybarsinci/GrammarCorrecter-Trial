from textblob import TextBlob
import keyboard
import pyperclip
from openai import OpenAI

client = OpenAI(api_key='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')

def correct_sentence(sentence):
    blob = TextBlob(sentence)
    corrected_text = str(blob.correct())
    return corrected_text
def on_triggered():
    original_text = pyperclip.paste()  # Get the current text from the clipboard
    corrected_text = correct_sentence(original_text)
    pyperclip.copy(corrected_text)  # Copy the corrected text to the clipboard

    # Print statements for debugging purposes; remove or comment out as needed
    print("Original:", original_text)
    print("Corrected:", corrected_text)

    # Simulate a paste operation to insert the corrected text
    keyboard.press_and_release('ctrl+v')

keyboard.add_hotkey('ctrl+c+alt', on_triggered)

# Block forever, listening for keyboard events
keyboard.wait()
