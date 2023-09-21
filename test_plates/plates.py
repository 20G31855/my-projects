def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(plate):
    first_letter = (plate[0:1])
    second_letter = (plate[1:2])
    digit_count = 0
    is_True = True
    # a vanity plate must contain a maximum of 6 characters and a minimum of 2 done
    if 6 >= len(plate) >= 2:
        is_True = True
    else:
        is_True = False
        return is_True
    # all vanity plates must start with two letters
    if first_letter.isalpha() and second_letter.isalpha():
        is_True = True
    else:
         is_True = False
         return is_True
    # no peiods spaces or punctuations are allowed
    if plate.isalnum():
        is_True = True
    else:
        is_True= False
        return is_True
    # numbers cannot be in the middle of the input
    for character in plate:
        if digit_count > 0 and character.isalpha():
            is_True = False
        #digit cannot start with zero
        if character.isdigit() and character == "0" and digit_count ==0:
            is_True = False
        if character.isdigit():
            digit_count += 1


    return is_True

if __name__ == "__main__":
    main()