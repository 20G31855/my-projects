def main():
    sort_list()


def sort_list():
    master_list = {}
    while True:
        try:
            grocery = input("").upper()
            if grocery in master_list:
                #make the key for the dictionary the integers and not the string
                master_list[grocery] += 1
            else:
                master_list[grocery] = 1
        except(EOFError):
               for grocery in sorted(master_list):
                   #print the integer and the string input
                   print(master_list[grocery],grocery)
               break


main()