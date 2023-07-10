courses = ['Maths', 'Python', 'React']
print(courses)
print(len(courses))
print(courses[0])  # Maths
print(courses[-1])  # React
print(courses[0:1])  # ['Maths']
print(courses[2:])  # ['React']
courses.append('Java')
print(courses)
courses.insert(0, 'Art')
print(courses)
courses2 = ['Node']
courses.extend(courses2)
print(courses)
courses.remove('Art')
print(courses)
popValue = courses.pop()
print(courses)
print(popValue)
courses.reverse()
print(courses)
courses.sort()
print(courses)

nums = [1, 5, 3, 4, 0]
nums.sort()
print(nums)
nums.sort(reverse=True)
print(nums)

sortedCourses = sorted(courses)
print(sortedCourses)

print(min(nums))
print(max(nums))
print(sum(nums))

print(courses.index('Java'))
print('Java' in courses)
print('Node' in courses)

for index, course in enumerate(courses):
    print(index, course)

course_string = ', '.join(courses)
print(course_string)
new_courses = course_string.split(', ')
print(new_courses)

# Tuples
# Cannot change the tuples
# list_1 = ['Table', 'Fan', 'Cupboard']
# list_2 = list_1
# list_1[0] = 'Laptop'
# print(list_2) # list_2 also changes
# print(list_1)

# tuple_1 = ('Table', 'Fan', 'Cupboard')
# tuple_2 = tuple_1
# print(tuple_2)
# print(tuple_1)
# tuple_1[0] ='Laptop' # Cannot Change values of Tuple
# print(tuple_1)
# print(tuple_2)

# SETS
# It does not care about order and does not have duplicates
animals = {'Lion', 'tiger', 'Rhino'}
next_animals = {'Lion', 'cheetah', 'Rhino'}
animals.add('Lion')
print(animals)
print(animals.intersection(next_animals))
print(animals.difference(next_animals))
print(animals.union(next_animals))

# Empty List Tuples & Set
empty_list = []
empty_list2 = list()

empty_tuple = ()
empty_tuple2 = tuple()

empty_set = {}  # Its dictionary
empty_set2 = set()
