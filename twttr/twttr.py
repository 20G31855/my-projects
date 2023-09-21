def main():
    word = input("Input: ")
    shorten(word)

def shorten(word):
    vowel = ("aAeEiIoOuU")
    for letters in word:
        if letters not in vowel:
            word.replace(letters, '')
            print(letters, end = "")


if __name__ == "__main__":
    main()

