#Khansole Academy

import random

def main():
    print("Khansole Academy")
    corrects = 0
    while (corrects < 3):
        x = random.randint(10,99)
        y = random.randint(10,99)
        print("What is", x, "+", y, "?")
        answer = input("Your answer: ")
        if int(answer) == (x + y):
           corrects += 1
           print("Correct! You've gotten", corrects, "correct in a row.")
        else:
           print("Incorrect. \nThe expected answer is", x + y)
           corrects = 0
    print("Congratulations! You mastered addition.")
     
if __name__ == '__main__':
    main()
