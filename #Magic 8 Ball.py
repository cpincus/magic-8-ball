#Magic 8 Ball
#Celia Pincus 
#1/19/24 

#Init
Reponses = ["Yes, definitely", "Without a doubt", "Signs point to yes!", "Of course!", "Ask again later", "Concentrate and try again", "Very doubtful", "My sources say no", "Definitely not", "Most certainly not!"]
import random 

#Functions
def eightBall(): 
    while True:
        question = input("Ask me a yes or no question")
        if question.endswith("?"):
            print(random.choice(Reponses))
            ans = input("Would you like to ask another question? (Y or N)")
            if ans == ("Y"):
                eightBall()
            if ans == ("N"):
                break
        else:
            print("Please retry your question with a question mark")
            eightBall()
        
#Main 
    
eightBall()