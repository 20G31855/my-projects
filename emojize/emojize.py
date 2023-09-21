import emoji


def main():
    emoji_converter()


def emoji_converter():
    emoji_input = input("Input:")
    print(emoji.emojize(f"output:{emoji_input}"))


if "__main__"==__name__:
    main()