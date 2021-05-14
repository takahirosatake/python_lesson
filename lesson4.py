# 辞書型のコピー

# 辞書型
x = {'a': 1}

# 参照渡し
y = x
y['a'] = 1000
print(x)
print(y)

y = {'a': 1}


# 辞書型のコピー
x = {'a': 1}

y = x.copy()
y['a'] = 1000

print(x)
print(y)

# 辞書型の使い方

fruits = {
    'apple': 100,
    'banana': 200,
    'orange': 300,
}
print(fruits['apple'])

list = [
    ['apple', 100],
    ['banana', 200],
    ['orange', 300],
]

print(list[1][1])
