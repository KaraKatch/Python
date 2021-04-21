'''
This program is going to ask basic trivia learned n high school. You will answer 
either a,b, or c to the following questions. The program will tell you if you
are correct, if not it will tell you the right answer. You will them be given
your score out of four. 

Author: Kara Katch
'''

score = 0

x = input("What is the powerhouse of the cell? A) Mitochondria B)Nucleus C)Ribsome")
answer = "A"
if(x.upper() == "A"):
    print ("Correct")
    score = score + 1
else:
    print ("incorrect, the correct answer is A")  


x = input("How many states comprise the United States? A) 13 B) 45 C) 50")
answer = "C"
if(x.upper() == "C"):
    print ("Correct")
    score = score + 1 
else:
    print ("incorrect, the correct answer was C")

x = input("In y = mx + b, what does m stand for? A)slope B)output C)I don't understand math")
answer = "A"
if(x.upper() == "A"):
    print("Correct")
    score = score + 1
else:
    print("incorrect, the answer was A")

x = input("In English, a person or thing is called: A)verb B)adjective C)noun")
answer = "C"
if(x.upper() == "C"):
    print("Correct")
    score = score + 1
else:
    print("incorrect, the answer was C")

p = score
if(p == 1):
    print ("You got 1/4, or 25%")
elif(p == 2):
    print("You got 2/4, or 50%")
elif(p == 3):
    print("You got 3/4, or 75%")
else:
    print("You got 4/4, or 100%")

