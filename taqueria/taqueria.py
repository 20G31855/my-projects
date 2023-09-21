def main():
    taqueria()


def taqueria():
    sum = 0
    while True:
        #dictionary showing the prices of goods
        d = {
            "Baja Taco": 4.00,
            "Burrito": 7.50,
            "Bowl": 8.50,
            "Nachos": 11.00,
            "Quesadilla": 8.50,
            "Super Burrito": 8.50,
            "Super Quesadilla": 9.50,
            "Taco": 3.00,
            "Tortilla Salad": 8.00
        }
        try:
            key = input("Item:").title()
        # control d should break the input loop
        except (EOFError):
            break
        except(KeyError):
            pass
        else:
            value = d.get(key)
            if key in d:
                sum += value
                print(f"${sum:.2f}")


main()