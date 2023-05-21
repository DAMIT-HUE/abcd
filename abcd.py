import os
import sys,time
import random

# declaring some variables
username = "1"
password = "1"
value_of_pass = "0"
value_of_name = "0"
current_bitcoin = 0
current_money = 10000
bitcoin_price = 26849
new_bitcoin_price = 0
percentage_change = 0

# converts the value amount to bitcoin
# error not saving bitcoin value to current_bitcoin
def bit_conv(amount):
    global current_bitcoin
    current_bitcoin = amount / bitcoin_price
    print(current_bitcoin)

#converts bitcoin to money, feature still not added just ignore
def money_conv():
    current_money = current_bitcoin * bitcoin_price


# function to make output display in style
def sprint(str):
   for c in str + '\n':
     sys.stdout.write(c)
     sys.stdout.flush()
     time.sleep(3./90)

def sprint2(str):
   for c in str:
     sys.stdout.write(c)
     sys.stdout.flush()
     time.sleep(3./90)

# creates new account if values in password.txt and username.txt are empty
def newAccount():
	sprint("Welcome to get rich with bitcoin trading app!")
	sprint("Create your new bitcoin account")
	sprint2("Input your new name: ")
	username = input()
	with open('username.txt','w') as file:
		file.write(str(username))
	sprint2("Input your new password: ")
	password = input()
	with open('password.txt','w') as file:
		file.write(str(password))

# checks if user has enough money to buy bitcoin and call bit_conv with amount_to_buy
def buy():
    global current_money
    sprint2(f" you have {current_money} in your account, bitcoin is worth {bitcoin_price}  how much do you want to buy?(write value in dollar): ")
    amount_to_buy = int(input())
    if amount_to_buy > current_money:
        sprint("You dont have enough money in your account")
        return
    current_money = current_money - amount_to_buy
    sprint(f"You have {current_money} left")
    bit_conv(amount_to_buy)


def sell():# still not added
	global new_bitcoin_price
	global bitcoin_price
	global current_bitcoin
	global percentage_change

	percentage_change = random.randint(-30,60) / 100
	new_bitcoin_price = percentage_change * bitcoin_price
	new_bitcoin_price = round(new_bitcoin_price, 2)
	bitcoin_price = bitcoin_price + new_bitcoin_price
	print(new_bitcoin_price)
	print(bitcoin_price)
	
def view_acc():#error current bitcoin variable isnt getting updated
	sprint(f"You have ${current_money} and {current_bitcoin} bitcoin")
	time.sleep(3)


if value_of_pass == "" and value_of_name == "":# checks if this is first time for user to open account and if so calls newAccount()
	newAccount()
	
with open('password.txt', 'r') as file: # these 2 commands handle user logins
    value_of_pass = file.read()

with open('username.txt', 'r') as file:
    value_of_name = file.read()

sprint2("Welcome back, enter your username: ")
entered_username = input()

sprint2("Welcome back, enter your password: ")
entered_password = input()

if entered_password == value_of_pass and entered_username == value_of_name:# checks for correct user and password
	sprint(f"Welcome back {value_of_name}")
else:
	sprint("Wrong pass or name")
	quit()

while True:# handles input
	sprint("What do you want to do buy, sell, view account or quit app")
	sprint2("Enter action: ")
	action = input()
	if  action.lower() == "buy":
		buy()
	if  action.lower() == "sell":
		sell()
	if  action.lower() == "view account":
		view_acc()
	# if action.lower() == "quit app" or "q":
	# 	quit()
