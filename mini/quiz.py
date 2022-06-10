print("Hello! Welcome to my quiz game!")

playing = input("Do you want to play?")

if playing.lower != "yes":
    quit()
    
print("Okay, Let's go")
score = 0

answer = input ("what does CPU stand for? ").lower
if answer == "central processing unit":
    print("correct")
    score += 1
else:
    print("incorrect")

answer = input ("what does RAM stand for? ").lower
if answer == "random access memory":
    print("correct")
    score += 1
else:
    print("incorrect")
    
print("You got" + str(score) + "question correct!")