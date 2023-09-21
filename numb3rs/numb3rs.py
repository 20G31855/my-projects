import re
import sys


def main():
    print(validate(str(input("IPv4 Address: "))))


def validate(ip):
    if IpAdress := re.search(r"^[0-225]+\.[0-225]+\.[0-225]+\.[0-225]+$", ip):
        return(True)
    else:
        return(False)




if  __name__ == "__main__":
    main()