# リスト型基本
r = [1, 2, 3, 4, 5, 1, 2, 3]

print(r.index(1, 5))

print(r.count(3))

r.sort()
print(r)
r.sort(reverse=True)
print(r)

r.reverse()
print(r)

s = 'My name is Mike'
to_split = s.split(' ')
print(to_split)

x = ' '.join(to_split)

print(x)

x = '#####'.join(to_split)
print(x)


i = [1, 2, 3, 4, 5]

j = i

j[0] = 100

print('j=', j)
print('i=', i)

x = [1, 2, 3, 4, 5]

y = x.copy()
#y = x[:]
y[0] = 100

print('y=', y)
print('y=', x)

# seat = []
# min = 0
# max = 5
# min <= len(seat) < max
