# CSE 415 Winter 2019
# Assignment 1
# Jichun Li 1531264

# Part A
# 1
def five_x_cubed_plus_1(x):
	return 5 * (x ** 3) + 1

#2
def pair_off(ary):
    result = []
    
    for i in range(0, int(len(ary) / 2 * 2), 2):
        result.append([ary[i], ary[i + 1]])
    if (int (len(ary) % 2) == 1):
        result.append([ary[-1]])
    return result

#3
def mystery_code(input_string):
	result = ''
	for c in input_string:
		next_char = c
		if str.isalpha(c):
			if c.upper() < 'H':
				if c.islower():
					next_char = chr(ord(c) + 19).upper()
				else:
					next_char = chr(ord(c) + 19).lower()
			else:
				if c.islower():
					next_char = chr(ord(c) - 7).upper()
				else:
					next_char = chr(ord(c) - 7).lower()
		result = result + next_char
	return result

#4
def past_tense(words):
	result = []
	irregular_dict = {'have':'had',
			  'be':'was',
			  'eat':'ate',
			  'go':'went'}
	for word in words:
		word = str.lower(word)
		if word in irregular_dict.keys():
			result.append(irregular_dict[word])
		elif word[-1] is 'e':
			result.append(word + 'd')
		elif word[-1] is 'y' and word[-2] not in 'aeiou':
			result.append(word[:-1] + 'ied')
		elif word[-2] in 'aeiou' and word[-1] not in 'aeiouwy' and word[-3] not in 'aeiou':
			result.append(word + word[-1] + 'ed')
		else:
			result.append(word + 'ed')
	return result
