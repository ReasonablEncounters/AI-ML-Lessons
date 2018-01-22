import random

a = random.randint(1,9)
c = 0
guess = 0

while guess != a:
    guess = input("Guess a number between 1 and 9!? ")

    if guess == "exit":
        break

    guess = int(guess)
    c += 1

    if guess < a:
        print("\n===== Too Low, Try Again! =====\n")
		
    elif guess > a:
        print("\n===== Too High, Try Again! =====\n")
		
    else:
        print("\nRight on!")
        print("It only took", c, "attempt(s)!")
		
input()
