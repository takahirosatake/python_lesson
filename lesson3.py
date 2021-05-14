# タプル型アンパッキング

num_tuple = (10, 20)

print(num_tuple)

x, y = num_tuple

print(x, y)

x, y = 10, 20
print(x, y)

min, max = 0, 100

print(min, max)


a, b, c, d, e, f = 'mike', '1', '2', '3', '4', '5'

print(a)
print(c)

# アンパッキング
i = 10
j = 20

tmp = i
i = j
j = tmp
print(i, j)

a = 100
b = 200
print(a, b)
a, b = b, a

print(a, b)

# タプルの使い道 リスト違い中身の変えることができないので、固定する時に使いやすい
chose_from_two = ('A', 'B', 'C')

answer = []
answer.append('A')
answer.append('B')

print(chose_from_two)
print(answer)
