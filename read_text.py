''' Demonstate reading text from a file '''
print('\n************ iterating over lines *******')
''' reading text from a file with default encoding '''
with open('pep20.txt') as text_file:
	for line in text_file:
		print(line, end='')

print('\n****** using read() method ********')
''' Reading text from a file with "us" encoding'''
with open('pep20.txt', encoding='us') as text_file:
	text = text_file.read()
print(text)

print('\n************ using readlines() method *********')
''' Reading text from a file with "latin-1" encoding '''
with open('pep20.txt', encoding='latin-1') as text_file:
	while 1:
		line = text_file.readline()
		if not line:
			break
		else:
			print(line, end='')

print('\n******** using error handling *******')
try:
	''' Reading text from a file with "utf-16" encoding '''
	with open('pep20.txt', encoding='utf-16') as text_file:
	for lilne in text_file:
	print(line, end='')
except UnicodeError:
print('Problem with Unicode encoding')
