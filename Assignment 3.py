print("Enter the number of students:")
number = int(input())
i=number
students = []
for i in range(number):
    if number > 0:
     student = number - (i + 1)
     print(f"Enter student {i + 1} name:")
     name = input()
     print(f"Enter student {name} grade:")
     grade = int(input())
     students.append((name, grade))
for name, grade in students: #I used AI here, because it was only printing the last student's name & grade
     print(f"{name} - {grade}")

for name, grade in students:
 if grade < 60:
   print(f"Failed Students: {name}")

for name, grade in students:
   max_grade = max([g for _, g in students]) #I used AI [g for _, g in students] because it was giving error without it & didn't know why
   if grade == max_grade:
      print(f"Max Grade student is: {name},{grade}")

      #I didn't know how to make the programe calculate the users average grades
      



    
