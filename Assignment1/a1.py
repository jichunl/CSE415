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
	for i in range(0, len(ary), 2):
		result.append([ary[i],ary[i+1]])
	return result

#3
def mystery_code(str):

	
