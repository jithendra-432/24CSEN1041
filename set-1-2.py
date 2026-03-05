m1 = int(input())
m2 = int(input())
m3 = int(input())





avg = (m1 + m2 + m3) / 3


if avg >= 90:
    grade = "O"
elif avg >=80:
    grade = "A+"
elif avg >=70:
    grade = "A"
elif avg >=60:
    grade = "B+"
elif avg >=50:
    grade = "B"
elif avg >= 45:
    grade = "C"
elif  avg >=40:
    grade = "P"
else:
    grade = "F"


print("Average is:",round(avg,2), "Grade is", grade)


84
75
88
Average is: 82.33 Grade is A+
