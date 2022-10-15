from replit import clear
from art import logo

print(logo)

situation = True
highest_bid = 0
bid_dictionary = {}
name_of_winner = ""

while situation:
  name = input("What is your name? ")
  bid = int(input("What is your bid? $ ")) 
  question = input("Is there a any user who want to bid ? ")
  
  def add_bid_and_name(name,bid):
    bid_dictionary[name] = bid   
  add_bid_and_name(name,bid)
  
  if (question ==  "yes"):
      clear()
  else:
      situation = False
 
for key in bid_dictionary:
 if (bid_dictionary[key] > highest_bid):
  highest_bid = bid_dictionary[key] 
  name_of_winner = key

print(f"The winner is {name_of_winner} and highest bid is {highest_bid}..")