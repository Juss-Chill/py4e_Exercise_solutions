'''
Exercise 1: Write a program which repeatedly reads numbers until the
user enters “done”. Once “done” is entered, print out the total, count,
and average of the numbers. If the user enters anything other than a
number, detect their mistake using try and except and print an error
message and skip to the next number.

Enter a number: 4
Enter a number: 5
Enter a number: bad data
Invalid input
Enter a number: 7
Enter a number: done
16 3 5.333333333333333

'''
sum = 0
count =0 
avg = 0 

# Using the function to calculate the average
# inputs : sum of the numbers and count of the numbers entered
# output : average computed by sum/count
def averg(sum, count):
    avg = sum / count
    return avg

#while(1) evelautes to True all the time and hence we need to breakout of it explcitly by using a condition
while 1:
    num = input('Enter a number: ')
    try:
        if num == 'done':
            break
        else:
            num = float(num)
            count = count + 1    # Track the count of number of values entered
            sum = sum + num    #add the numbers
    except:
        print('bad data')

avg = averg(sum, count) 

print('\nTotal: ',sum,'\nCount: ',count,'\nAverage: ',avg)



