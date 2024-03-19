import requests


def correct_english_text(text):
    url = "https://languagetool.org/api/v2/check"
    params = {
        "text": text,
        "language": "en-US",
    }
    response = requests.post(url, data=params)
    corrections = response.json()

    corrected_text = text
    for mistake in corrections['matches'][::-1]:  # Reverse to avoid index issues
        if mistake['replacements']:
            corrected_text = corrected_text[:mistake['offset']] + mistake['replacements'][0]['value'] + corrected_text[
                                                                                                        mistake[
                                                                                                            'offset'] +
                                                                                                        mistake[
                                                                                                            'length']:]

    return corrected_text


# Input text
input_text = "i want make an desktop application. this application runs in background. when I type some sentence and trigger an input event, I corrects specified sentence. how can I do that can you help me. i will use it for primarily turkish and english."

# Correct the text
corrected_text = correct_english_text(input_text)

print("Original Text:")
print(input_text)
print("\nCorrected Text:")
print(corrected_text)