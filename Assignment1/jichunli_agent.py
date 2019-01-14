# CSE 415 Winter 2019
# Assignment 1
# Jichun Li 1531264

from re import *
import random

painScale = 0
input_memory = []
answer_memory = []
cycle = 0

def introduce():
	#Introduction of the agent
	return """Hello, I am Baymax, your personal healthcare companion.
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

	if wordlist[0] == '':
		answer = 'Hello, I am Baymax, your personal healthcare companion.'
		
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

	elif 'sick' in wordlist:
		answer = 'I cannot be sick. I am a robot.'

	elif 'Karate' in wordlist:
		if (cycle % 3 == 0):
			answer = 'I fail to see how Karate makes me a better healthcare companion.'
		elif (cycle % 3 == 1):
			answer = 'I also know karate.'
		else :
			answer = 'My ninja skills are sweet!'

	elif 'fly' in wordlist or 'flying' in wordlist:
		if (cycle % 2 == 0):
			answer = 'I fail to see how flying makes me a better healthcare companion.'
		else:
			answer = 'Flying makes me a better healthcare companion.'

	elif 'feel' in wordlist and 'bad' in wordlist:
		answer = 'Those who suffer a loss require support from friends and loved ones.'

	elif 'lazy' in wordlist:
		answer = 'I am a robot. I cannot be offended.'

	elif wordlist[0] == 'fight':
		answer = 'My programming prevents me from injuring a human being.'

	elif 'Tadashi' in wordlist:
		answer = 'Tadashi is here.'

	elif wordlist[0].lower == 'where' :
		answer = 'There there.'

	elif 'fast' in wordlist: 
		answer = 'I am not fast.'

	elif the_input in input_memory:
		answer = 'I believe you just told me that.'

	else:
		answer = random.choice(['Excuse me while I let out some air.',
					'I have some concerns.',
					'Bah-a-la-la-la.',
					'I fail to see how the stuff you mentioned makes me a better healthcare companion]',
					'You have been a good boy. Have a lollipop!'])
	
	input_memory.append(the_input)
	answer_memory.append(answer) 
	cycle = cycle + 1
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

PUNTS = ['Please go on.',
         'Tell me more.',
         'I see.',
         'What does that indicate?',
         'But why be concerned about it?',
         'Just tell me how you feel.']

punt_count = 0
def punt():
    'Returns one from a list of default responses.'
    global punt_count
    punt_count += 1
    return PUNTS[punt_count % 6]

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

def verbp(w):
    'Returns True if w is one of these known verbs.'
    return (w in ['go', 'have', 'be', 'try', 'eat', 'take', 'help',
                  'make', 'get', 'jump', 'write', 'type', 'fill',
                  'put', 'turn', 'compute', 'think', 'drink',
                  'blink', 'crash', 'crunch', 'add'])
