def check_guess(guess, answer):
    global score
    still_guessing = True
    attempt = 0
    while still_guessing and attempt < 3:
        if guess.lower() == answer.lower():
            print("Correct Answer!")
            score = score + 1
            still_guessing = False
        else:
            if attempt < 2:
                guess = input("Sorry that is the wrong answer, please try again:   ")
            attempt = attempt + 1
    if attempt == 3:
        print("The correct answer is the",answer )
    
score = 0
print("Guess the Animal")
guess1 = input("Which bear lives at the North Pole? ")
check_guess(guess1, "Polar Bear")
guess2 = input("Which is the fastest land animal? ")
check_guess(guess2, "Cheetah")
guess3 = input("Which is the largest aquatic animal? ")
check_guess(guess3, "Blue Whale")
guess4 = input("Which is the smallest animal? ")
check_guess(guess4, "Etruscan shrew")
guess4 = input("Which is the fastest bird? ")
check_guess(guess4, "Peregrine Falcon")
print("Your score is "+ str(score, ))