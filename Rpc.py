import random

choices = ("r","p","s")
Emoji= {
  'r':'🪨', 'p': '📃','s':'✂️'
}
while True:
    User_choice = input("Rock, Paper and Sissors:").lower()

    if User_choice not in choices:
     print ("Invalid Input!! Please try again.")
    continue

    Computer_choice = random.choice(choices)
    print(f"Computer Choose {Emoji [Computer_choice]}")
    print(f"You Choose{Emoji [User_choice]}")

    if Computer_choice == User_choice:
        print("It's a Tie")
    elif (
        (User_choice =='r' and Computer_choice =='s') or
        (User_choice == 'p' and Computer_choice =='r') or
        (User_choice =='s' and Computer_choice =='p')):
            print("You Win!!!")
    else:
        print("You Lost!")

    Playing = input("Continue Playing? (y/n)").lower()
    if Playing== 'n':
        break