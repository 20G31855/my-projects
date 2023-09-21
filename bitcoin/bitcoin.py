import json
import sys
import requests

def main():
    bitcoin_price()


def bitcoin_price():
    if len(sys.argv) < 2:
        sys.exit("too few command-line arguments")
    elif len(sys.argv) > 2:
        sys.exit("too many command-line arguments")
    else:
        try:
            response = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
            o = response.json()
            integer = ""
            rate = (o["bpi"]["USD"]["rate"])
            for numbers in rate:
                if numbers ==",":
                    pass
                else: integer += numbers
            integer = float(integer)
            if "." in sys.argv[1]:
                dollar_amount = integer * float(sys.argv[1])
            else:
                dollar_amount = integer * int(sys.argv[1])
            print(f"${dollar_amount:,.4f}")
        except(ValueError):
            sys.exit("command line argument is not a number")
        except requests.RequestException:
            sys.exit("invalid request link")


if __name__ == "__main__":
    main()