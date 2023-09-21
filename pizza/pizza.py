import csv
from tabulate import tabulate
import sys


def main():
    table()


def table():
    command_count = 0
    lines_list = ("")
    for words in sys.argv[1:]:
        lines_list+=words
        command_count += 1
    if command_count == 0:
            sys.exit("too few command line argument")
    elif command_count > 1:
        sys.exit("too many command line arguments")
    elif not sys.argv[1].endswith(".csv"):
        sys.exit("not a csv file")
    else:
        try:
            with open(lines_list) as file:
                reader = csv.reader(file)
                print(tabulate(reader, headers="firstrow", tablefmt="grid"))
        except(FileNotFoundError):
            sys.exit("csv file does not exist")


if __name__ == "__main__":
    main()