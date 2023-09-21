def main():
    dollars = dollars_to_float(input("How much was the meal? "))
    percent = percent_to_float(input("What percentage would you like to tip? "))
    tip = dollars * percent
    print(f"Leave ${tip:.2f}")


def dollars_to_float(d):
    no_sign = d.translate({ord("$"):None})
    floated = float(no_sign)
    return floated


def percent_to_float(p):
    percent = p.translate({ord("%"):None})
    integer_value  = int(percent)/100
    floated_percent= float(integer_value)
    return floated_percent



main()