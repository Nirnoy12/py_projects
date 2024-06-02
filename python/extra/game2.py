import random
end_num = input("Enter the number you want to be your boundary in this game: ")
end_num = int(end_num)
if end_num >= 0:
    print("\nLet's start the game.")
    
else:
    print("PLEASE TYPE A NUMBER GREATER THAN 0 NEXT TIME.\n")
    quit()
        
random_no = random.randint(0,end_num)
guesses = 0

while True:
    guesses += 1
    ug = input("Make a guess: ")
    if ug.isdigit():
        ug = int(ug)
    else:
        print('Please type a number next time.')
        continue
    if ug == random_no:
        print("You got it! ")
        break
    elif ug > random_no:
        print("You were above the random number")
    else:
        print("You were below the random number")

print("You got it in", guesses, "guesses")
        