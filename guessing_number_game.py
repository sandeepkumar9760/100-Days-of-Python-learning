import random

random_num = random.randint(1,100)

user_num = int(input("Guess your number: "))
count = 1
while user_num!=random_num:
    if user_num<random_num:
        count += 1
        print("guess higher: ")
        user_num = int(input("Choose your next guess: "))
    else:
        count+=1
        print("guess lower.")
        user_num = int(input("Choose your next guess: "))
 
print(f"HURRAY YOU WON ! you took {count} guesses to guess the number.")
