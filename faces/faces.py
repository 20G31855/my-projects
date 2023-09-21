def main():
    print(convert())

def convert():
    value = input("")
    output = value.replace(":)","🙂").replace(":(","🙁")
    return output
main()