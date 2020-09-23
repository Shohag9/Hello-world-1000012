Student = (int(input("Enter total number of students,N:")))
print(Student)
for i in (1,Student):
    continue
    if(Student>=Student):
        break
        roll = int(input("Enter your roll number:"))
        name = input("Enter student name:")
        num1 = int(input("Enter the first number:"))
        num2 = int(input("Enter the second number:"))
        num3 = int(input("Enter the third number:"))
        num4 = int(input("Enter the fourth number:"))
        num5 = int(input("Enter the fifth number:"))
        num6 = int(input("Enter the sixth number:"))
        num7 = int(input("Enter the seventh number:"))
        avg = (num1+num2+num3+num4+num5+num6+num7)/7
        if (avg >= 90):
            print("Grade : A+")
        elif (avg >= 80):
            print("Grade : A")
        elif (avg >= 70):
            print("Grade : A-")
        elif (avg >= 60):
            print("Grade : B")
        elif (avg >= 50):
            print("Grade : C")
        elif (avg >= 40):
            print("Grade  : D")
        else:
            print("Grade  : F")
        print("Roll :", roll)
        print("Name :", name)

