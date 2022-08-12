'''
Exercise 1: Write a function called chop that takes a list and modifies
it, removing the first and last elements, and returns None. Then write
a function called middle that takes a list and returns a new list that
contains all but the first and last elements.

'''
# chop 
# input : list
# output: None 
# Functionality: modifies it, removing the first and last elements, and returns None.

def chop(rem_fl):
    front = rem_fl[1:]
    front_len = len(rem_fl)
    last = front[:front_len-2]
    print('\nModified List using chop: ',last)


# middle
# input : list
# ouput : list
# Function: returns a new list that contains all but the first and last elements.
def middle(rem_fl):
    front = rem_fl[1:]
    front_len = len(rem_fl)
    last = front[:front_len-2]
    return last


lst = list()
res = list()
count = input('Enter the Number of Elements: ')
count = int(count)

while count > 0:
    ele = input('\nEnter the elements of the list: ')
    if len(ele) > 0:
        lst.append(ele)
        count = count - 1
    else:
        print('\nPlease enter the Data....Do not leave it blank')
        
print('\nOriginal List',lst)
chop(lst)                          # Returns nothing
res = middle(lst)                  # retuens modified list
print('\nModfied list using Middle function: ',res)
print('\nOriginal List left unmodified: ',lst)








