import random
from art import logo

def game(lives):
    chosen_num=random.randint(1,100)
    
    print(f"You have {lives} attempts remaining to guess the number")
    while lives!=0:
        user_input=int(input("Make a guess: "))
        if user_input==chosen_num:
            print("Amazing! You won!")
            break
        elif user_input<chosen_num:
            print("Too low")
            lives-=1
            if lives==0:
                print("You lost! The number was {chosen_num}")
                break
            print(f"You have {lives} attempts remaining to guess the number")
        else:
            print("Too high like Snoop Dogg")
            lives-=1
            if lives==0:
                print("You lost! The number was {chosen_num}")
                break
            print(f"You have {lives} attempts remaining to guess the number")



print(logo)
print("\n")
print('''Welcome to the Number Guessing Game!
I'm thinking of a number between 1 and 100.
''')
difficulty=input("Choose a difficulty, 'easy' or 'hard': ").lower()

if difficulty=='easy':
    lives=10
    game(lives)
else:
    lives=5
    game(lives)