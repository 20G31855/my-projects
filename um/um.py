#this code checks for stand alone characters using regex, in this case "um"
import re
import sys


def main():
    print(count(input("Text: ")))

#function using word boundaries to the left and right of "um"
def count(s):
     search = re.findall(r"\bum\b",s, re.IGNORECASE)
     return(len(search))









if __name__ == "__main__":
    main()