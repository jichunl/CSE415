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

	if wordlist[0] == '':
		answer = 'Hello, I am Baymax, your personal healthcare companion.'
 	
	elif 'food' in wordlist and 'suggestion' in wordlist:
		answer = """The suggestions for food would be based on your hunger level.
			 On the scale of one to four, how would you rate your hunger level?""" 
	
	elif wordlist[0].lower() in ['one', 'two']:
		answer = 'I believe some salad would suit your needs.'

	elif wordlist[0].lower() in ['three', 'four']:
		answer = 'I believe some taco would suits your needs.'

	elif 'hate' in wordlist:
		answer = 'Although you do not like what I suggest, I still insist that you should follow my instructions.'

	elif 'pain' in wordlist or 'hurt' in wordlist or 'Ow' in wordlist:
		painScale = input('On a scale of 1 to 10, how would you rate your pain? (in digits)')
		if painScale == 0 :
			answer = 'It is alright to cry.'
		
		elif painScale < 5 :
			hurt_answer = raw_input('Does it hurt when I touch it?') 
			if (hurt_answer.lower() == 'yes'):
				answer = 'My apologies. I will scan you for injuries.'
			
			else:
				answer = 'I will scan you for injuries.'
		
		else:
			answer = 'I will scan you for injuries.'
		
	elif 'scan' in wordlist:
		answer = 'Scan complete!'
		if (painScale < 3):
			answer = """You have sustained no injuries. 
				However, your hormone and neurotransmitter levels indicate that 
				you are experiencing mood swings, common in adolescence."""

	elif ('heart' in wordlist and 'attack' in wordlist) or 'heart-attack' in wordlist:
		answer = 'My hands are equipped with defibrillators. Clear!'

	elif wordlist[0:3] == ['are','you','sick']:
		answer = 'I cannot be sick. I am a robot.'

	elif 'Karate' in wordlist:
		if (cycle % 3 == 0):
			answer = 'I fail to see how Karate makes me a better healthcare companion.'
		elif (cycle % 3 == 1):
			answer = 'I also know karate.'
		else :
			answer = 'My ninja skills are sweet!'

	elif 'weather' in wordlist:
		answer = random.choice(["It's a sunny day.", "It's a rainy day."])

	elif 'feel' in wordlist and 'bad' in wordlist:
		answer = 'Those who suffer a loss require support from friends and loved ones.'

	elif 'lazy' in wordlist:
		answer = 'I am a robot. I cannot be offended.'

	elif wordlist[0] == 'fight':
		answer = 'My programming prevents me from injuring a human being.'

	elif 'other' in wordlist and 'ideas' in wordlist :
		answer = 'Probably we should order take-out from your favorite restaurant.'
	
	elif 'favorite' in wordlist and 'restaurant' in wordlist and 'order' in wordlist:	
		fav_rest.append(wordlist[0].lower())	
		answer = 'The estimated time of arrive for your order at would be 60 minutes.'
		

	elif 'wait' in wordlist or 'waiting' in wordlist:
		if cycle % 3 == 0 :
			answer = 'There is still 40 minutes before your order gets here.'		
		
		elif cycle % 3 == 1:
			answer = 'Just 20 more minutes! Your is out for delivery.'
		
		elif cycle % 3 == 2:
			answer = 'Hang in there. Your order will arrive in 5 minutes.'

		cycle = cycle + 1

	elif 'delivered' in wordlist:	
		answer = 'Here, your dinner is ready.'
 
	elif wordlist[-2:] == ['too','spicy']:
		answer = 'OK I will inform ' + fav_rest[-1] + ' next time. Are you full now?'

	elif wordlist[-2:] == ['still', 'hungry']:
		answer = 'Your BMI is too high. I do not suggest you make another order.'
	
	elif 'force' in wordlist:
		answer = 'Your order request is declined.'

	elif 'useless' in wordlist:
		answer = 'Service is no longer needed. Shutting down.'		

	elif 'indoor' in wordlist :
		answer = 'Indoor activities. Emmmmm. What about cooking?'

	elif 'outside' in wordlist: 
		answer = 'You would like to go outside. What about shopping?'

	elif the_input in input_memory:
		answer = 'I believe you just told me that.'

	else:
		answer = random.choice(['Excuse me while I let out some air.',
					'I have some concerns.',
					'Bah-a-la-la-la.',
					'I fail to see how the stuff you mentioned makes me a better healthcare companion',
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

def wpred(w):
    'Returns True if w is one of the question words.'
    return (w in ['when','why','where','how'])

def dpred(w):
    'Returns True if w is an auxiliary verb.'
    return (w in ['do','can','should','would'])

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

