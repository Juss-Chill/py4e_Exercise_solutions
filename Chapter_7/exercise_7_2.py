'''
Exercise 2: Write a program to prompt for a file name, and then read
through the file and look for lines of the form:
X-DSPAM-Confidence: 0.8475

When you encounter a line that starts with “X-DSPAM-Confidence:”
pull apart the line to extract the floating-point number on the line.
Count these lines and then compute the total of the spam confidence
values from these lines. When you reach the end of the file, print out
the average spam confidence.
Enter the file name: mbox.txt
Average spam confidence: 0.894128046745
Enter the file name: mbox-short.txt
Average spam confidence: 0.750718518519

'''
ind = 0
sum = 0
count = 0
len_str = len('X-DSPAM-Confidence:')
file_name = input('Enter the file name[No need to add the extension of the File]: ')
fhandle = open(file_name+'.txt','r')     

for line in fhandle:
    ind = line.find('X-DSPAM-Confidence:')
    if ind == 0:                                 # To print only the statements that the substring has been found. ind = 0 when the substring is found else it will be -1
        #print(line[ind + len_str:].strip())
        sum = sum + float(line[ind + len_str:])  # Computing the sum of the Flot values recovered from the string
        count = count + 1                        # Count the number of values as this is required to compute average

print('\nNum of Values = %d\nSum of all Floating point Numbers = %g\nAverage = %g \n' %(count, sum, sum/count))
