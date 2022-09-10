'''
Exercise 3: Write a program to read through a mail log, build a histogram using a dictionary to count how many messages have come from
each email address, and print the dictionary.
Enter file name: mbox-short.txt
{'gopal.ramasammycook@gmail.com': 1, 'louis@media.berkeley.edu': 3,
'cwen@iupui.edu': 5, 'antranig@caret.cam.ac.uk': 1,
'rjlowe@iupui.edu': 2, 'gsilver@umich.edu': 3,
'david.horwitz@uct.ac.za': 4, 'wagnermr@iupui.edu': 1,
'zqian@umich.edu': 4, 'stephen.marquard@uct.ac.za': 2,
'ray@media.berkeley.edu': 1}

'''
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
        if len(words) > 0:
            #if words[1] in mails:
            #    mails[words[1]] += 1
            #else:
            #    mails[words[1]] = 1
            mails[words[1]] = mails.get(words[1], 0) + 1         # Using get method instead of if-else

print(mails)