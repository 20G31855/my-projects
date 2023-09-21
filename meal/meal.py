def main():
    converted = convert(input("whats the time? "))
    converted = float(converted)
    if 7.00 <= converted <= 8.00:
        value_time = ("breakfast time")
    if 12.00 <= converted <= 13.00:
        value_time = ("lunch time")
    if 18.00 <= converted <= 19.00:
        value_time = ("dinner time")
    print(value_time)


def convert(time):
    hours, minuites = time.split(":")
    hours = float(hours)
    minuites = float(minuites)
    min_fraction = minuites/60
    value = hours + min_fraction
    return value


if __name__ == "__main__":
    main()