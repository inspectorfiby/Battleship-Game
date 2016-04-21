from random import randint

#Method to print the board
def print_board(board):
    for row in board:
        print " ".join(row)

def random_row(board):
    return randint(0, len(board) - 1)

def random_col(board):
    return randint(0, len(board[0]) - 1)

if __name__ == '__main__':
	#Initializing the board
	board = []
	input_flag=False
	guess_row = guess_col=-1
	for x in range(10):
		board.append(["O"] * 10)
	print "Let's play Battleship! Who can sink the battleship first?"
	
	print_board(board)
	ship_row = random_row(board)
	ship_col = random_col(board)
	board[ship_row][ship_col] = "S"
	
	#Players names input
	p1_name = str(raw_input("Player 1 is:"))
	p2_name = str(raw_input("Player 2 is:"))
	
	#Telling which player is playing in a certain turn
	def player(n):
		if n % 2 == 0: 
			return p1_name
		else:
			return p2_name
	turn_count = 0
	
	#Telling which player has guessed a certain spot
	guess = {"X": p1_name, "Y": p2_name, "O": "no one"}
	#Core game logic
	while turn_count < 8:
			print "Turn", (turn_count- (turn_count % 2)) / 2 + 1, "for", player(turn_count)
			while input_flag == False:
				guess_row = raw_input("Guess Row:")
				guess_col = raw_input("Guess Col:")
				if guess_row.isdigit() and guess_col.isdigit():
					guess_col = int(guess_col)
					guess_row = int(guess_row)
					input_flag = True
					break
				else:
					print "invalid inputs, enter again!"
					
			#Guessed the right cell
			if guess_row == ship_row and guess_col == ship_col:
				print "No way! You sunk my battleship! The winner is", player(turn_count), "!"
				break
			else:
				#Doesn't count when guess is out of board
				if (guess_row < 0 or guess_row > 9) or (guess_col < 0 or guess_col > 9):
					print "This one doesn't count, that's not even in the ocean."
				#Does'nt count if previously guessed
				elif guess[board[guess_row][guess_col]] == player(turn_count):
					print "Hey you guessed this one already! One more time!"
				elif guess[board[guess_row][guess_col]] == player(turn_count + 1):
					print player(turn_count + 1), "guessed this earlier. Not right! Again!"
				#Wrong Guess
				else:
					if player(turn_count) == p1_name:
						board[guess_row][guess_col] = "X"
					if player(turn_count) == p2_name:
						board[guess_row][guess_col] = "Y"
					print "Oops, you missed my battleship!",
					if turn_count < 7:
						print "Let", player(turn_count + 1), "try!"
				
					turn_count += 1
			input_flag = False

	#Max turn_count achieved
	if turn_count == 8:
			print "Game Over"
			print turn_count + 1
			print_board(board)