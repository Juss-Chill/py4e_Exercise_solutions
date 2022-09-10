'''
Exercise 5: This program records the domain name (instead of the
address) where the message was sent from instead of who the mail came
from (i.e., the whole email address). At the end of the program, print
out the contents of your dictionary.
python schoolcount.py
Enter a file name: mbox-short.txt
{'media.berkeley.edu': 4, 'uct.ac.za': 6, 'umich.edu': 7,
'gmail.com': 1, 'caret.cam.ac.uk': 1, 'iupui.edu': 8}

'''
from curses import keyname


words = list()
mails = dict()


try:
    fhandle = open('mbox-short.txt','r')
    print(fhandle)
except:
    print('Error opening the required file')
    exit()

for line in fhandle:
    if line.startswith('From '):
        #print(line.strip())
        words = line.strip().split()
        key_name = words[1].split('@')
        #print(key_name)
        #print(words)
        if len(words) > 0:
            mails[key_name[1]] = mails.get(key_name[1], 0) + 1         # Using get method instead of if-else

print(mails)

