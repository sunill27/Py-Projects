# ADVENTURE WALK

name= input("Enter your name: ")
print("Welcome to this adventure!", name)

answer= input("You are on a dirt road.Which way you wanna go (left/right)? ").lower()
if answer == "left":
    answer = input("Would you like to walk or swim? ").lower()
    if answer == "walk":
        print("If you walked for miles,you ran out of water and you lost.")
    elif answer == "swim":
        print("If you swim across you were eaten by an alligator and you lost.")
    else:
        print("Not a valid option.You lose")
elif answer == "right":
    answer = input("You came to bridge,it looks damaged, Do you want to cross it or head back(cross/back? ").lower()
    if answer == "cross":
        answer= input("You cross a bridge and met a stranger. Do you talk to him/her (yes/no)? ").lower()
        if answer == "yes":
            print("Ask him/her for help.")
            answer = input("Does he/she help(yes/no)? ").lower()
            if answer== "yes":
                print("Well Done! You won.")
            elif answer== 'no':
                answer = input("Did you found a treasure box? Yes/No! ").lower()
                if answer == 'yes':
                    print("Congrats! You won.")
                elif answer== 'no':
                    print("Sorry! You lost.")
                else:
                    print("Not a valid option.You lose")
            else:
                print("Not a valid option.You lose")                  
        elif answer== 'no':
            print("Ok! keep moving ahead.")
        else:
            print("Not a valid option.You lose")
    elif answer == "back":
        print("Sorry! You lost.")
    else:
        print("Not a valid option.You lose")
else:
    print("You lost!!")

print("Thanks for trying", name, ".")