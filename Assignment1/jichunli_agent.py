# CSE 415 Winter 2019
# Assignment 1
# Jichun Li 1531264

from re import *
import random

painScale = 0
input_memory = []
answer_memory = []
cycle = 0
fav_rest = []

def introduce():
	#Introduction of the agent
	return """Hello, I am Bayma, your personal diet companion.
		I was programmed by Jichun Li. If you don't like
		the way I deal, contact him at jichunli@uw.edu.
		"""

def agentName():
	#Return the name of the agent
	return 'Baymax'

def respond(the_input):
	wordlist = split(' ', remove_punctuation(the_input))
	wordlist[0] = wordlist[0].lower()
	mapped_wordlist = you_me_map(wordlist)
	mapped_wordlist[0] = mapped_wordlist[0].capitalize()
	
	global cycle	
	global fav_rest
	
	# rule 1: if nothing is said to the chatbot, it will introduce itself
	if wordlist[0] == '':
		answer = 'Hello, I am Baymax, your personal diet companion.'
 	
	# rule 2: When the chatbot is asked about the suggestions on food, it will ask for hunger level
	elif 'food' in wordlist and 'suggestion' in wordlist:
		answer = """The suggestions for food would be based on your hunger level.
			 On the scale of one to four, how would you rate your hunger level?""" 
	
	# rule 3: the response when the hunger level is between one to two
	elif wordlist[0].lower() in ['one', 'two']:
		answer = 'I believe some salad would suit your needs.'

	# rule 4: the response when the hunger level is between three to four
	elif wordlist[0].lower() in ['three', 'four']:
		answer = 'I believe some taco would suits your needs.'

	# rule 5: when the user express their hatred for the chatbot
	elif 'hate' in wordlist:
		answer = 'Although you do not like what I suggest, I still insist that you should follow my instructions.'

	# rule 6: When the chatbot is asked about the whether, it will randomly select between sunny and rainy
	elif 'weather' in wordlist:
		answer = random.choice(["It's a sunny day.", "It's a rainy day."])

	# rule 7: When the chat bot receives greetings from the user
	elif 'good' in wordlist and 'morning' in wordlist:
		answer = 'Good morning to you! What can I do for you today?'
	
	# rule 8: When the chatbot is asked for other ideas about what to eat
	elif 'other' in wordlist and 'ideas' in wordlist :
		answer = 'Probably we should order take-out from your favorite restaurant.'
	
	# rule 9: When the chatbot is asked to order take-out from user's favorite restaurant
	elif 'favorite' in wordlist and 'restaurant' in wordlist and 'order' in wordlist:	
		fav_rest.append(wordlist[0].lower())	
		answer = 'The estimated time of arrive for your order at would be 60 minutes.'
		
	# rule 10: when the user said to the chatbot that he/she is waiting
	elif 'wait' in wordlist or 'waiting' in wordlist:
		if cycle % 3 == 0 :
			answer = 'There is still 40 minutes before your order gets here.'		
		
		elif cycle % 3 == 1:
			answer = 'Just 20 more minutes! Your is out for delivery.'
		
		elif cycle % 3 == 2:
			answer = 'Hang in there. Your order will arrive in 5 minutes.'

		cycle = cycle + 1
	
	# rule 11: when the chatbot is told that the food is delivered
	elif 'delivered' in wordlist:	
		answer = 'Here, your dinner is ready.'
 
	# rule 12: When the chatbot is told that food is too spicy
	elif wordlist[-2:] == ['too','spicy']:
		answer = 'OK I will inform ' + fav_rest[-1].capitalize() + ' next time. Are you full now?'

	# rule 13: When the user says that he/she is still hungry
	elif wordlist[-2:] == ['still', 'hungry']:
		answer = 'Your BMI is too high. I do not suggest you make another order.'
	
	# rule 14: When the user is forcing the chatbot to order stuff
	elif 'force' in wordlist:
		answer = 'Your order request is declined.'
	
	# rule 15: When the user said that the bot is useless, it will shut down
	elif 'useless' in wordlist:
		answer = 'Service is no longer needed. Shutting down.'		
	
	# rule 16: When the user talking about indoor
	elif 'indoor' in wordlist :
		answer = 'Indoor activities. Emmmmm. What about cooking?'
	
	# rule 17: When the user talking about going outside
	elif 'outside' in wordlist: 
		answer = 'You would like to go outside. What about shopping?'
	
	# rule 18: Respond when the user say the exactly same thing to the bot
	elif the_input in input_memory:
		answer = 'I believe you just told me that.'

	
	# rule 19: When the bot dont know what to say
	else:
		answer = random.choice(['Excuse me while I let out some air.',
					'Bah-a-la-la-la.',
					'I fail to see how the stuff you mentioned makes me a better diet companion',
					'You have been a good boy. Have a lollipop!'])
	
	input_memory.append(the_input)
	answer_memory.append(answer) 
	return answer

def stringify(wordlist):
    'Create a string from wordlist, but with spaces between words.'
    return ' '.join(wordlist)

punctuation_pattern = compile(r"\,|\.|\?|\!|\;|\:")    

def remove_punctuation(text):
    'Returns a string without any punctuation.'
    return sub(punctuation_pattern,'', text)

CASE_MAP = {'i':'you', 'I':'you', 'me':'you','you':'me',
            'my':'your','your':'my',
            'yours':'mine','mine':'yours','am':'are'}

def you_me(w):
    'Changes a word from 1st to 2nd person or vice-versa.'
    try:
        result = CASE_MAP[w]
    except KeyError:
        result = w
    return result

def you_me_map(wordlist):
    'Applies YOU-ME to a whole sentence or phrase.'
    return [you_me(w) for w in wordlist]

