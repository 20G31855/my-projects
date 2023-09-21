#THIS CODE RETURNS THE TOTAL NUMBER OF LINES OF CODE IN A FILE MINUS COMMENTS AND BLANK LINES
import sys
def main():
        line_count= lines_of_code()
        print(line_count)


def lines_of_code():
    lines_list = ("")
    no_of_files = ("")
    line_count = 0
    command_count = 0
    for words in sys.argv[1:]:
        lines_list+=words
        command_count += 1
    if command_count == 0:
        sys.exit("too few command line argument")
    elif command_count > 2:
        sys.exit("too many command line arguments")
    elif not sys.argv[1].endswith(".py"):
        sys.exit("not a python file")
    else:
        try:
            with open(lines_list) as file:
                for line in file:
                    new_line = line.lstrip()
                    if new_line.startswith("#"):
                        pass
                    elif not line.isspace():
                        no_of_files+=new_line
                        line_count+= 1
        except (FileNotFoundError):
            sys.exit("file does not exist")
        else:
            return (line_count)


if __name__ == "__main__":
    main()