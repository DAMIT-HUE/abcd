import sys, time
import random

# declaring some variables
username = "1"
password = "1"
value_of_pass = "0"
value_of_name = "0"
bitcoin_price = 26849
new_bitcoin_price = 0
percentage_change = 0
percentage_change_display = 0
left_over = 0
tries = 0

#Saves amount of money and bitcoin of the user
# converts the value amount to bitcoin
# error not saving bitcoin value to current_bitcoin


# function to make output display in style
def sprint(str):
  for c in str + '\n':
    sys.stdout.write(c)
    sys.stdout.flush()
    time.sleep(3. / 90)


def sprint2(str):
  for c in str:
    sys.stdout.write(c)
    sys.stdout.flush()
    time.sleep(3. / 90)


def bit_conv(amount):
  global current_bitcoin
  global left_over

  left_over = current_bitcoin
  current_bitcoin = amount / bitcoin_price + left_over
  current_bitcoin = round(current_bitcoin, 2)
  sprint(f"you currently have {current_bitcoin}")
  time.sleep(0.5)


def money_conv(sell_amount):
  global current_money
  global current_bitcoin

  current_money = sell_amount * bitcoin_price + current_money
  current_money = round(current_money, 0)
  current_bitcoin = current_bitcoin - sell_amount

  sprint(f"you currently have $ {current_money}")
  time.sleep(0.5)


# creates new account if values in password.txt and username.txt are empty
def newAccount():
  global username
  global password
  global current_money
  global current_bitcoin

  current_bitcoin = 0
  current_money = 10000
  sprint("Welcome to get rich with bitcoin trading app!")
  time.sleep(0.5)
  sprint("Create your new bitcoin account")
  sprint2("Input your new username: ")
  username = input()
  with open("username.txt", 'w') as file:
    file.write(str(username))
  time.sleep(0.5)
  sprint2("Input your new password: ")
  password = input()
  time.sleep(0.5)
  with open("password.txt", 'w') as file:
    file.write(str(password))
  with open('money.txt', 'w') as file:
    file.write(str(current_money))
  with open('bitcoin.txt', 'w') as file:
    file.write(str(current_bitcoin))


try:
  with open('money.txt', 'r') as file:
    current_money = float(file.read())
  with open('bitcoin.txt', 'r') as file:
    current_bitcoin = float(file.read())
except FileNotFoundError:
  newAccount()


# checks if user has enough money to buy bitcoin and call bit_conv with amount_to_buy
def buy():
  gen_new_price()
  global current_money
  sprint2(
    f"you have {current_money} in your account, bitcoin is worth {round(bitcoin_price, 2)}  are you sure you want to buy?: (y/n) "
  )
  buychoice = input()
  if buychoice.lower() != "y":
    return
  else:
    sprint2("Enter the amount you want to buy: ")
    amount_to_buy = int(input())
    if amount_to_buy > current_money:
      sprint("You dont have enough money in your account")
      return
    current_money = current_money - amount_to_buy
    current_money = round(current_money, 0)
    sprint(f"You have {current_money} dollars left")
    bit_conv(amount_to_buy)


def gen_new_price():
  global new_bitcoin_price
  global bitcoin_price
  global current_bitcoin
  global percentage_change
  global percentage_change_display

  percentage_change = random.randint(-30, 60) / 100
  while percentage_change == 0:
    percentage_change = percentage_change = random.randint(-30, 60) / 100
  new_bitcoin_price = percentage_change * bitcoin_price
  new_bitcoin_price = round(new_bitcoin_price, 2)
  bitcoin_price = bitcoin_price + new_bitcoin_price
  percentage_change_display = percentage_change * 100
  # print(new_bitcoin_price)
  # print(bitcoin_price)


def sell():  # still not added
  gen_new_price()
  if percentage_change <= 0:
    sprint2(
      f"bitcoin is {percentage_change_display}% down, its price is {bitcoin_price}, do you want to sell? (y/n) "
    )
  if percentage_change >= 0:
    sprint2(
      f"bitcoin is {percentage_change_display}% up, its price is {bitcoin_price}, do you want to sell? (y/n) "
    )
  sell_choice = input()
  if sell_choice.lower() == "y":
    sprint2(
      f"You currently have {current_bitcoin} how much do you want to sell? ")
    sell_amount = float(input())
    if sell_amount > current_bitcoin:
      sprint("You dont have enough bitcoin")
      return
    if sell_amount <= current_bitcoin:
      money_conv(sell_amount)
    else:
      sprint("non viable input, please write numbers")
  if sell_choice.lower() != "y":
    return


def view_acc():  #error current bitcoin variable isnt getting updated
  sprint(f"You have ${current_money} and {current_bitcoin} bitcoin")


try:
  with open('password.txt',
            'r') as file:  # these 2 commands handle user logins
    value_of_pass = file.read()

  with open('username.txt', 'r') as file:
    value_of_name = file.read()

except FileNotFoundError:
  newAccount()

# if value_of_pass == "0" and value_of_name == "0":# checks if this is first time for user to open account and if so calls newAccount()
# 	newAccount()

for i in range(3):
  sprint2("Enter your username: ")
  entered_username = input()
  time.sleep(0.5)
  sprint2("Enter your password: ")
  entered_password = input()
  tries = tries + 1
  if entered_password == value_of_pass and entered_username == value_of_name:  # checks for correct user and password
    sprint(f"Welcome back {value_of_name}")
    break
  else:
    if tries == 3:
      sprint("Too many incorrect password or username")
      time.sleep(1)
      quit()
    else:
      sprint("Wrong password try again")

while True:  # handles input
  sprint("What do you want to do buy, sell, view account")
  sprint2("Enter action: ")
  action = input()
  if action.lower() == "buy":
    buy()
  if action.lower() == "sell":
    sell()
  if action.lower() == "view account":
    view_acc()
  # if action.lower() == "quit" or "quit app":
  #   quit()
  with open('money.txt', 'w') as file:
    file.write(str(current_money))
  with open('bitcoin.txt', 'w') as file:
    file.write(str(current_bitcoin))
