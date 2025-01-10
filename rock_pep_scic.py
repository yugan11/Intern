import random
user_choice = int(input("Enter your choice  :type 0 for Rock ,  1 for paper , 2 for scissor"))
if user_choice >= 3 or user_choice < 0:
    print("You entered invaild number, you loose")
else:
    computer_choice = random.randint(0,2)
    print("computer chose:")
    print(computer_choice)
    if computer_choice == user_choice:
        print("Its draw")
    elif computer_choice == 0 and user_choice == 2:
        print("You loose")
    elif computer_choice == 2 and user_choice == 0:
        print("you win")
    elif computer_choice > user_choice :
        print("You loose")
    elif computer_choice < user_choice :
        print("you win")
