'''
Exercise 2: Rewrite your pay program using try and except so that your
program handles non-numeric input gracefully by printing a message
and exiting the program. The following shows two executions of the
program:
Enter Hours: 20
Enter Rate: nine
Error, please enter numeric input
Enter Hours: forty
Error, please enter numeric input

'''
try:
    Hrs = input("Enter Hours: ")
    Rate = input("Enter Rate: ")
    Hrs = float(Hrs)
    Rate = float(Rate)
    pay = Hrs * Rate
    print("Pay for", Hrs, "Hours is Rs.",pay)

except:
    print("Error, please enter numeric input")

    