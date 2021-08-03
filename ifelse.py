#ifelse.py
score=int(input("Input score:"))

if 90<=score <=100:
    grade="A"
elif 80<=score<90:
    grade="B"
elif 70 <=score <80:
    grade="C"
else:
    grade="D"

print("Grade is",grade)
