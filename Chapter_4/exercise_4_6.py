'''
Exercise 6: Rewrite your pay computation with time-and-a-half for overtime 
and create a function called computepay which takes two parameters
(hours and rate).
Enter Hours: 45
Enter Rate: 10
Pay: 475.0

'''

def computePay(Hrs, Rate):
    OverTime = Hrs-40
    pay = 40 * Rate                               # Normal per hour Hour pay
    pay = pay + (OverTime * Rate * 1.5)           # overtime pay
    print("Pay for", Hrs, "Hours is Rs.",pay)

try:
    Hrs = input("Enter Hours: ")
    Rate = input("Enter Rate: ")
    Hrs = float(Hrs)
    Rate = float(Rate)
    computePay(Hrs, Rate)

except:
    print("Error, please enter numeric input")

    
