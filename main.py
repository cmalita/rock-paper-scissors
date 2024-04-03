import random
import console
import sys

options = ["rock", "paper", "scissors"]

def display_choice(choice):

	rock = '''
	
	     ______
	----'  ____)
	     (_____)
	     (_____)
	     (____)
	---._(___)
	
	'''
	
	paper = '''
	    _______
	---'    ___)_____
	            _____)
	            ______)
	           _____)
	--.___________)  
	'''
	
	scissors = '''
	    _______
	---'    ___)____
	          _______)
	          _______)
	          (___)
	--.______(___)  
	
	'''
	img = [rock, paper, scissors]
	print(img[choice])

def get_user_choice():
	print('What do you choose? Type "rock", "paper" or "scissors":')	
	user_input = input().lower()
	if user_input == "quit":
		print("Bye!")
		sys.exit()
	try:
		user_choice = options.index(user_input)
		return user_choice
	except:
		print("Please enter a valid option.")
		return get_user_choice()
		
def get_computer_choice():
	number = random.randint(0,2)
	return number
	
def get_winner(user_choice, computer_choice):
	if user_choice == computer_choice:
		return 'tie'
	
	elif user_choice == 0 and computer_choice == 2:
		return 'user'
	elif user_choice == 2 and computer_choice == 0:
		return 'computer'
	elif user_choice > computer_choice:
		return 'user'
	else:
		return 'computer'

console.clear()

print("Rock, Paper, Scissors Game. Type quit to exit.\n\n")

while (True):
	user_choice = get_user_choice()
	computer_choice = get_computer_choice()
	display_choice(user_choice)
	print("Computer choice:")
	display_choice(computer_choice)
	winner = get_winner(user_choice, computer_choice)
	
	if winner == 'user':
		print("You won!")
	elif winner == 'computer':
		print("You lost!")
	else:
		print("It's a tie!")
