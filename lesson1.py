print('hello')
print(r'c: \name\name')
print('hello. \n how are you')

print('#########')
print("""\
line1
line2
line3\
""")

print('#########')

print('hi'*3 + "mike")

word = 'python'

print(word[0])
print(word[1])
print(word[-1])
print(word[0:3])

word = 'j' + word[1:]

print(word[:])


n = len(word)
print(n)

s = 'My name is mike. hi mike'
print(s)

is_start = s.startswith('My')

print(is_start)

is_start = s.startswith('x')
print(is_start)
print(s.find('mike'))
print(s.rfind('mike'))
print(s.count('mike'))

print(s.capitalize())

print(s.replace('mike', 'alex'))


a = 'a'
print(f'a is {a}')

x, y, z = 1, 2, 3
print(f'a is {x}, {y}, {z}')
print(f'a is {z}, {y}, {x}')

name = 'Jun'
family = 'Sakai'
print(f'My name is {name} {family}. Watashi ha {family} {name}')
