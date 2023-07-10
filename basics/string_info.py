message = "Hello World"
print(len(message))  # 11
print(message[3])  # l

# Slicing
print(message[0:5])  # Hello
print(message[:5])  # Hello
print(message[6:])  # World

print(message.lower())
print(message.upper())
print(message.count('o'))
print(message.find('World'))

new_message = message.replace('World', 'Universe')
print(new_message)

new_var = message + " , " + new_message + '. Welcome'
mess = '{} , {}. Welcome'.format(message, new_message)
mess1 = f'{message} , {new_message.upper()}. Welcome'

print(new_var)
print(mess)
print(mess1)
