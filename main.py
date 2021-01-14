"""
Chatbot
Author: Colton Gotham
Period/Core: 7

"""
import os
import importlib.util
import random
import time

def run_tests():
  """
  This function will check for the pytest module
  before calling it to run the included tests.py
  """
  if importlib.util.find_spec('pytest') is None: # Check if pytest is installed
    os.system('python3 -m pip install -q pytest')

  command = "python3 -m pytest --tb=line -v -s tests.py"
  print(command)
  os.system(command)


def main():
  """This function contains all code for the chatbot."""

  #Game (RPSD) (This is part of the activity question so right now it is not active)
  rock = 1
  paper = 2
  scissors = 3 
  dynamite = 4

  names =  {rock: "Rock", paper: "Paper", scissors: "Scissors", dynamite: "Dynamite"}

  rules = {rock: scissors, paper: rock, scissors: paper, dynamite: rock, scissors: dynamite, dynamite: paper }

  player_score = 0
  computer_score = 0

  def start(): 
    print ("Rock, Paper, Scissors, Dynamite?")
    while game() :
      pass
    scores()
  def game():
    player = move()
    computer = random.randint (1,4)
    result (computer, player)
    return play_again()
  def move():
    while True:
      print
      player = input ("Rock = 1\nPaper = 2\nScissors = 3\nDynamite = 4\nMake a move: ") 
      try: 
          player = int(player)
          if player in (1,2,3,4): 
            return player
      except ValueError: 
          pass
      print ("Oops! I didn't understand that. Please enter 1, 2, 3, 4.")
  def result(computer, player) : 
      print ("1...")
      time.sleep(1)
      print ("2...")
      time.sleep(1)
      print ("3...")
      time.sleep(1)
      print ("Computer choose {0}!".format(names[computer]))
      global computer_score, player_score
      if player == computer: 
        print ("Tie\n") 
      else: 
        if rules[player] == computer:
          print ("You won\n")
          player_score += 1
        else:
          print ("You lose\n")
          computer_score += 1 
  def play_again():
    answer = input ("Would you like to play again? yes/no: ").lower
    if answer in ("y", "yes"):
      return answer
    else:
      print ("Game Over")
  def scores(): 
    global computer_score, player_score
    print ("HIGH SCORES")
    print ("Computer: ", computer_score)
    print ("Player: ", player_score)


  #Chatbot 
  name = input("Konichiwa! What is your name?\n")

  print (f"Nice to meet you {name}\nI have a name too! Mine is 01000001010010010010000001001000011101010110110101100001011011100010000001010011011010010110110101110101011011000110000101110100011010010110111101101110")
  
  feeling = str(input("\n\nHow are you today?\n")).lower()

  happy_emotions = ["happy","good", "great", "well", "amazing", "beautiful","happy!","good!", "great!", "well!", "amazing!", "beautiful!"]

  sad_emotions = ["bad", "sad", "not great", "not good", "no good", "depressed"]

  mad_emotions = ["mad", "angry", "upset", "annoyed"]

  neutral_emotions = ["okay", "eh", "neutral", "pretty okay"]

  negative_emotions = ["tired", "bored", "hungry"]
  
  if feeling in happy_emotions:
    print (f"YAY! I am happy that you are feeling {feeling}")
  
  elif feeling in sad_emotions:
    print (f"Oh! I am sorry that you are feeling {feeling}")

  elif feeling in mad_emotions:
    print (f"Oh! I hope that you aren't feeling too {feeling}")

  elif feeling in neutral_emotions:
    print ("Yeah I feel the same")

  elif feeling in negative_emotions:
    print (f"I hope you will be able to fill your {feeling}ness")

  else:
    print ("Okay")
  
  




  
  #Demo of a activity questions:
#_________________________________________________________________________
  #activity = input("What would like to do?\n\nDo you want to play a game, see a art piece, or neither?\n").lower()

  #activity_game = ["game", "play a game", "a", "1"]

  #activity_art = ["art", "art piece", "b", "2"]

  #if activity in activity_RPSD:
  #  start()
 # elif activity in activity_:
    
  #else:
   # print("Well then what do you want to do?")
#________________________________________________________________________




  

    

  
  





if __name__ == "__main__":
  main()
  t = input("Run pytest? (y/n)").lower()
  if t == 'y':
    run_tests()
