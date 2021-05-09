'''
This program will run a rock, paper, scissors game. The user will play against 
the computer. You can play as many games as you like and can quiet at any time.

Created on May 4, 2021
@author: Kara Katch
'''
import random


#Make a boolean variable called keepPlaying to track weather they wan to
#keep playing and set it to True.
keepPlaying = True
#LOOP:Make a game loop that continues while keepPlaying is true.
while(keepPlaying):   
    #print out a statement to welcome the user to the game.
    print("Welcome to Rock Paper Scissors!")
    print("Best two out of three. Press 'q' to quit")
    #Make variable called userScore and cpuScore to keep track scores, set to 0
    cpuScore = 0
    userScore = 0
    #LOOP:Make a round loop that continues while the userScore or cpuScore is less 
    #than 2.
    while(userScore < 2 and cpuScore < 2):
        #use input() to get choice from the user rock, paper, scissors, q.
        #Store choice in variable. Use .lower() to make users choice all 
        #lower case. 
        user = input("Please choose (Rock, Paper, Scissors): ")
        #Make list of choices, than use random.choice() to get random choice for 
        #the cpu, store choice in a variable. 
        list= ["rock", "paper","scissors"]
        cpu = random.choice(list)
        print(cpu)
        #note you will have to compare the user and cpu choice to rock, paper, 
        #scissors separately and combine with logical operators. EXAMPLE
        '''
        if((user == "rock" and cpu == "rock") or (user == "paper" and cpu== "paper") 
        or (user == "scissors" and cpu == "scissors" )):
        
            print("DRAW") 
            print("User:" + str(userScore) + "CPU:" + str(cpuScore)
        '''
        #if the user won, add one to the users score, then print out the scores
        #"User: [#], CPU: [#]"
        if(user.lower() == "rock" and cpu == "scissors") or (user == "paper" and
         cpu == "rock") or (user == "scissors" and cpu == "paper"):
            print("You won")
            print("User: " + str(1) + " CPU: " + str(0))
        
        #else if (elif) the computer won, add one to the computer's score, then
        #print out the scores...
        elif(user.lower() == "rock" and cpu == "paper") or (user == "paper" and 
        cpu == "scissors") or (user == "scissors" and cpu == "rock"):
            print("CPU won")
            print("User: " + str(0) + " CPU: " + str(1)) 
        #else if it is a draw, print ("Draw"), then print out the scores...
        elif(user.lower() == "rock" and cpu == "rock") or (user == "paper" and 
        cpu == "paper") or (user == "scissors" and cpu == "scissors" ):
            print("Draw")
            print("User: " + str(userScore) + " CPU: " + str(cpuScore))
        #else if the user entered 'q', then end the round and the game loop. 
        #use the break statement to end the round. Make keepPlay equals False.
        elif(user.lower() == 'q'):
            break
            keepPlaying = False
            
            
            
        #else the user didn't enter an excepted input, print "Not an option,
        #try again."
        else:
            print("Not and option, try again")
    
    #print out the thank you message
    #print out who won:
    if(user.lower() == 'q'):
        print("Thanks for playing")
    #if the user score is 2, the the user won    
    if(userScore >= 2):
        print("You won!")
    #elif the cpuScore is 2, then the cpu won.
        #code
    elif(cpuScore >= 2):
        print("CPU won")
    #print out the final scores
    print("User: " + str(userScore) + " CPU: " + str(cpuScore))
