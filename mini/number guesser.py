import random

top_of_range = input("Please type a number: ")

if top_of_range.isdigit():
    top_of_range = int(top_of_range)
    
    if top_of_range <= 0:
        print('please type a number that greater than that next time.')
        quit()
        
else:
    print('please type another number.')
    quit()

random_number = random.randint(0, top_of_range)
guesses = 0

while True:
    guesses += 1
    user_guess = input("make a guess: ")
    if user_guess.isdigit():
        user_guess = int(user_guess)
    else:
        print('please type the number next time.')
        continue
    
    if user_guess == random_number:
        print("You got it!")
        break
    elif user_guess > random_number:
        print("You're above the number")
    else:
         print("You're below the number")
        
print("You got", guesses, "guesses right")