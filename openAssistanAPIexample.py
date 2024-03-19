import keyboard
import pyperclip
import cohere
import time

# Replace 'your-cohere-api-key' with your actual Cohere API key
co = cohere.Client('your_api_key')


def correct_sentence(sentence):
    prompt = (
        "Correct the following sentence by fixing spelling and grammatical errors, "
        "but do not change the meaning or add any extra content ony the corrected sentence:\n\n"
        f"{sentence}\n\nCorrected sentence:"
    )
    response = co.generate(
        model='command',  # Replace with a valid Cohere model name
        prompt=prompt,
        max_tokens=1000,  # Adjust based on the expected length of corrections
        temperature=0.3,  # Adjust for more conservative corrections
        stop_sequences=["Corrected sentence:"]  # This helps to stop the generation
    )

    if response.generations:
        generation = response.generations[0].text.strip()
        # Extract the text after "Corrected sentence:"
        corrected_text = generation.split('Corrected sentence:')[
            1].strip() if 'Corrected sentence:' in generation else generation
        # Further split by new line if necessary and return the first line
        return corrected_text.split('\n')[0].strip() if corrected_text else "No correction found."
    else:
        return "No correction found."


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
