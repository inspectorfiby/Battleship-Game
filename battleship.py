from random import randint

#Initializing the board
board = []

for x in range(5):
    board.append(["O"] * 5)

#Method to print the board
def print_board(board):
    for row in board:
        print " ".join(row)

def random_row(board):
    return randint(0, len(board) - 1)

def random_col(board):
    return randint(0, len(board[0]) - 1)

if __name__ == '__main__':
	print "Let's play Battleship!"
	print_board(board)
	ship_row = random_row(board)
	ship_col = random_col(board)
	board[ship_row][ship_col] = "S"
	turn_count =0
	#Core game logic
	while turn_count<3:
		print "Turn", turn_count + 1
		guess_row = int(raw_input("Guess Row:"))
		guess_col = int(raw_input("Guess Col:"))
		
		#Guessed the right cell
		if guess_row == ship_row and guess_col == ship_col:
			print "Congratulations! You sunk my battleship!"
			break
		else:
			#When guess is out of board
			if (guess_row < 0 or guess_row > 4) or (guess_col < 0 or guess_col > 4):
				print "Doesn't Count, that's not even in the ocean."
			#Does'nt count if previously guessed
			elif(board[guess_row][guess_col] == "X"):
				print "You guessed that one already."
				turn = turn_count - 1
			#Wrong Guess
			else:
				print "You missed my battleship!"
				board[guess_row][guess_col] = "X"
				turn_count += 1
		#Max turn_count achieved
		if turn_count == 3:
			print "Game Over"
			print turn_count + 1
			print_board(board)