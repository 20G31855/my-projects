import random


level = int(input("Level: "))
while level < 0:
    level = int(input("Level: "))
guess = int(input("Guess: "))
while guess < 0:
    guess = int(input("Guess: "))
random = random.randint(1, level+1)
if guess < random > 0:
    while guess < random > 0:
        print("Too small!")
        guess = int(input("Guess: "))
elif guess > random:
    while guess > random:
         print("Too large!")
         guess = int(input("Guess: "))
if guess == random:
    print("just right!")