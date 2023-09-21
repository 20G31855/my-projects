name = input("name:")
for letters in name:
    #i got the isupper method from the internet stackflow to be exact
    upper_case = letters.isupper()
    if upper_case is True:
        print( "_"+letters.lower(), end= "")
    else:
        print(letters,end="")
