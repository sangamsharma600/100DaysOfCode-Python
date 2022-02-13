
#/*HIGHER OR LOWER GAME*\#
# Reference : "http://www.higherlowergame.com/" 
import art
from game_data import data
from random import randint
import os
def clear(): os.system('cls')

score = 0
print(art.logo)
is_game_over=False

data1 = data[randint(0, len(data)-1)]
temp_data=data[randint(0, len(data)-1)]
while not is_game_over:
  data2=data[randint(0, len(data)-1)]
  if temp_data==data2:
    continue
  print(
      f"Compare A: {temp_data['name']}, {temp_data['description']}, {temp_data['country']}")

  print(art.vs)

  print(
      f"Compare B: {data2['name']}, {data2['description']}, {data2['country']}")

  answer= input("\nWho has more followers? A or B : ").lower()
  clear()
  print(art.logo)

  followers1=temp_data['follower_count']
  followers2=data2['follower_count']
  if(answer=='a' and followers1>followers2):
      score+=1
  elif answer=='b' and followers2>followers1:
    score+=1
  else:
    print(f"Game Over. Your high score is {score}")
    is_game_over=True
  temp_data=data2


# END OF CODE #