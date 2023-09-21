def main():
    fraction = (input("fraction: "))
    print(guage(convert(fraction)))


def convert(fraction):
    # take input and convert to fraction
    while True:
    # numerator and denominator
        try:
            x, y = fraction.split("/")
            # convert strings to integers
            numerator = int(x)
            denominator = int(y)
            # calculation to get decimals
            decimal =(int(numerator / denominator * 100))
            if numerator > denominator:
                pass
            else:
                return(decimal)
        except(ZeroDivisionError, ValueError):
            pass


def guage (integer_value):
        if integer_value <= 1:
            return("E")
        elif integer_value >= 99:
            return("F")
        else:
            return(f"{integer_value}%")


if __name__ == '__main__':
    main()