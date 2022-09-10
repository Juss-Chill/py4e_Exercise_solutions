'''
Exercise 1: Download a copy of the file www.py4e.com/code3/words.txt
Write a program that reads the words in words.txt and stores them as
keys in a dictionary. It doesn’t matter what the values are. Then you
can use the in operator as a fast way to check whether a string is in the
dictionary

'''

all_words = dict()

fhandle = open('words.txt')
#print(fhandle)

for line in fhandle:
    lst = line.strip().split()
    if len(lst) > 0:              # Add keys to the dictionary only if the line is valid i.e, Line has some values
    #    print(lst,'------->',len(lst))
        for word in lst:          # Take each word from the list and add it to the dictionary as a key
            all_words[word] = 1
    
print(all_words)

word = input('Enter the word to search: ')
if word in all_words:                        # searches only for the keys not values
    print('\nSearch Found')
else:
    print('\nsearch failed due to non-existence of the word')
