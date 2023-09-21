from datetime import date
import re
import sys
import inflect

p = inflect.engine()

def main():
    try:
        year, month, day  = input("Date of Birth: ").split("-")
    except ValueError:
        sys.exit("Invalid Date")
    print(minuites_lived(year, month, day))

def minuites_lived(year, month, day):
    try:
        date_given = date(int(year), int(month), int(day))
    except ValueError:
        return "Invalid Date"
    today = date.today()
    diff = today - date_given
    minuites = int(diff.total_seconds() / 60)
    msg = p.number_to_words(minuites, andword = "") + " minuites"
    return msg.capitalize()


if __name__ == "__main__":
    main()