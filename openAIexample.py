import os
import keyboard
import openai
import pyperclip
from openai import OpenAI

api_key = os.getenv('OPENAI_API_KEY')
if not api_key:
    raise ValueError("OpenAI API key not found in environment variables.")

client = openai.OpenAI(api_key=api_key)

def correct_sentence(sentence):
    # Attempt to more explicitly maintain the language of the input
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {
                "role": "system",
                "content": "Correct spelling and grammatical errors without changing the sentence structure or the language."
            },
            {"role": "user", "content": sentence}
        ],
        temperature=0.5,  # Lower temperature to reduce creativity
        max_tokens=64,
        top_p=1.0
    )

    if response.choices:
        corrected_text = response.choices[0].message.content
    else:
        corrected_text = "No correction found."
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
