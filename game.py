from random import randint
from time import sleep

EASY = 'EASY'
MEDIUM = 'MEDIUM'
HARD = 'HARD'

PLAYER_NAME = None
PLAYER_LEVEL = None
PLAYER_SCORE = 0

POSITIVE_SCORE = 0
NEGATIVE_SCORE = 0

POSITIVE_SCORE_MAP = {
	EASY: 5,
	MEDIUM: 10,
	HARD: 20
}

NEGATIVE_SCORE_MAP = {
	EASY: 2,
	MEDIUM: 5,
	HARD: 10
}

START_TEXT = '''\n\n********************************** GAMBLE **********************************
Just guess what will be the sum of the numbers on all the dices and win.
Its harder to win and very easy to loose!!

Try as many times you want and try to improve your score\n\n'''


def get_name():
	
	global PLAYER_NAME

	print('Enter Player Name - ', end="")
	
	PLAYER_NAME = input()
	PLAYER_NAME = PLAYER_NAME.capitalize()


def initiate_play(again=False):
	
	play_text = 'Hey %s, do you want to play %s?? \n1. Yes \n2. No \n\nEnter choice number - '
	
	again_text = '\b'
	if again:
	    again_text = 'again'
	
	play_text = play_text % (PLAYER_NAME, again_text)

	print_line()
	print(play_text, end='')

	choice = input()
	
	try:
		choice = int(choice)
	except:
		print('Incorrect choice!!!')
		return initiate_play()

	if choice == 1:
		level_selection()
	elif choice == 2:
		initiate_exit()
	else:
		print('Incorrect choice!!!')
		return initiate_play()


def level_selection():
	
	global PLAYER_LEVEL, POSITIVE_SCORE, NEGATIVE_SCORE

	level_selection_text = '%s, Choose your level - \n1. Easy [1 - DICE] - +5/-2 \n2. Medium [2 - DICES] - +10/-5 \n3. Hard [3 - DICES] - +20/-10 \n\nEnter choice number - '

	print_line() 
	print(level_selection_text % PLAYER_NAME, end='')

	try:
		choice = int(input())
	except:
		print('Incorrect choice!!!')
		return level_selection()
	
	print_line()
	
	level_map = {
		1: EASY,
		2: MEDIUM,
		3: HARD
	}

	if level_map.get(choice):
		PLAYER_LEVEL = level_map[choice]
	else:
		print('Incorrect choice!!!')
		return level_selection()

	POSITIVE_SCORE = POSITIVE_SCORE_MAP[PLAYER_LEVEL]
	NEGATIVE_SCORE = NEGATIVE_SCORE_MAP[PLAYER_LEVEL]

	start_game()


def start_game():

	global PLAYER_SCORE

	die_sum = 0

	number_of_die_throws = {
		EASY: 1,
		MEDIUM: 2,
		HARD: 3
	}

	print('Guess the sum - ')
	try:
		player_guess = int(input())
		print_line()
	except:
		print('Some error has occurred!!')
		return start_game()

	print('Lets roll ...')

	for count in range(number_of_die_throws[PLAYER_LEVEL]):
		for seconds in range(randint(3,5)):
			sleep(seconds)
		die_number = randint(1,6)
		print('The number on die %s is %s' % (count + 1, die_number))

		die_sum += die_number

	sleep(5)
	if die_sum == player_guess:
		PLAYER_SCORE += POSITIVE_SCORE
	else:
		PLAYER_SCORE -= NEGATIVE_SCORE

	print_line()
	print('Your current score is %d' % PLAYER_SCORE)

	initiate_play(again=True)


def initiate_exit():
	print_line()
	sleep(2)
	print('%s\'s final score is %d.' % (PLAYER_NAME, PLAYER_SCORE))
	print_line()
	sleep(3)
	print('Goodbye!!!!')
	print_line()


def print_line():
	print('-' * 50)
	

print(START_TEXT)
get_name()
initiate_play()
