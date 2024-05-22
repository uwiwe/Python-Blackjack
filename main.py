import art
from replit import clear
import random

keep_playing = True
current_cash = 1000.00

def win(current_bet):
  global current_cash
  print(f"Your final hand: {user_cards}, final score: {sum(user_cards)}")
  print(f"Computer's final hand: {computer_cards}, final score: {sum(computer_cards)}")
  print(f"You win! We added {current_bet}$ to your cash.")
  current_cash += current_bet

def lose(current_bet):
  global current_cash
  print(f"Your final hand: {user_cards}, final score: {sum(user_cards)}")
  print(f"Computer's final hand: {computer_cards}, final score: {sum(computer_cards)}")
  print(f"You lose! You lost {current_bet}$ from your cash.")
  current_cash -= current_bet

def game_not_over(stop):
  # global user_cards
  # global computer_cards
  if stop:
    return False
  elif sum(user_cards) < 21 and sum(computer_cards) < 21:
    return True
  else:
    return False

def generate_card(another_card, list_cards):
  new_card = cards[random.randint(0, 12)]
  if new_card == 11 and sum(list_cards) > 10:
    new_card = 1
  list_cards.append(new_card)

while keep_playing:
  stop = False
  bet_continue = False
  want_play = input("Do you want to play a game of Blackjack? Type 'y' or 'n' ")
  if want_play == "n":
    print(f"You closed the program. You ended up with {current_cash}$!")
    keep_playing = False
  else:
    clear()
    print(art.logo)
    current_cash = round(current_cash, 2)
    print(f"You got {current_cash}$.")
    while bet_continue == False:
      current_bet = round(float(input("How much money you want to bet? ")), 2)
      if current_bet > current_cash:
        print(f"You can't bet more money than your current cash, which is {current_cash}")
      else:
        print(f"You are betting {current_bet}$.")
        bet_continue = True
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    user_cards = [cards[random.randint(0, 12)], cards[random.randint(0, 12)]]
    computer_cards = [cards[random.randint(0, 12)], cards[random.randint(0, 12)]]
    print(f"Your cards: {user_cards}, current score: {sum(user_cards)}")
    print(f"Computer first card: {computer_cards[0]}")
    double_bet = input("Do you want to double your bet? Type 'y' or 'n' ")
    if double_bet == 'y' and current_bet * 2 <= current_cash:
      current_bet *= 2
      print(f"You are now betting {current_bet}$.")
    elif double_bet == 'y':
      print("You can't double your bet, you don't have enough cash!")
    while game_not_over(stop):
      another_card = input("Type 'y' to get another card, type 'n' to pass ")
      if another_card == 'y':
        generate_card(another_card, user_cards)
        print(f"Your cards: {user_cards}, current score: {sum(user_cards)}")
        print(f"Computer's first card: {computer_cards[0]}")
      elif another_card == 'n':
        while sum(computer_cards) < 17:
          generate_card(another_card, computer_cards)
        stop = True
    if sum(user_cards) > sum(computer_cards):
      if sum(user_cards) > 21:
        lose(current_bet)
      else:
        win(current_bet)
    elif sum(computer_cards) > sum(user_cards):
      if sum(computer_cards) > 21:
        win(current_bet)
      else:
        lose(current_bet)
    else:
      print(f"Draw. Your {current_bet}$ were returned to your cash.")
    if current_cash <= 0:
      print(f"Your current cash is {current_cash}$! End of the game!")
      keep_playing = False
    bet_continue = False