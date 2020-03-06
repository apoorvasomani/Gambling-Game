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


def get_name():
	special_print('Enter Player Name - ')
	PLAYER_NAME = input()
	PLAYER_NAME.capitalize()
	
	initiate_play()


def initiate_play(again=False):
	play_text = '''
	Hey %s, do you want to play %s??

	1. Yes
	2. No

	Enter choice number ...
	'''
	
	again_text = '\b'
	if again:
	    again_text = 'again'
	
	play_text = play_text % (PLAYER_NAME, again_text)

	special_print(play_text)
	
	choice = int(input())

	if choice == 1:
		level_selection()
	elif choice == 2:
		initiate_exit()
	else:
		special_print('Incorrect Option')
		return initiate_play()


def level_selection():
	level_selection_text = '''
	%s, Choose your level -

	1. Easy [1 - DIE]
	2. Medium [2 - DIE]
	3. Hard [3 - DIE]

	Enter choice number ...
	'''

	special_print(level_selection_text % PLAYER_NAME)

	choice = int(input())

	level_map = {
		1: EASY,
		2: MEDIUM,
		3: HARD
	}

	if level_map.get(choice):
		PLAYER_LEVEL = level_map[choice]
	else:
		special_print('Incorrect choice!!!')
		return level_selection()

	POSITIVE_SCORE = POSITIVE_SCORE_MAP[PLAYER_LEVEL]
	NEGATIVE_SCORE = NEGATIVE_SCORE_MAP[PLAYER_LEVEL]

	start_game()


def start_game():

	die_sum = 0

	number_of_die_throws = {
		EASY: 1,
		MEDIUM: 2,
		HARD: 3
	}

	special_print('Guess the sum of trials - ')
	try:
		player_guess = int(input())
	except:
		special_print('Some error has occurred!!')
		return start_game()

	special_print('Lets roll ...')

	for count in xrange(number_of_die_throws[PLAYER_LEVEL]):
		
		for seconds in xrange(randint(3,8)):
			special_print('......')
			time.sleep(seconds)
			die_number = random.randint(1,6)
			print('The number on die %s is %s' % (count, die_number))

			die_sum += die_number

	if die_sum == player_guess:
		PLAYER_SCORE += POSITIVE_SCORE
	else:
		PLAYER_SCORE -= NEGATIVE_SCORE

	initiate_play(again=True)


def initiate_exit():
	special_print('%s\'s final score is %s.' % (PLAYER_NAME, PLAYER_SCORE))
	special_print('Goodbye!!!!')


def special_print(text):

	for letter in text:
		print(letter, end='')
		sleep(0.10)
	
get_name()
