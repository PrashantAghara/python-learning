# It's a key value pair
student = {'name': 'Prashant', 'age': 23, 'courses': ['Java', 'Python']}
print(student)
print(student['name'])
print(student.get('name'))
print(student.get('phone','Not Found'))
student['phone'] = '12345678901'
print(student)
student.update({'name': 'ABC', 'age': 25, 'phone' : '23456789'})
print(student)
del student['age']
print(student)
phone = student.pop('phone')
print(student)
print(phone)
print(len(student))
print(student.keys())
print(student.values())
print(student.items())

for key, value in student.items():
    print(key, value)