from gtts import gTTS
import sys

def main():
    wordings = TextToSpeech()


def TextToSpeech():
    counter = 0
    with open(sys.argv[1]) as textFile:
        for words in textFile:
            if words == sys.argv[3]:
                counter +=1
            else:
                pass
    tts = gTTS(f"{sys.argv[3]} appeared a total of {counter} times")
    tts.save(sys.argv[2])


main()