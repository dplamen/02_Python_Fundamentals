mark = float(input())

def grades(grade):
    grade_in_words = ''
    if 2 <= grade < 3:
        grade_in_words = 'Fail'
    elif 3 <= grade < 3.50:
        grade_in_words = 'Poor'
    elif 3.5 <= grade < 4.50:
        grade_in_words = 'Good'
    elif 4.50 <= grade < 5.50:
        grade_in_words = 'Very Good'
    elif 5.50 <= grade <= 6:
        grade_in_words = 'Excellent'
    print(grade_in_words)

grades(mark)