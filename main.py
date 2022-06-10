#Creating the game of Rock, Papers, Scissors!

import random


#Printing Intro for the game
print ("\n                    Welcome to Kaptain-T's Rock-Paper-Scissors Game! \n\n Kindly read below the instructions for the game before you begin. \n")
print ("  At the start of the game, you are to make a selection - R for Rock, P for Paper, S for Scissors. \n  The game is played between you and the computer. The first to get three points wins the game. \n  Note: One point per round but no point for a tie!")
computeroptions = ["Rock", "Paper", "Scissors"]
optionsdict = {"R" : "Rock", "P" : "Paper", "S" : "Scissors"}
options_value = {'R': 2, 'S':1, 'P':0}



#making a function for the game to run
def thegame():
    score = {"Player": 0, "CPU": 0}
    stop = 3
    while True:
        userchoice = input("Rock! Paper! Scissors! Shoot! ... ")
        userchoice = userchoice.upper()

        if userchoice in optionsdict.keys():
            userchoicevalue = options_value[userchoice]
            thechoice = optionsdict[userchoice]

            computerchoice = random.choice(computeroptions)
            computerchoicevalue = options_value[computerchoice[0]]

            decision = userchoicevalue - computerchoicevalue

            print ("Player (",thechoice,") : CPU (",computerchoice,")")

            if (decision == 1) or (decision == -2):
                print ("Player Wins!")
                score["Player"] += 1
                print ("Player: %1d, CPU: %1d \n" % (score["Player"], score["CPU"]))
                if stop in score.values():
                    key_list = list(score.keys())
                    val_list = list(score.values())
                    position = val_list.index(3)
                    if key_list[position] == "Player":
                        print ("You won this round. Congratulations!")
                        again()
                        break
                    else:
                        print (key_list[position], "wins this round. Better luck next time.")
                        again()
                        break
                else:
                    continue
            elif decision == 0:
                print("It's a Tie! \n")
            else:
                print ("CPU Wins!")
                score["CPU"] += 1
                print ("Player: %1d, CPU: %1d \n" % (score["Player"], score["CPU"]))
                if stop in score.values():
                    key_list = list(score.keys())
                    val_list = list(score.values())
                    position = val_list.index(3)
                    if key_list[position] == "Player":
                        print ("You won this round. Congratulations!")
                        again()
                        break
                    else:
                        print (key_list[position], "wins this round. Better luck next time.")
                        again()
                        break
                else:
                    continue

        else:
            print("Invalid Entry! Again")

    
def again():
    print("Want to play again?\n")
    playagain = input("Y for Yes, N for No: ")
    playagain = playagain.upper()
    if playagain == "Y":
        print ("Great! Let's go again! \n")
        thegame()

    elif playagain == "N":
        print ("\n Alright. Thanks for playing. Bye!")
        

    else:
        print("That's not what I asked. Y OR N?")
        again()
        
#initialising a start
def Welcome():
    select = input("\n                 Shall We Begin? \n\nEnter Yes or No:   ")
    select = select.upper()
    if select == "YES":
        print("Lovely! Lets play...")
        thegame()

    elif select == "NO":
        print ("\n You really don't want to play huh? Alright then. Bye!")

    else:
        print("\nHuh? Invalid reponse. Reply Yes OR No!")
        Welcome()

Welcome()