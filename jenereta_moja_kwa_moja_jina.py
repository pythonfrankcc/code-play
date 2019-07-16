import string,random
#reading the documentation
#print(help(string))
#print(string.ascii_letters)
#print(string.ascii_lowercase)
#giving the script a list of letters to choose from which is only those that are in the brackets
#print(random.choice('pull a letter from here'))
#remember that for the above choice the random.choice can still pick a whitespace as a value  
#bbprint(random.choice(string.ascii_lowercase))
#since we are through with the tests we can comment out the above tests and remain with only the relevant parts
'''def generator():
	first_letter=random.choice(string.ascii_lowercase)
	second_letter=random.choice(string.ascii_lowercase)
	third_letter=random.choice(string.ascii_lowercase)
	fourth_letter=random.choice(string.ascii_lowercase)
	fifth_letter=random.choice(string.ascii_lowercase)
	name = first_letter +second_letter+third_letter+fourth_letter+fifth_letter
	return(name)
print(generator())'''
#now the above is totally based on the computer lets now as the user for some input
letter_input_1 = input('choose a letter..."v" for vokali,"k" for konsonanti,"l" for other Kiswahili words,you can also input your own preference')
letter_input_2 = input('choose a letter..."v" for vokali,"k" for konsonanti,"l" for other Kiswahili words,you can also input your own preference')
letter_input_3 = input('choose a letter..."v" for vokali,"k" for konsonanti,"l" for other Kiswahili words,you can also input your own preference')
letter_input_4 = input('choose a letter..."v" for vokali,"k" for konsonanti,"l" for other Kiswahili words,you can also input your own preference')
letter_input_5 = input('choose a letter..."v" for vokali,"k" for konsonanti,"l" for other Kiswahili words,you can also input your own preference')
#define the vowels and consonants
vokali='aeiou'
konsonanti='bcdfghjklmnpqrstvwxyz'
l=['ch','sh','kh','ah']
letter=string.ascii_lowercase
#building a conditional clause for the generator to go through
def generator1():
	if letter_input_1=="v":
		letter_1=random.choice(vokali)
	elif letter_input_1=="k":
		letter_1=random.choice(konsonanti)
	elif letter_input_1=="l":
		letter_1=random.choice(l)
	else:
		letter_1=letter_input_1#case where the user decides to input his own personal value


	if letter_input_2=="v":
		letter_2=random.choice(vokali)
	elif letter_input_2=="k":
		letter_2=random.choice(konsonanti)
	elif letter_input_1=="l":
		letter_1=random.choice(l)
	else:
		letter_2=letter_input_2


	if letter_input_3=="v":
		letter_3=random.choice(vokali)
	elif letter_input_3=="k":
		letter_3=random.choice(konsonanti)
	elif letter_input_1=="l":
		letter_1=random.choice(l)
	else:
		letter_3=letter_input_3


	if letter_input_4=="v":
		letter_4=random.choice(vokali)
	elif letter_input_4=="k":
		letter_4=random.choice(konsonanti)
	elif letter_input_1=="l":
		letter_1=random.choice(l)
	else:
		letter_4=letter_input_4


	if letter_input_5=="v":
		letter_5=random.choice(vokali)
	elif letter_input_5=="k":
		letter_5=random.choice(konsonanti)
	elif letter_input_1=="l":
		letter_1=random.choice(l)
	else:
		letter_5=letter_input_5
	name=letter_1+letter_2+letter_3+letter_4+letter_5
	return(name)
print(generator1())