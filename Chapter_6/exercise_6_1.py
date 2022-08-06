'''
Exercise 1: Write a while loop that starts at the last character in the
string and works its way backwards to the first character in the string,
printing each letter on a separate line, except backwards.

Input = 'Hello'
Output = 
'o
'l'
'l'
'e'
'H'

'''

in_str = input('Enter a string: ')
len_str = len(in_str)          # compute the length of the input string

#print the each character from the backward
index = len_str-1
print('\nPrinting Backwards...')
while index >= 0:
    print(in_str[index])
    index = index - 1

