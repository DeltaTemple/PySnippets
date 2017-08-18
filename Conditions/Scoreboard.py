#Checks the score using grade letters
score = int(input("Enter your test score: "))

if score == 100:
    grade = "A+"
    print("Perfect score")

elif score >= 90:
    grade = "A"
    print("High grade")

elif score >= 80:
    grade = "B"
    print("Medium grade")

elif score >= 70:
    grade = "C"
    print("Substandard grade")

elif score >= 1:
    print("Failing grade")
    grade = "F"

elif score == 0:
    grade = "F. You christmas-tree'd the test, didn't you?"



print("Your grade: ", grade)
