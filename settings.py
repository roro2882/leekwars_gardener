from utils import g, behavior, shutdown, goal

#################################################################
# Declaring accounts
#################################################################
class Accounts:
	shutdown = shutdown.OFF
	list= [
		{
			'login': 'myAccount',
			'password': 'myPassword',
			'behavior': behavior.EQUALIZE,
			'limit': 50, # if behavior != TODOLIST, how many fights we always keep in stock
			'todolist': { # only needed if behavior = TODOLIST
				g.FARMER: 0,
				g.LEEK_1: 0,
				g.LEEK_2: 0,
				g.LEEK_3: 0,
				g.LEEK_4: 0,
			},
			'tournaments': [
				g.FARMER,
				g.LEEK_1,
				g.LEEK_2,
				g.LEEK_3,
				g.LEEK_4,
			],
			'goals': {
				g.LEEK_1: goal.NONE,
				g.LEEK_2: goal.FOCUS_LIFE,
				g.LEEK_3: goal.FOCUS_STRENGTH,
				g.LEEK_4: goal.FOCUS_WISDOM,
			},
		},
		{
			'login': 'myAccount2',
			'password': 'myPassword2',
			'behavior': behavior.NONE,
		},
	]
