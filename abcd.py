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
    current_bitcoin = round(current_bitcoin , 2)
    print(current_bitcoin)

#converts bitcoin to money, feature still not added just ignore
def money_conv():
    # current_money = 
	print("1")


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
	global username
	global password
	sprint("Welcome to get rich with bitcoin trading app!")
	sprint("Create your new bitcoin account")
	sprint2("Input your new name: ")
	username = input()
	with open("username.txt",'w') as file:
		file.write(str(username))
	sprint2("Input your new password: ")
	password = input()
	with open("password.txt",'w') as file:
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


def gen_new_price():
	global new_bitcoin_price
	global bitcoin_price
	global current_bitcoin
	global percentage_change

	percentage_change = random.randint(-30,60) / 100
	while percentage_change == 0:
		percentage_change = percentage_change = random.randint(-30,60) / 100
	new_bitcoin_price = percentage_change * bitcoin_price
	new_bitcoin_price = round(new_bitcoin_price, 2)
	bitcoin_price = bitcoin_price + new_bitcoin_price
	print(new_bitcoin_price)
	print(bitcoin_price)

def sell():# still not added
	gen_new_price()
	if percentage_change <= 0:
		sprint2(f"bitcoin is {percentage_change}% down, its price is {bitcoin_price}, do you want to sell? (y/n) ")
	if percentage_change >= 0:
		sprint2(f"bitcoin is {percentage_change}% up, its price is {bitcoin_price}, do you want to sell? (y/n) ")
	sell_choice = input()
	if sell_choice.lower() == "y":
		sprint2(f"You currently have {current_bitcoin} how much do you want to sell? ")
		sell_amount = int(input())
		if sell_amount > current_bitcoin:
			sprint("You dont have enough bitcoin")
			return
		if sell_amount <= current_bitcoin:
			money_conv(sell_amount)
		else:
			sprint("non viable input, lease write numbers")
	if sell_choice.lower() == "n":
		return
	else:
		sprint2("Non viable input")
	
def view_acc():#error current bitcoin variable isnt getting updated
	sprint(f"You have ${current_money} and {current_bitcoin} bitcoin")
	time.sleep(3)

try:
	with open('password.txt', 'r') as file: # these 2 commands handle user logins
		value_of_pass = file.read()

	with open('username.txt', 'r') as file:
		value_of_name = file.read()

except FileNotFoundError:
	newAccount()

# if value_of_pass == "0" and value_of_name == "0":# checks if this is first time for user to open account and if so calls newAccount()
# 	newAccount()




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
