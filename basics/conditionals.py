if True:
    print('True')

language = 'Java1'
if language == 'Python':
    print('Language is python')
elif language == 'Java':
    print('Language is Java')
else:
    print('Not found')

user = 'Admin'
isLoggedIn = False

if user == 'Admin' and isLoggedIn:
    print('Admin Login Success')
else:
    print('Login Failed')

if user == 'Admin' or isLoggedIn:
    print('Admin Login Success')
else:
    print('Login Failed')

if not isLoggedIn:
    print('Please Login')
else:
    print('Success')

a = '123'
b = '123'

if a is b:
    print('TRUE')
else:
    print('FALSE')

c = [1, 2, 3]
d = [1, 2, 3]

if c is d:
    print('TRUE')
else:
    print('FALSE')

print(id(c))
print(id(d))
print(id(a))
print(id(b))

# False Values (FALSY VALUES)
# cond = False
# cond = None
# cond = 0
# cond = ''
# cond = [],()
cond = {}
if cond:
    print('TRUE')
else:
    print('FALSE')
