target = 37
guess = None

while guess != target:
    guess = int(input("Guess my favorite number: "))
    if guess < target:
        print("Too low!")
    elif guess > target:
        print("Too high!")
    else:
        print("You got it!")
        break