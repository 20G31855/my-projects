import re
import sys


def main():
    print(parse(input("HTML: ")))


def parse(s):
    if link := re.search(r'src="https?://(?:www.)?youtube.com/embed/([a-z_0-9]+)', s, re.IGNORECASE):
        return(f"https://youtu.be/{link.group(1)}")
        special_characters = link.group(1)

    else:
        return None






if __name__ == "__main__":
    main()