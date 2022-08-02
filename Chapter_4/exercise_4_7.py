'''
Exercise 7: Rewrite the grade program from the previous chapter using
a function called computegrade that takes a score as its parameter and
returns a grade as a string.
Score Grade
>= 0.9 A
>= 0.8 B
>= 0.7 C
>= 0.6 D
< 0.6 F
Enter score: 0.95
A
Enter score: perfect
Bad score

'''



def computeGrade(score):

    if score >= 0.9 and score  < 1.0:
        return 'A'
    elif score >= 0.8 and score < 0.9:
        return 'B'
    elif score >= 0.7 and score < 0.8:
        return 'C'
    elif score >= 0.6 and score < 0.7:
        return 'D'
    elif score < 0.6:
        return('F')
    else:
        return('Bad Score')


try:
    score = input("Enter score: ")
    score = float(score)
    grade = computeGrade(score)
    if score >=0 and score < 1.0:
        print('Grade for score',score,'is = ',grade)
    else:
        print('Score out of Range')
    
except:
    print('Bad Score, Please enter a Real number between 0.0 and 1.0')

    