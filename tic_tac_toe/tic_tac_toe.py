from board import Board
import time

# This function is the miniMax function. It takes in the current board and the current player's turn ('x' or 'o') and returns it's score
def miniMax(board, player):

    # Test for win
    results = board.DidPlayerWin(False)
    if results != ' ':
        # Returns values
        if results == 'x':
            return -1
        if results == 'o':
            return 1
        if results == 't':
            return 0

    # sets best
    if player == 'x':
        # Trying to maximize
        best = 1
    else:
        # Trying to minimize
        best = -1

    # Loops through all possible moves
    for x in range(0, 3):
        for y in range(0, 3):
            # Test if the space is not taken
            if board.GetMark(x, y) == ' ':
                # Take the space
                board.SetMark(x, y, player)

                # Finds the best score possible
                # Player, min
                if player == 'x':
                    best = min(best, miniMax(board, 'o'))
                # Computer, max
                if player == 'o':
                    best = max(best, miniMax(board, 'x'))

                # Undos
                board.SetMark(x, y, ' ')
            
    return best


def main():
    # Creates the board
    drawBoard = Board()

    # Loop for updates
    playerTurn = True # Indicates if it's the first players turn
    endGame = False # Indicates if its the end of the game
    while endGame == False:
        drawBoard.Update()

        # Test if we got a click
        if drawBoard.GotClick:

            # Check for a valid click
            if drawBoard.GetCurrMark() == ' ':
                
                # Player's turn
                drawBoard.Mark(playerTurn)
                playerTurn = False

                # Finds the next best move with minimax
                bestScore = -10
                bestMove = [-1, -1]
                for x in range(0, 3):
                    for y in range(0, 3):
                        if drawBoard.GetMark(x, y) == ' ':
                            
                            # Runs the minimax
                            drawBoard.SetMark(x, y, 'o')
                            score = miniMax(drawBoard, 'x')
                            drawBoard.SetMark(x, y, ' ')

                            # Test if we hit a new score
                            if score > bestScore:
                                bestScore = score
                                bestMove = [x, y]

                # Test if it is not the last turn
                if (bestScore != -10):
                    # Draws
                    drawBoard.SetCurrCoords(bestMove[0], bestMove[1])
                    drawBoard.Mark(playerTurn)
                    playerTurn = True

                # Checks for a player win
                winningPlayer = drawBoard.DidPlayerWin()
                if winningPlayer != ' ':
                    endGame = True

            # Prints error msg
            else:
                print("Invalid space chosen")

    # Updates the board for the red strike
    drawBoard.Update()

    # Checks for tie
    if winningPlayer != 't':
        print("The winner is " + winningPlayer + "!")
    else:
        print("Its a tie!")
    
    # Pauses before closing
    time.sleep(2)

if __name__ == "__main__":
    main()