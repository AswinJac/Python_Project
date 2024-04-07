import random
import art
print(art.logo)
print("Welcome to Number Guessing Game!\n")
print("I'am thinking of a number between 1 and 100\n")
rand=random.randint(1,100)
print(rand)
def hard():
    life=5
    for i in range (life):
        print("You have ",life-i," lifes left\n")
        no=int(input("Enter a guess\n"))
        if no<rand:
            print("TOO LOW \n")
        elif no>rand:
            print("TOO HIGH\n")
        else:
            print(art.win)
            print("Your Number was ",rand)
            return
    print(art.lost)            
def easy():
   life=10
   for i in range (life):
        print("You have ",life-i," lifes left\n")
        no=int(input("Enter a guess\n"))
        if no<rand:
            print("TOO LOW \n")
        elif no>rand:
            print("TOO HIGH\n")
        else:
            print(art.win)
            print("Your number was ",rand)
            return
   print(art.lost) 
choice=input("Choose a difficulty,easy or hard\n")
if choice=='easy':
    easy()
elif choice=='hard':
    hard()
else:
    print("Invalid Choice")
