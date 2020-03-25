import numpy as np

rand=np.random.randint(1,50,1)
number=int(input("enter number which u think is correct"))
def guess(rand,number):b
    
    for i in range(3):
        if(number>rand[0] and number<100):
            print("the number guessed is larger..please think smaller number")
            number=int(input("enter number which u think is correct"))
        elif(number<rand[0] and number>0):
            print("the number guessed is smaller..please think larger number")
            number=int(input("enter number which u think is correct"))
        elif(number>100 or number<0):
            print("the number should be less than 100 or greater than 0")
            number=int(input("enter number which u think is correct"))
    if(number==rand[0]):
        print("u guessed it right")
            
    if(number!=rand[0]):        
        print("sorry u lost 9 chances the number is",rand)      
guess(rand,number)
# Number Guessing
#Make a program which randomly chooses a number to guess and
#then the user will have a few chances to guess the number correctly.
#In each wrong attempt, the computer will give a hint that the
#number is greater or smaller than the one you have guessed.


