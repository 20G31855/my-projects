from gtts import gTTS
import os

# Function to convert text to speech with word omission
def text_to_speech_with_omission(text, omit_word):
    # Replace the omit_word with an empty string to omit it
    text = text.replace(omit_word, "")

    # Initialize gTTS with the modified text
    tts = gTTS(text)

    # Save the speech to an audio file (e.g., output.mp3)
    tts.save("output.mp3")

    # Play the audio using your system's default player
    os.system("start output.mp3")

if __name__ == "__main__":
    input_text = "This is a sample sentence. We can omit specific words from this sentence."
    word_to_omit = "omit"

    text_to_speech_with_omission(input_text, word_to_omit)
