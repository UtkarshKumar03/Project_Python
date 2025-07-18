Student_dict = {'Ayush': 75 ,
                'Alice': 85,
                'Nobita': 60,
                'Alex': 95}
name = input("Enter the student's name: ")

marks = Student_dict.get(name)

if name in Student_dict:
    print(f"{name}'s marks: {marks}")
else:
    print("Student not found")
