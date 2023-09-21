def main():
    word = input("Input: ")
    var = shorten(word)
    print("Output: "+ var)


def shorten(word):
    list = ""
    vowel = ("aAeEiIoOuU")
    for letters in word:
        if not letters.lower() in ['a', 'e', 'i', 'o', 'u']:
            list+= letters
    return list








if __name__ == "__main__":
    main()
