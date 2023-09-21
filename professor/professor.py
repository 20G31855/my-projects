import random


def main():
    generate_integer(get_level())

#Ask for level in loop till valid input 1,2 or 3 is given.
def get_level():
    while True:
        try:
            level = int(input("level:"))
            if level in [1,2,3]:
                break
        except:
            pass
    return level


#generate 10 random questions based on level and reveals score
#repeat a question if failed and revealing correct answer after 3 failed attempts
def generate_integer(level):
    counter = 0
    score = 0
    trails = 1
    for _ in range(10):
        if level == 1:
            first_integer = random.randint(0, 9)
            second_integer = random.randint(0, 9)
            solution = first_integer+second_integer
        elif level == 2:
            first_integer = random.randint(10, 99)
            second_integer= random.randint(10, 99)
            solution = first_integer+second_integer
        elif level == 3:
            first_integer = random.randint(100, 999)
            second_integer = random.randint(100, 999)
            solution = first_integer+second_integer
        while True:
            attempt = int(input(f"{first_integer} + {second_integer} = "))
            if attempt != solution and trails !=3:
                trails +=1
                print("EEE")
                continue
            elif attempt == solution:
                score +=1
                trails = 1
                break
            else:
                print("EEE")
                print(f"{first_integer} + {second_integer} = {solution} ")
                trails = 1
                break
    counter += 1
    print(f'score: {score}')


if __name__ == "__main__":
    main()
