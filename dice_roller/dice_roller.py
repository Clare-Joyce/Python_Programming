
import random
from termcolor import colored
import pandas as pd
import time
import numpy as np

def roll_dice(dice_size=6):

  roll = random.randint(1,dice_size)
  if roll == 1:
    print(f'You rolled a {roll}! Critical Fail')
  elif roll == dice_size:
    print(f'You rolled a {roll}! Critical Success!')
  else:
    print(f'You rolled a {roll}')
  return roll

def ludo():
  """
  This program mimics the ludo game.

  Will start with a very simple algorithm and improve it with time
  
  """
  print(colored("\n\nLUDO Game!!!\n", "blue", attrs=['bold']))

  num_players = int(input("Enter number of players: "))
  while num_players <2 or num_players>4:
    num_players = int(input("Enter number of players: "))

  # dice_size = int(input('How many sides are the dice? '))
  winning_score = int(input('What is your winning score? '))

  players = ["p_" + str(i+1) for i in range(0, num_players)]
  num = 0
  score_table = pd.DataFrame(columns = players)
  score_table.loc['score'] = 0
  score_table.loc[num, :] = 0
  # print(score_table)
  # print(players)

  while not any(i>=winning_score for i in score_table.loc['score']):
    num += 1
    score_list = list()
    score_table.loc['score'] = 0
    for i in range(0, len(players)):
      score_list.append(roll_dice())
      time.sleep(2)

    score_table.loc[num] = score_list
    score_table.loc['score']= score_table.sum(axis=0)
    # print("no winner")
    # print(score_table.loc['score'])
    # print(score_list)
    print(score_table)
  
  # check winner
  winner_s = score_table.loc['score'].ge(winning_score)
  winner_s = np.where(score_table.loc['score'].ge(winning_score), score_table.columns, '')
  winner_s = np.delete(winner_s, np.where(winner_s=='')).tolist()
  print(winner_s)
  print(len(winner_s))
  if len(winner_s) >=2:
    print("Yaay!, more than one winner")
    print('\n'.join(winner_s))
    gt_score = score_table.loc['score'].max()
    print(gt_score)
    print(f"Overall winner: {score_table.loc['score'].eq(gt_score).keys()}")
  else:
    print(f"Player {winner_s} wins!!!")

if __name__== "__main__":
  ludo()