import random
number = random.randint (1,100)
guess = int(input("A number between 1,100"))
while int(guess) != number:
    if guess < number:
        print ("your number is too low")
    else:
        print ("your number is too high")
    guess = int(input("Try again....."))
print ("Correct")