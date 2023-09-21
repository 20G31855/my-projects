import re
import sys


def main():
    print(convert(input("Hours: ")))


def convert(s):
            if time := re.search(r"^(\d*):?(\d*)? (AM|PM)* to+ (\d*):?(\d*)? (AM|PM)*$", s, re.IGNORECASE):
                initial_hour,initial_minuite,initial_suffix,final_hour,final_minuite,final_suffix = time.groups()
            else:
                 raise ValueError
            initial_hour = int(initial_hour)
            final_hour = int(final_hour)
            if initial_suffix == "PM" and initial_hour != 12:
                  initial_hour = initial_hour+12
            if final_suffix == "PM" and final_hour != 12:
                  final_hour = final_hour+12
            if initial_hour == 12 and initial_suffix == "AM":
                  initial_hour -=12
            if final_hour == 12 and final_suffix == "AM":
                  final_hour -=12
            if initial_minuite == "":
                  initial_minuite = "00"
            if final_minuite == "":
                  final_minuite = "00"
            if initial_hour < 10:
                  initial_hour = "0"+ str(initial_hour)
            if final_hour < 10:
                  final_hour = "0"+ str(final_hour)
            if int(initial_minuite) > 59 or int(final_minuite)> 59:
                  raise ValueError
            return(f"{initial_hour}:{initial_minuite} to {final_hour}:{final_minuite}")


if  __name__ == "__main__":
    main()