# QUIZ GAME

print("Welcome to my computere quiz!")
playing= input("Do you want to play (Yes/No)? ").lower()
if playing.lower() != "yes":
    quit()
print("Okay! Let's play:)")
score = 0

answer = input("What does CPU stands for? ")
if answer.lower() == "central processing unit":
    print("congratulation! It's correct.")
    score += 1
else:
    print("Sorry! It's not correct.")

answer = input("What does GPU stands for? ")
if answer.lower() == "graphics processing unit":
    print("congratulation! It's correct.")
    score += 1
else:
    print("Sorry! It's not correct.")
    
answer = input("What does RAM stands for? ")
if answer.lower() == "random access memory":
    print("congratulation! It's correct.")
    score += 1
else:
    print("Sorry! It's not correct.")
    
answer = input("What does GUI stands for? ")
if answer.lower() == "graphical user interface":
    print("congratulation! It's correct.")
    score += 1
else:
    print("Sorry! It's not correct.")
    
answer = input("What does PC  stands for? ")
if answer.lower() == "personal computer":
    print("congratulation! It's correct.")
    score += 1
else:
    print("Sorry! It's not correct.")

print("Your score is:",str(score))  
print("You got " + str(score ) + " questions correct!")
# To get percent
print("You got " + str((score/5)*100) + "%.")
   


    
    
