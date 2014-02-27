import argparse
import re

#Accepts input in the command line as "python Alliteration.py args", where 'args' is the name of the file to be checked

parser = argparse.ArgumentParser()
parser.add_argument("file", help = "file to be checked for alliteration")
args = parser.parse_args()

#Retrieves the text file as a string object to allow it to be checked and manipulated
with open(args.file, 'r') as f:
	read_file = f.readlines()
f.close()

letter1 = ''
letter2 = ''

alliteration_string = ['']
top_alliteration_string = ['']

#Keeps count for the sound repetition in each line and for the file, respectively
alliteration_level = 0
top_alliteration_level = 0

for x in range(len(read_file)):
	#Splits the file into lines to be checked individually
	check = re.split('\b([A-Z])', read_file[x], flags = re.IGNORECASE)
	alliteration_level = 0
	alliteration_string = ['']
	letter1 = ''
	letter2 = ''
	for y in range(len(check)):
		#Skips over spaces and blank characters for the purpose of checking first letters
		if check[y] == '' or check[y] == ' ':
			continue
		#Further divides the assigned line into individual words
		test_case = re.split('\s?', check[y], flags = re.IGNORECASE)
		for z in range(len(test_case)):
			if test_case[z] == '':
				continue
			if z > 0:
				letter1 = test_case[z-1][0]
			letter2 = test_case[z][0]
			#Checks whether there is a previous word in the line, and if so whether they share the same first letter
			if z != 0 and letter1.capitalize() == letter2.capitalize():
				alliteration_level = alliteration_level + 1
				if alliteration_string == ['']:
					alliteration_string = test_case[z-1] + ' ' + test_case[z]
				else:
					alliteration_string = alliteration_string + ' ' + test_case[z]
				if alliteration_level > top_alliteration_level:
					top_alliteration_level = alliteration_level
					top_alliteration_string = alliteration_string
				letter1 = letter2
print '~~~~~~~~'
print top_alliteration_string
print '~~~~~~~~'
