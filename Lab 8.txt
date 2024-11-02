#2.1
student = {'name' : 'Adam', 'assignment' : [82, 56, 44, 30], 'lab' : [78.20, 77.20], 'test' : [78, 77]}
print(student)

print(" ")
print("***")
print(" ")

#2.2
count = len(student['assignment']) + len(student['lab']) + len(student['test'])
check = {student['name']: count}
print(check)

print(" ")
print("***")
print(" ")

#2.3
def final_grade(student, count):
    if count < 4:
        student['final_grade'] = 0
    else:
        assignment_avg = sum(student['assignment']) / len(student['assignment'])
        test_avg = sum(student['test']) / len(student['test'])
        lab_avg = sum(student['lab']) / len(student['lab'])
        student['final_grade'] = 0.3 * assignment_avg + 0.5 * lab_avg + 0.2 * test_avg
    return student

student2 = {'name': 'Kevin','assignment': [82, 30],'test': [],'lab': [78.2]}
count2 = len(student2['assignment']) + len(student2['lab']) + len(student2['test'])

print(final_grade(student, count))
print(final_grade(student2, count2))

print(" ")
print("***")
print(" ")

#2.4
def students_dict(*students):
    students_dict = {}
    for student in students:
        students_dict[student['name']] = {
            'assignment': student.get('assignment', []),
            'test': student.get('test', []),
            'lab': student.get('lab', []),
            'final_grade': student.get('final_grade', 0)
        }
    return students_dict

students = students_dict(student, student2)
print(students)
