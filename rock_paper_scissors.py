import random

done = False

# Starting messages
while done == False:
    print("Rock Paper Scissors!")
    print("--------------------------------")

    # Get difficulty
    while True:
        response = input("Enter difficulty (easy, medium, hard): ")
        if response == "easy":
            difficulty = "easy"
            break
        elif response == "medium":
            difficulty = "medium"
            break
        elif response == "hard":
            difficulty = "hard"
            break
        else:
            print("that's not a difficulty dummy!")

    # Choose move
    while True:
        move = input("Choose rock, paper, or scissors: ")
        if move == "rock" or move == "paper" or move == "scissors":
            break
        else:
            print("that's not an option dummy!")

    # AI choosing move
    if difficulty == "easy":
        if move == "rock":
            ai_move = "scissors"
        elif move == "paper":
            ai_move = "rock"
        elif move == "scissors":
            ai_move = "paper"
    elif difficulty == "medium":
        rng = random.randint(1, 3)
        if rng == 1:
            ai_move = "rock"
        elif rng == 2:
            ai_move = "paper"
        elif rng == 3:
            ai_move = "scissors"
    elif difficulty == "hard":
        if move == "rock":
            ai_move = "paper"
        elif move == "paper":
            ai_move = "scissors"
        elif move == "scissors":
            ai_move = "rock"

    # Some messages
    print()
    print("You picked:\t", move)
    print("AI picked:\t", ai_move)
    print()

    # Determine winner
    if move == ai_move:
        print("Tie!")
    elif move == "rock":
        if ai_move == "paper":
            print("You lose!")
        elif ai_move == "scissors":
            print("You win!")
    elif move == "paper":
        if ai_move == "rock":
            print("You win!")
        elif ai_move == "scissors":
            print("You lose!")
    elif move == "scissors":
        if ai_move == "rock":
            print("You lose!")
        elif ai_move == "paper":
            print("You win!")

    # End
    print("--------------------------------")
    while True:
        next = input("Enter \"r\" to replay or \"q\" to quit: ")
        if next == "q":
            done = True
            break
        elif next == "r":
            print()
            break
        else:
            print("That's not an option dummy!")