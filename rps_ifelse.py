# Module 3 Assignment, part 1
# Jameel H. Khan

# declaring variables and assigning them to initial values
invalidGame = 0
player1Win = 0
player2Win = 0
gameTie = 0
gameNumber = 0  # tracks current iteration of game for output purposes

n = range(7)    # set number of game durations with each run

for games in n:
    # obtain Player 1 user input, convert to lowercase for validity test
    player1Selection = input("Player 1: Enter your selection: ")
    player1Selection = player1Selection.lower()
    # Validity test for Player 1
    if (player1Selection == "rock"
            or player1Selection == "paper"
            or player1Selection == "scissors"):
        pass
    else:
        invalidGame += 1
        gameNumber += 1
        print("Game #" + str(gameNumber) +
              ": Player 1 made an incorrect selection. Invalid game!\n")
        continue
    # obtain Player 2 user input, convert to lowercase for validity test
    player2Selection = input("Player 2: Enter your selection: ")
    player2Selection = player2Selection.lower()
    # Validity test for Player 2
    if (player2Selection == "rock"
            or player2Selection == "paper"
            or player2Selection == "scissors"):
        pass
    else:
        invalidGame += 1
        gameNumber += 1
        print("Game #" + str(gameNumber) +
              ": Player 2 made an incorrect selection. Invalid game!\n")
        continue
    # After successful validation, the following if/elif code block determines
    # a tie game or a winner. The first if statement determines a tie based on
    # any pairings of rock, paper, or scissors
    if player1Selection == player2Selection:
        gameTie += 1
        gameNumber += 1
        print("Game #" + str(gameNumber) + ": Tie game!\n")
    # The next six elif statements determine winner/loser
    # rock vs paper (P2 win)
    elif player1Selection == "rock" and player2Selection == "paper":
        player2Win += 1
        gameNumber += 1
        print("Game #" + str(gameNumber) + ": Player 2 Wins!\n")
    # rock vs scissors (P1 win)
    elif player1Selection == "rock" and player2Selection == "scissors":
        player1Win += 1
        gameNumber += 1
        print("Game #" + str(gameNumber) + ": Player 1 Wins!\n")
    # paper vs rock (P1 win)
    elif player1Selection == "paper" and player2Selection == "rock":
        player1Win += 1
        gameNumber += 1
        print("Game #" + str(gameNumber) + ": Player 1 Wins!\n")
    # paper vs scissors (P2 win)
    elif player1Selection == "paper" and player2Selection == "scissors":
        player2Win += 1
        gameNumber += 1
        print("Game #" + str(gameNumber) + ": Player 2 Wins!\n")
    # scissors vs rock (P2 win)
    elif player1Selection == "scissors" and player2Selection == "rock":
        player2Win += 1
        gameNumber += 1
        print("Game #" + str(gameNumber) + ": Player 2 Wins!\n")
    # scissors vs paper (P1 win)
    elif player1Selection == "scissors" and player2Selection == "paper":
        player1Win += 1
        gameNumber += 1
        print("Game #" + str(gameNumber) + ": Player 1 Wins!\n")

# output of game results: player 1 wins, player 2 wins, ties, & invalid games
print("Player 1 won " + str(player1Win) + " games, Player 2 won "
      + str(player2Win) + " games, and there were " + str(gameTie)
      + " ties. There was a total of " + str(invalidGame) + " invalid games.")
