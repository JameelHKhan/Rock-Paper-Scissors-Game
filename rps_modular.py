# Module 3 Assignment, part 2
# Jameel H. Khan

# declaring variables and assigning them to initial values
player1Selection = -1
player2Selection = -1
player1Win = 0
player2Win = 0
gameTie = 0
player1Invalid = 0
player2Invalid = 0
gameNumber = 0      # tracks current iteration of game for output purposes

n = range(10)       # set number of game durations with each run

for games in n:
    # obtain user input, convert to lowercase for validity test
    player1Input = input("Player 1: Enter your selection: ")
    player1Input = player1Input.lower()
    # Validity tests for player 1 selection
    while (player1Selection != 0
           or player1Selection != 1
           or player1Selection != 2):
        if player1Input == "rock":
            player1Selection = 0
            break
        elif player1Input == "paper":
            player1Selection = 1
            break
        elif player1Input == "scissors":
            player1Selection = 2
            break
        else:
            player1Invalid += 1
            print("Player 1 entered an invalid gesture!")
            player1Input = input("\nPlayer 1: Enter your selection: ")
            continue
    player2Input = input("Player 2: Enter your selection: ")
    player2Input = player2Input.lower()
    # Validity tests for player 2 selection
    while (player2Selection != 0
           or player2Selection != 1
           or player2Selection != 2):
        if player2Input == "rock":
            player2Selection = 0
            break
        elif player2Input == "paper":
            player2Selection = 1
            break
        elif player2Input == "scissors":
            player2Selection = 2
            break
        else:
            player2Invalid += 1
            print("Player 2 entered an invalid gesture!")
            player2Input = input("\nPlayer 2: Enter your selection: ")
            continue
    # Tie, winner, loser determination using modular arithmetic
    gameResult = (player1Selection - player2Selection) % 3
    if gameResult == 0:
        gameTie += 1
        gameNumber += 1
        print("Game #" + str(gameNumber) + ": Tie game!\n")
    elif gameResult == 2:
        player2Win += 1
        gameNumber += 1
        print("Game #" + str(gameNumber) + ": Player 2 Wins!\n")
    elif gameResult == 1:
        player1Win += 1
        gameNumber += 1
        print("Game #" + str(gameNumber) + ": Player 1 Wins!\n")

# output of game results: player wins, ties, & invalid games
print("Player 1 won " + str(player1Win) + " games, Player 2 won "
      + str(player2Win) + " games, and there were " + str(gameTie)
      + " ties. Player 1 made " + str(player1Invalid)
      + " invalid gestures and Player 2 made "
      + str(player2Invalid) + " invalid gestures.")
