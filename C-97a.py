import random
r = random.randint(0, 10)
chances = 0
guess = int( input ("Guess a number: "))
while chances < 3:
    if guess == r:
        print("Congrats, you were right")
    if guess > r:
        print("Nope, too high", r, guess)
        guess = int( input("Guess a number: "))
    if guess < r:
        print("Nope, too low", r, guess)
        guess = int( input("Guess a number: "))
    chances= chances +1
if chances >= 3 and guess != r:
    print("Sorry, your chances are over. The number was:", r)
