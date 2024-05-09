grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
a_grades = {}
print(a_grades)
s_students = sorted(students)
print(s_students)
for i, student in enumerate(s_students):
    a_grade = sum(grades[i]) / len(grades[i])
    a_grades[student] = a_grade
print(a_grades)
