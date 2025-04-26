secret_number = 9
guess_count = 0
guess_limit = 3
print("Guess the number on 3 chances")
while guess_count < guess_limit:
    guess = int(input("Guess: "))
    guess_count += 1
    if guess == secret_number:
        print("You won!")
        break
    else:
        print("Try Again")
else:
    print("Opps! 3 chances missed.")
    