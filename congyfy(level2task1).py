import random
secret = random.randint(1,100)
guess=int(input("guess a number from 1 to 100: "))
while guess != secret:
    if guess>secret:
        print("Too high")
    else:
        print("to low")
    guess=int(input("guess again:"))
print("congratulations")