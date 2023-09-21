def main():
    Greet = input("Greeting:").lower().strip()
    cash = value(Greet)
    print(f"${cash}")

def value(Greet):
    if Greet.startswith("hello"):
        return 0
    elif Greet.startswith("h"):
        return 20
    else:
        return 100


if __name__ == "__main__":
    main()
