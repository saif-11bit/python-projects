import random

CORRECT_NUM = random.randint(1,100)

playing = True

MIN_GUESS = 1
MAX_GUESS = 100

while playing:
    try:
        user_guess = int(input(f"Guess the number b/w {MIN_GUESS} to {MAX_GUESS}: "))

        if user_guess < CORRECT_NUM and user_guess >= MIN_GUESS and user_guess <= MAX_GUESS:
            MIN_GUESS = user_guess
            print(f"Your Guess is less than Correct one\nHint:b/w {MIN_GUESS} to {MAX_GUESS}")
        
        elif user_guess > CORRECT_NUM and user_guess >= MIN_GUESS and user_guess <= MAX_GUESS:
            MAX_GUESS = user_guess
            print(f"Your Guess is greater than Correct one\nHint:b/w {MIN_GUESS} to {MAX_GUESS}")
        
        elif user_guess == CORRECT_NUM:
            print(f"Hurray!!!\nWon the game\nCorrect guess:{CORRECT_NUM}")
            playing = False

        else:
            print("Please input valid guess!!")
    
    except Exception as e:
        print("Please input valid guess!!")