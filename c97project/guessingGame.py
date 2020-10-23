import random

number = random.randint(1,9)

chances = 0



print("Number Guessing Game")
print("Guess a number (between 1 and 9)")

while chances < 5:
    guess = input("Enter your guess: ") 
    chances = chances + 1 

    if guess == number:
        print("Congratulations YOU WON!!!")
        break
 
if not chances < 5:
        print("YOU LOSE!!! The number is", number)
   
