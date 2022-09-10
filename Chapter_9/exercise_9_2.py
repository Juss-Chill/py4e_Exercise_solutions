'''
Exercise 2: Write a program that categorizes each mail message by
which day of the week the commit was done. To do this look for lines
that start with “From”, then look for the third word and keep a running
count of each of the days of the week. At the end of the program print
out the contents of your dictionary (order does not matter).
Sample Line:
From stephen.marquard@uct.ac.za Sat Jan 5 09:14:16 2008
Sample Execution:
python dow.py
Enter a file name: mbox-short.txt
{'Fri': 20, 'Thu': 6, 'Sat': 1}

'''
count = 0
lst = list()
days = dict()   # TO track the number of days

try:
    fhandle = open('mbox-short.txt')
    print(fhandle)
except:
    print('File open error')
    exit()

for line in fhandle:
    if line.startswith('From '):     # Filter only line that starts with 'From '
        lst = line.strip().split()   # Form a list with the words in the line
        if len(lst) > 0:
            if lst[2] in days:
                #print('present')
                days[lst[2]] += 1 
            else:
                #print('Absent')
                days[lst[2]] = 1 


print(days)

