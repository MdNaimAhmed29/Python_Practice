marks = input("Enter marks: ")
marks = float(marks)

if 100 >= marks >= 80:
    print("GPA: A+")

elif 80 > marks >= 70:
    print("GPA: A-")

elif 70 > marks >= 60:
    print("GPA: B")

elif 60 > marks >= 50:
    print("GPA: C")

elif 50 > marks >= 33:
    print("GPA: D")

else:
    print("GPA: F")