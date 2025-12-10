def calculate_stats(marks):
    mean = sum(marks) /len(marks)
    if mean >= 90:
        grade = 'A'
    elif mean >= 60:
        grade = 'B'
    else:
        grade = 'C'
        
    return mean,grade
    

marks = [90,87,96,86,97]
mean , grade = calculate_stats(marks)


print("Mean:",mean)
print ("grade:",grade)