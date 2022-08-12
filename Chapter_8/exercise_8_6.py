'''
Exercise 6: Rewrite the program that prompts the user for a list of
numbers and prints out the maximum and minimum of the numbers at
the end when the user enters “done”. Write the program to store the
numbers the user enters in a list and use the max() and min() functions to
compute the maximum and minimum numbers after the loop completes.
Enter a number: 6
Enter a number: 2
Enter a number: 9
Enter a number: 3
Enter a number: 5
Enter a number: done
Maximum: 9.0
Minimum: 2.0

'''

def Add_val(val):
    try:
        val = float(val)
        if val not in all_nums:
            all_nums.append(val)
    except:
        print('Enter a valid Digit')
        
    return all_nums


all_nums = list()
while True:
    val = input('Enter number: ')
    if val == 'done':
        break
    else:
        all_nums = Add_val(val)


print('\nMaximum of the Entered Digits is %g\n'%max(all_nums))
print('\nMinimum of the Entered Digits is %g\n'%min(all_nums))

