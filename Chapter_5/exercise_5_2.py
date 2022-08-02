'''
Exercise 2: Write another program that prompts for a list of numbers
as exercise:5_1 and at the end prints out both the maximum and minimum of
the numbers instead of the average.

'''
max_val = None    # None is a special data type
min_val = None

# Function to calculate the Largest value entered so far
def Largest(num, max_val):
    if (max_val == None) or (max_val < num):
        max_val = num
    return max_val
    
# Function to calculate the Smallest value entered so far
def Smallest(num, min_val):
    if (min_val == None) or (min_val > num):
        min_val = num
    return min_val

while 1:
    num = input('Enter a number: ')
    try:
        if num == 'done':
            break
        else:
            num = float(num)

        max_val = Largest(num, max_val)
        min_val = Smallest(num ,min_val)

    except:
        print('bad data')

print('\nLargest number so far is ....',max_val,'\nSmallest number so far is .....',min_val)
