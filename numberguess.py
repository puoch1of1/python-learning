#let us import the libraries for the functions we are going to use
import math  # for mathematical functions
import random  # to generate random numbers 
import time   # for time related tasks

def main():  
    #read the user's inputs 
    lower_input = int(input("Enter the lower bound: "))
    upper_input = int(input("Enter the upper bound: "))

    #let's seed the random number generator
    random.seed(time.time())

    #generate the random number between the lower and upper bound
    x = random.randint(lower_input, upper_input)

    #calculate total chances based on the binary search principle
    total_chances = math.ceil(math.log(upper_input - lower_input + 1, 2))

    print(f"\n\tYou have only {total_chances} chances to guees the integer!\n")
    count = 0
    flag = False
    
    while count < total_chances:
        count += 1
        
        #the guessing number as input
        guess = int(input("Guess a number: "))

        #condition testing
        if x == guess:
            print(f"Congrats you did it in {count} try!")
            flag = True
            break
        elif x > guess:
            print("You have guessed too small!")
        else:
            print("You have guessed too high")

    if not flag:
                print(f"\n The number is {x}")
                print(f"\tBetter luck next time!")
if __name__ == "__main__":
        main()