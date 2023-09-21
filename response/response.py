from validator_collection import checkers

def main():
    email_checker()

def email_checker():
    result = checkers.is_email(input("whats your email address? "))
    if result:
        print("Valid")
    else:
        print("Invalid")


if __name__ == "__main__":
    main()