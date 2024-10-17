#Blayne Hoy
#U2 L3

import random
from time import sleep

class TicTacToe:
  def __init__(self):
    self.__board = [[x + (3*y)+1 for x in range(3)] for y in range(3)]
    self.__turn = random.choice(["X", "O"])

  def __check_win(self):
    for x in range(3):
      if self.__board[x][0] == self.__board[x][1] == self.__board[x][2]:
        return True
      elif self.__board[0][x] == self.__board[1][x] == self.__board[2][x]:
        return True
    if self.__board[0][0] == self.__board[1][1] == self.__board[2][2]:
        return True
    elif self.__board[0][2] == self.__board[1][1] == self.__board[2][0]:
        return True
    return False
  
  def place_token(self, row, col):
    if isinstance(self.__board[row][col], int):
      self.__board[row][col] = self.__turn
      self.__turn = "O" if self.__turn == "X" else "X"
      return "Next turn"
    else:
      return "Cell already occupied"

  
  def is_winner(self):
    return self.__check_win()


  def __str__(self):
    board = "---------\n"
    for row in self.__board:
      board += f"{row[0]} | {row[1]} | {row[2]}\n"
      board += f"---------\n"
    return board