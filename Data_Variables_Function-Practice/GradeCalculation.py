marks = input("Enter marks: ")
marks = float(marks)

if marks >= 80:
    print("GPA: A+")

elif marks >= 0:
    print("GPA: A-")

elif marks >= 60:
    print("GPA: B")

elif marks >= 50:
    print("GPA: C")

elif marks >= 40:
    print("GPA: D")

else:
    print("GPA: F")