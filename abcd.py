import os
import sys,time
import random

# declaring some variables
username = "1"
password = "1"
value_of_pass = "0"
value_of_name = "0"
current_bitcoin = 0
bitcoin = 0
current_money = 10000
print(current_money)

# converts the value amount to bitcoin
# error not saving bitcoin value to current_bitcoin
def bit_conv(amount):
    current_bitcoin = amount / 26849
    print(current_bitcoin)

#converts bitcoin to money, feature still not added just ignore
def money_conv():
    current_money = current_bitcoin * 26849


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
    sprint2(f" you have {current_money} in your account how much do you want to buy?(write value in dollar): ")
    amount_to_buy = int(input())
    if amount_to_buy > current_money:
        sprint("You dont have enough money in your account")
        return
    current_money = current_money - amount_to_buy
    sprint(f"You have {current_money} left")
    bit_conv(amount_to_buy)


def sell():# still not added
	print("2")
	time.sleep(3)

def view_bit():#error current bitcoin variable isnt getting updated
	sprint(f"You have ${current_money} and {current_bitcoin} bitcoin")
	print("3")
	time.sleep(3)


with open('password.txt', 'r') as file: # these 2 commands handle user logins
    value_of_pass = file.read()

with open('username.txt', 'r') as file:
    value_of_name = file.read()

if value_of_pass == "" and value_of_name == "":# checks if this is first time for user to open account and if so calls newAccount()
	newAccount()

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
	sprint("What do you want to do buy, sell, view deposited bitcoin")
	sprint2("Enter action: ")
	action = input()
	if  action.lower() == "buy":
		buy()
	if  action.lower() == "sell":
		sell()
	if  action.lower() == "view deposited bitcoin":
		view_bit()s
