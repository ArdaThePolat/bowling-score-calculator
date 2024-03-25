import random

#We get the rolls with this function. 
def get_rolls():
    roll1=0
    roll2=0
    #Flag to understand if input is as we wanted. 
    isInputFalse = True
    while isInputFalse:
        roll1 = (input("Pins: "))
        if roll1.isnumeric():
            roll1=int(roll1)
            #We check the conditions. 
            if roll1 >= 0 and roll1 <= 10:
                if roll1 == 10:
                    return [roll1,roll2]
                isInputFalse = False
            else:print("Invaid input...")
        else:print("Invaid input...")
    isInputFalse = True
    while isInputFalse:
        roll2 = (input("Pins: "))
        #Same here for 2nd roll. 
        if roll2.isnumeric():
            roll2=int(roll2)
            if roll2 >= 0 and roll2 <= 10 and roll1+roll2 <= 10:
                return [roll1,roll2]    
            else:print("Invaid input...")
        else:print("Invaid input...")

#This function is to decide who is gonna start first. 
def get_random_player():
    temp = random.randint(0,1)
    if temp==0:
        return "A"
    else:
        return "B"

def main():
    #We define the variables that we're going to need. 
    strikeRounds = []
    spareRounds = []
    A_BallScores = []
    B_BallScores = []
    A_TotalScores = []
    B_TotalScores = []
    #Round counter to count and understand which round we are in
    RoundCounter=20
    #We get the first player. 
    player = get_random_player()
    while RoundCounter > 0:
        print("Player",player,"rolls...")
        #Every round we get the rolls that we're gonna append to our lists. 
        rolls = get_rolls()
        #Checks the condition to understand which player's turn is this
        #round and to make the calculations according to their values in their lists. 
        if player == "A":
            #Checks if the roll before this one was 'spare' if so,
            #checks the conditions and makes the calculations to
            #add the values into the lists. 
            for j in spareRounds:
                if RoundCounter+2 == j:
                    if j-2 in strikeRounds and RoundCounter == 1 or RoundCounter == 2:
                        A_TotalScores.append(A_TotalScores[-1]+20)
                        spareRounds[spareRounds.index(j)]=24 
                    elif (rolls[0] != 10):
                        if len(A_TotalScores) == 0:
                            A_TotalScores.append(rolls[0]+10)
                        else:
                            A_TotalScores.append(A_TotalScores[-1]+rolls[0]+10)
                        spareRounds[spareRounds.index(j)]=24 
                    else:
                        if len(A_TotalScores) == 0:
                            A_TotalScores.append(20)
                        else:
                            A_TotalScores.append(A_TotalScores[-1]+20)
                        spareRounds[spareRounds.index(j)]=24 
            
            #Same here for the strike rounds with one difference:
            #if the round after the one which our player striked is
            #strike again, our code waits for the next round to calculate
            #the rolls. If not, then it gets both roll1 and roll2 and add
            #them to our list.
            for i in strikeRounds:
                if RoundCounter+2 == i and rolls[0] != 10:
                    if len(A_TotalScores) == 0:
                        A_TotalScores.append(rolls[0] + rolls[1] + 10)
                    else:
                        A_TotalScores.append(A_TotalScores[-1] + rolls[0] + rolls[1] + 10)
                    strikeRounds[strikeRounds.index(i)]=24
                elif RoundCounter+4 == i:
                    if len(A_TotalScores) == 0:
                        A_TotalScores.append(rolls[0] + 20)
                    else:
                        A_TotalScores.append(A_TotalScores[-1] + rolls[0] + 20)
                    strikeRounds[strikeRounds.index(i)]=24

            #If roll1 is 10 then it is a strike. 
            if rolls[0] == 10:
                A_BallScores.append(rolls[0])
                strikeRounds.append(RoundCounter)
                #If it is the last round, we give the player 2 more chance
                #because he/she made a strike. 
                if RoundCounter == 1 or RoundCounter == 2:
                    isInputFalse = True
                    while isInputFalse:
                        roll3 = input("Pins: ")
                        if roll3.isnumeric():
                            roll3=int(roll3)
                            if roll3 >= 0 and roll3 <= 10:
                                A_BallScores.append(roll3)
                                isInputFalse = False   
                            else:print("Invaid input...")
                        else:print("Invaid input...")
                    isInputFalse = True
                    while isInputFalse:
                        roll4 = input("Pins: ")
                        if roll4.isnumeric():
                            roll4=int(roll4)
                            if roll4 >= 0 and roll4 <= 10:
                                A_BallScores.append(roll4)
                                isInputFalse = False   
                            else:print("Invaid input...")
                        else:print("Invaid input...")
                    A_TotalScores.append(A_TotalScores[-1]+10+roll3+roll4)
            #If the sum of both rolls is equal to 10, then it is spare.
            elif rolls[0]+rolls[1] == 10: 
                A_BallScores.extend(rolls)
                spareRounds.append(RoundCounter)
                #Here we check if player made spare in last round if it is,
                #we give him/her 1 more chance to roll. 
                if RoundCounter == 1 or RoundCounter == 2:
                    isInputFalse = True
                    while isInputFalse:
                        roll3 = input("Pins: ")
                        if roll3.isnumeric():
                            roll3=int(roll3)
                            if roll3 >= 0 and roll3 <= 10:
                                A_BallScores.append(roll3)
                                isInputFalse = False   
                            else:print("Invaid input...")
                        else:print("Invaid input...")
                    A_TotalScores.append(A_TotalScores[-1]+rolls[0]+rolls[1]+roll3)
            #If it's not strike or neither spare, we just add them to the list. 
            else:
                A_BallScores.extend(rolls)
            
            #Again if it is a normal round, we just add the values to our list of total scores. 
            if (rolls[0]+rolls[1] != 10):
                if len(A_TotalScores) == 0:
                    A_TotalScores.append(rolls[0]+rolls[1])
                else:
                    A_TotalScores.append(A_TotalScores[-1]+rolls[0]+rolls[1])
            #We change the player for next round. 
            player="B"
            #We format and print the results. 
            print("Ball scores: ",end="")
            for i in A_BallScores:
                print(i,end=" ")
            print()
            print("Total scores: ",end="")
            for j in A_TotalScores:
                print(str(j)+" | ",end="")
            for k in range(9-len(A_TotalScores)):
                print(" | ",end="")
            print()



        #Checks if it is B's turn and uses the same methods as in player A's section.
        elif player == "B":
            
            for j in spareRounds:
                if RoundCounter+2 == j:
                    if j-2 in strikeRounds and RoundCounter == 1 or RoundCounter == 2:
                        B_TotalScores.append(B_TotalScores[-1]+20)
                        spareRounds[spareRounds.index(j)]=24 
                    elif (rolls[0] != 10):
                        if len(B_TotalScores) == 0:
                            B_TotalScores.append(rolls[0]+10)
                        else:
                            B_TotalScores.append(B_TotalScores[-1]+rolls[0]+10)
                        spareRounds[spareRounds.index(j)]=24 
                    else:
                        if len(B_TotalScores) == 0:
                            B_TotalScores.append(20)
                        else:
                            B_TotalScores.append(B_TotalScores[-1]+20)
                        spareRounds[spareRounds.index(j)]=24 
                        
            for i in strikeRounds:
                if RoundCounter+2 == i and rolls[0] != 10:
                    if len(B_TotalScores) == 0:
                        B_TotalScores.append(rolls[0] + rolls[1] + 10)
                    else:
                        B_TotalScores.append(B_TotalScores[-1] + rolls[0] + rolls[1] + 10)
                    strikeRounds[strikeRounds.index(i)]=24
                elif RoundCounter+4 == i:
                    if len(B_TotalScores) == 0:
                        B_TotalScores.append(rolls[0] + 20)
                    else:
                        B_TotalScores.append(B_TotalScores[-1] + rolls[0] + 20)
                    strikeRounds[strikeRounds.index(i)]=24

            if rolls[0] == 10:
                B_BallScores.append(rolls[0])
                strikeRounds.append(RoundCounter)
                if RoundCounter == 1 or RoundCounter == 2:
                    isInputFalse = True
                    while isInputFalse:
                        roll3 = input("Pins: ")
                        if roll3.isnumeric():
                            roll3=int(roll3)
                            if roll3 >= 0 and roll3 <= 10:
                                B_BallScores.append(roll3)
                                isInputFalse = False   
                            else:print("Invaid input...")
                        else:print("Invaid input...")
                    isInputFalse = True
                    while isInputFalse:
                        roll4 = input("Pins: ")
                        if roll4.isnumeric():
                            roll4=int(roll4)
                            if roll4 >= 0 and roll4 <= 10:
                                B_BallScores.append(roll4)
                                isInputFalse = False   
                            else:print("Invaid input...")
                        else:print("Invaid input...")
                    B_TotalScores.append(B_TotalScores[-1]+10+roll3+roll4)
            elif rolls[0]+rolls[1] == 10:
                B_BallScores.extend(rolls)
                spareRounds.append(RoundCounter)
                if RoundCounter == 1 or RoundCounter == 2:
                    isInputFalse = True
                    while isInputFalse:
                        roll3 = input("Pins: ")
                        if roll3.isnumeric():
                            roll3=int(roll3)
                            if roll3 >= 0 and roll3 <= 10:
                                B_BallScores.append(roll3)
                                isInputFalse = False   
                            else:print("Invaid input...")
                        else:print("Invaid input...")
                    B_TotalScores.append(B_TotalScores[-1]+rolls[0]+rolls[1]+roll3)
            else:
                B_BallScores.extend(rolls)
                
            if (rolls[0]+rolls[1] != 10):
                if len(B_TotalScores) == 0:
                    B_TotalScores.append(rolls[0]+rolls[1])
                else:
                    B_TotalScores.append(B_TotalScores[-1]+rolls[0]+rolls[1])
            player="A"
            print("Ball scores: ",end="")
            for i in B_BallScores:
                print(i,end=" ")
            print()
            print("Total scores: ",end="")
            for j in B_TotalScores:
                print(str(j)+" | ",end="")
            for k in range(9-len(B_TotalScores)):
                print(" | ",end="")
            print()

        #We change the value of out round counter to keep the game going. 
        RoundCounter-=1

    #we check if there is a winner and which player it is.
    if A_TotalScores[len(A_TotalScores)-1] > B_TotalScores[len(B_TotalScores)-1]:
        print("Winner is player A.")
    elif A_TotalScores[len(A_TotalScores)-1] < B_TotalScores[len(B_TotalScores)-1]:
        print("Winner is player B.")
    else:
        print("There is no winner :)")
    
#We call the main function for our program to work    
main()