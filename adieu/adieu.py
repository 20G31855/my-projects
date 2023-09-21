import inflect

list = []
p = inflect.engine()
while True:
    try:
        names = input("Name: ")
        list.append(names)
    #break on a new line
    except EOFError:
        print()
        break

mylist = p.join(list)
print('Adieu, adieu, to '+ mylist)