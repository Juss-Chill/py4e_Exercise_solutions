'''
Exercise 5: Take the following Python code that stores a string:
str = 'X-DSPAM-Confidence:0.8475'
Use find and string slicing to extract the portion of the string after the
colon character and then use the float function to convert the extracted
string into a floating point number.

'''

str = 'X-DSPAM-Confidence:0.8475'
#sanity check of the string length before proceeding
if len(str) > 0:
    pos = str.find(':')   # store the location where colon first appeared
    float_str = str[pos+1:]
    float_num = float(float_str)
    print("\n This is a string = %s and This is a number %g\n" %(float_str, float_num)) # Format specifiers ==> %s : string, %g: float, %d: decimals
else:
    print('Enter a string of valid length') # this will never gets executed as we are hardcoding the string value

# To learn more on python string methods, Visit : https://docs.python.org/3/library/stdtypes.html#string-methods
