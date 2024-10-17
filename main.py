#Blayne Hoy
#U2 L3

from tic_tac_toe import *

def rules():
    print(f"Hello player, the game you will be playing today is called Tic Tac Toe. I will be explaining the rules of said game now.\n")
    sleep(3.5)
    print(f"You will be playing against a computer, your goal is to get 3 x/o in either a diagonal, horizontal, or vertical row.\n")
    sleep(4.5)
    print(f"When all 9 squares are full, the game ends. If no player has no 3 marks in a row then the game ends.\n")
    sleep(3.5)
    print(f"Will you beat the computer? Try it now.\n")
    sleep(1.5)

def player_move(game):
  while True:
    try:
      move = int(input("Enter your desired posistion (1-9): ")) - 1
      row, col = divmod(move, 3)
      result = game.place_token(row, col)
      if result == "Next turn":
        break
      else:
        print(result)
    except (ValueError, IndexError):
      print("Invalid input. Please enter a number between 1 and 9.")

def ai_move(game):
  available_moves = [(x, y) for x in range(3) for y in range(3) if isinstance(game._TicTacToe__board[x][y], int)]
  if available_moves:
    move = random.choice(available_moves)
    game.place_token(move[0], move[1])
    print(f"Computer chose spot {move[0] * 3 + move[1] + 1}")

def main():
  rules()
  game = TicTacToe()
  print(game)
  while True:
    print("Player turn:")
    player_move(game)

    if game.is_winner():
      print("Player wins!")
      break

    if all(not isinstance(cell, int) for row in game._TicTacToe__board for cell in row):
      print("You tied!")
      break
    
    print("Computers turn:")
    sleep(1)
    ai_move(game)
    print(game)

    if game.is_winner():
      print("Computer wins!")
      break
    
    if all(not isinstance(cell, int) for row in game._TicTacToe__board for cell in row):
      print("You tied!")
      break
    
  print(game)

if __name__ == "__main__":
  main()