import sys
import csv


def main():
    read_and_write_files()


def read_and_write_files():
    if len(sys.argv)  > 3:
        sys.exit("too many command-line arguments")
    if len(sys.argv) < 3:
        sys.exit("too few command-line arguments")
    if not sys.argv[1]==("before.csv"):
        sys.exit(f"could not read {sys.argv[1]}")
    elif not sys.argv[1].endswith(".csv")or not sys.argv[2].endswith(".csv"):
        sys.exit("could not read csv file")
    else:
        try:
            students = []
            with open(sys.argv[1], "r") as file1:
                read_lines = csv.DictReader(file1)
                for row in read_lines:
                    last, first = row["name"].split(",")
                    students.append({
                        "first":first.lstrip(),
                        "last":last,
                        "house":row["house"]
                                    })
            with open(sys.argv[2], "w") as file2:
                write_lines = csv.DictWriter(file2, fieldnames = ["first","last","house"])
                write_lines.writeheader()
                for row in students:
                    write_lines.writerow({
                        "first":row['first'],
                        "last": row["last"],
                        "house": row["house"]
                                    })
        except(FileNotFoundError):
            sys.exit(f"could not read {sys.argv[1]} ")


if __name__ == "__main__":
    main()
