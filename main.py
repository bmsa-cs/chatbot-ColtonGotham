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

  happy_emotions = ["happy","good", "great", "well", "amazing", "beautiful","wonderful","happy!","good!", "great!", "well!", "amazing!", "beautiful!", "wonderful!"]

  sad_emotions = ["bad", "sad", "not great", "not good", "no good", "depressed", "unhappy", "lonely", "gloomy"]


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
    print ("Sorry I don't understand...")
  
  #2011-2025
  generation_alpha = ["2011","2012","2013","2014","2015","2016","2017","2018","2019","2020","2021","2022","2023","2024","2025"]

  #1998-2010
  generation_z = ["1998","1999","2000","2001","2002","2003","2004","2005","2006","2007","2008","2009","2010"]

  #1981-1997
  millennial = ["1981","1982","1983","1984","1985","1986","1987","1988","1989","1990","1991","1992","1993","1994","1995","1996","1997"]

  #1965-1980
  generation_x = ["1965","1966","1967","1968","1969","1970","1971","1972","1973","1974","1975","1976","1977","1978","1979","1980"]

  #1946-1964
  baby_boomer = ["1946","1947","1948","1949","1950","1951","1952","1953","1954","1955","1956","1957","1958","1959","1960","1961","1962","1963","1964"]

  #1928-1945
  generation_silent = ["1928","1929","1930","1931","1932","1933","1934","1935","1936","1937","1938","1939","1940","1941","1942","1943","1944","1945"]

  #1901-1927
  generation_greatest = ["1901","1902","1903","1904","1905","1906","1907","1908","1909","1910","1911","1912","1913","1914","1915","1916","1917","1918","1919","1920","1921","1922","1923","1924","1925","1926","1927"]
  
  age = input("\nWhat year were you born?\n")

  if age in generation_alpha:
    print (f"Okay so if you were born in {age} that means you are generation Alpha")

  elif age in generation_z:
    print (f"Okay so if you were born in {age} that means you are Generation Z")

  elif age in millennial:
    print (f"Okay so if you were born in {age} that means you are a Millennial")

  elif age in generation_x:
    print (f"Okay so if you were born in {age} that means you are Generation X")
  
  elif age in baby_boomer:
    print (f"Okay so if you were born in {age} that means you are a Baby Boomer")
  
  elif age in generation_silent:
    print (f"Okay so if you were born in {age} that means you are the Silent Generation") 
  
  elif age in generation_greatest:
    print (f"Okay so if you were born in {age} that means you are the Greatest Generation")

  else:
    print (f"Okay so if you were born in {age} you are either a zombie or a time traveler?!")
  





  color = input("\nWhat is your favorite color?\n").lower

  if color == ("red"):
    print (f"Okay so if your color is {color} then you probably like apples or cherries")
  elif color == ("blue"):
    print (f"Okay so if your color is {color} then you probably like birds or the ocean ")
  elif color == ("green"):
    print (f"Okay so if your color is {color} then you probably like plants or turtles")
  elif color == ("yellow"):
    print (f"Okay so if your color is {color} then you probably like pichachu or bananas")
  elif color == ("pink"):
    print (f"Okay so if your color is {color} then you probably like flamingos or cherry blossoms")
  elif color == ("purple"):
    print (f"Okay so if your color is {color} then you probably like grapes or butterflys")
  elif color == ("orange"):
    print (f"Okay so if your color is {color} then you probably like sunsets or basketball")
  elif color == ("brown"):
    print (f"Okay so if your color is {color} then you probably like bears or chocolate")
  elif color == ("white"):
    print (f"Okay so if your color is {color} then you probably like snow or seashells")
  elif color == ("black"):
    print (f"Okay so if your color is {color} then you probably like penguins or cats")
  else:
    print (f"If your color is {color} then I am not familer with that color\n")

  activity = input("What would like to do?\n\nDo you want to play a game?\n").lower()

  activity_game = ["yes", "y"]

  if activity in activity_game:
    if __name__ == '__main__':
      start()
    
  else:
    print("Well then...")

  print (f"Thank you for talking to me {name}")

  good_reaction = ["good","okay","pretty good","great", "amazing","awesome", "wonderful"]

  bad_reaction = ["bad", "not great", "horrible", "eh", "boring","meh"]

  conclusion = input("So how do you think this conversation went?").lower

  if conclusion in good_reaction:
    print (f"I am very glad that you agree with me that it was {conclusion} well bye then")
  elif conclusion in bad_reaction:
    print ("Oh... I am sorry well bye then")
  else: 
    print ("I see well bye then")



if __name__ == "__main__":
  main()
  t = input("Run pytest? (y/n)").lower()
  if t == 'y':
    run_tests()
