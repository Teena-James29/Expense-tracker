import random
num = random.randint(1, 100)
tries = 0
while tries < 7:
    guess = int(input("Guess the number: "))
    tries =tries+ 1
    if guess > num:
        print("Too High!")
    elif guess < num:
        print("Too Low!")
    else:
        print("You found it in", tries, "tries!")
        break
else:
    print("Out of tries! The lucky number was:", num)
