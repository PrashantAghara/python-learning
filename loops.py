nums = [1, 2, 3, 4, 5]

for num in nums:
    if num == 3:
        print('FOUND')
        break
    print(num)

for num in nums:
    if num == 3:
        print('FOUND')
        continue
    print(num)

for num in nums:
    for char in 'abc':
        print(num, char)

for i in range(3):
    print(i)

for i in range(1, 3):
    print(i)

x = 0
while x < 10:
    if x == 5:
        break
    print(x)
    x += 1
