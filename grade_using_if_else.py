score = int(input("Enter the student's score: "))

if score >= 90:
    grade = 'A'
elif score >= 80:
    grade = 'B'
elif score >= 70:
    grade = 'C'
elif score >= 60:
    grade = 'D'
else:
    grade = 'F'

print(f"The student's grade is: {grade}")

    ###output
      Enter the student's score: 76
      The student's grade is: C
