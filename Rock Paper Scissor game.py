from random import randint 
#create a list of play options
o = ["Rock", "Paper", "Scissors"]
#assign a random play to the computer
computer = o[randint(0,1)]
#set player to False
player = False

while player == False:
#set player to True
   player = input( "Rock, Paper, Scissors:  " )
if player == computer :
    print("Tie")
elif player == "Rock":
    if computer == "Scissor":
        print("Rock smashes Scissor, You Win!")
    elif computer == "Paper":
        print("Paper covers Rock, You Loose!")
    elif computer == "Rock":
        print("Tie")
    else: print("Check Spelling")
elif player == "Paper":
    if computer == "Scissor":
        print("Scissors cut paper,You Loose!")
    elif computer == "Paper":
        print("Tie")
    elif computer == "Rock":
        print("Paper covers rock,You Win!")
    else: print("Check Spelling")
elif player == "Scissor":
    if computer == "Scissor":
        print("Tie")
    elif computer == "Paper":
        print("Scissor cuts Paper,You Win!") 
    elif computer == "Rock":
        print("Rock smashes Scissor,You Loose!")
    else: print("Check Spelling")
else:
        print("That's not a valid play. Check your spelling!")
 #player was set to True, but we want it to be False so the loop continues
player = False
computer = o[randint(0,2)]