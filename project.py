#Student Managment System
import sys
i=0
name = input("Please enter your name and your surname : ").title()
while i<3:
  student_name = input("Enter student name and surname: ").title()

  if (student_name == name ):
     print("Welcome:", name)
     break
  else:
     print("Please try again later!")
     i+=1
     if(i==3):
       print("Invalid login")
       sys.exit()

lessons= []
print(lessons)
print(len(lessons))
c = int(input("You choose the number of lessons: "))

while c<3:
    print("You failed in class!")
    sys.exit()

while c>5:
    print("You entered more lessons")
    c = int(input("Enter less than 5 lessons: "))
    break

while c >= 3 and c <= 5:
    break

student_list = []

for i in range(c):
        lesson = input(f"Enter the {i + 1}. lessons of your choose: ")
        student_list.append(lesson)

print(student_list)

cLesson = input("Enter the lesson of your choose:")
print(cLesson)

grades = {'midterm': 0, 'final': 0, 'project':0}

midterm = int(input('Enter your midterm grade: '))
grades['midterm'] = midterm

final = int(input('Enter your final grade: '))
grades['final'] = final

project = int(input('Enter your project grade: '))
grades['project'] = project

grades = {'midterm': midterm, 'final': final, 'project':project}
print(grades)

your_grade = grades['midterm'] * 0.3 + grades['final'] * 0.2 + grades['project'] * 0.5

if your_grade >= 90:
    print(f'You got AA from {cLesson} lesson')

elif 90 > your_grade and your_grade >= 70:
    print(f'You got BB from {cLesson} lesson')

elif 70 > your_grade and your_grade >= 50:
    print(f'You got CC from {cLesson} lesson')

elif 50 > your_grade and your_grade >= 30:
    print(f'You got DD from {cLesson} lesson')

elif 30 > your_grade:
    print("FF")
    print(f'You failed the {cLesson} lesson')