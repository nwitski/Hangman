# Hangman Game

import random
import time
import collections


# Get users name
name = input("What is your name? ")

# introduction
print ('Welcome to Hangman! ' + name)
print ('\n')



#importing words from words.txt and getting a single word
words = [line.rstrip('\n') for line in open('words.txt')]
rand_word = random.choice(words)


correct_char = set(list(rand_word))

#create variable as an empty value
correct_guess = ''
guesses = ''
incorrect = ''

turns = 0

#hangman graphics

graphics_list = [' _____ \n | \n | \n | \n | \n | \n | \n_______ \n', 
				' _____ \n |   |\n | \n | \n | \n | \n | \n_______ \n', 
				' _____ \n |   |\n |   o\n | \n | \n | \n | \n_______ \n',
				' _____ \n |   |\n |   o\n |   |\n | \n | \n | \n_______ \n',
				' _____ \n |   |\n |   o\n |  /|\n | \n | \n | \n_______ \n',
				' _____ \n |   |\n |   o\n |  /|\ \n | \n | \n | \n_______ \n',
				' _____ \n |   |\n |   o\n |  /|\ \n |   |\n | \n | \n_______ \n',
				' _____ \n |   |\n |   o\n |  /|\ \n |   |\n |  /\n | \n_______ \n',
				' _____ \n |   |\n |   o\n |  /|\ \n |   |\n |  / \ \n | \n_______ \n',
				' _____ \n |   |\n |   o   AHHHH\n |  /|\ \n |   |\n |  / \ \n | \n_______ \n',
				' _____ \n |   |\n |   X   AHHHH\n |  /|\ \n |   |\n |  / \ \n | \n_______ \n']

# initializing the lines
correct_guess_ordered = ["_"] * len(rand_word)



while turns < 11:
	guess = input("guess a character: ").lower()
	guesses += guess

	#making sure its an alphabetical letter
	if not guess.isalpha():
		print ('This is not a letter')
		continue

	#guesses within the code
	elif guess in correct_guess or guess in incorrect:
		print("Already guessed this one.")
		continue

	elif guess in correct_char:
		correct_guess += guess

		#setting guesses in order

		for i in range(len(rand_word)):
			if guess == rand_word[i]:
				correct_guess_ordered[i] = guess

		# this joins the lines to be with one another
		print(" ".join(correct_guess_ordered))

	else:
		incorrect += guess

	
	if len(correct_char) == len(correct_guess):
		print ('You Win!')
		break

	if guess not in rand_word: 

		turns += 1
		print ("Wrong")
		print(graphics_list[turns])
		
	
		
	if turns == 10:           
		print ("You Lose, the correct word was:", rand_word)
		break












