'''
Exercise 4: Add code to the above program(Exercise-3) to figure out who has the
most messages in the file. After all the data has been read and the dictionary has been created, look through the dictionary using a maximum
loop (see Chapter 5: Maximum and minimum loops) to find who has
the most messages and print how many messages the person has.
Enter a file name: mbox-short.txt
cwen@iupui.edu 5
Enter a file name: mbox.txt
zqian@umich.edu 195

'''

words = list()
mails = dict()
max_mails = None         # To hold max mailing list number

try:
    fhandle = open('mbox.txt','r')
    print(fhandle)
except:
    print('Error opening the required file')
    exit()

for line in fhandle:
    if line.startswith('From '):
        #print(line.strip())
        words = line.strip().split()
        if len(words) > 0:
            mails[words[1]] = mails.get(words[1], 0) + 1         # Using get method instead of if-else

# Loop to capture the max mails number into the variable max_mails
for key in mails:
    #print(key, mails[key])
    if max_mails is None:
        max_mails = mails[key]
        max_mail_name = key
    elif max_mails < mails[key]:
        max_mails = mails[key]
        max_mail_name = key

print(max_mail_name, ':',max_mails)
