# 集合型set型
a = {1, 2, 3, 4, 5, 6}

print(type(a))

b = {2, 3, 6, 7}

print(a-b)
# aに該当するbの値を差し引く ->{1, 4, 5}

print(b-a)
# bに該当するaの値を差し引く-> {7}

print(a & b)
# ->{2, 3, 6}
print(a | b)
# ->{1, 2, 3, 4, 5, 6, 7}
print(a ^ b)
# ->{1, 4, 5, 7}

# method

s = {1, 2, 3, 4, 5, }
s.add(6)

print(s)

s.remove(6)

print(s)

s.clear()
print(s)

# 集合型の使い所

my_friends = {'A', 'B', 'C'}

A_friends = {'B', 'D', 'E', 'F'}

print(my_friends & A_friends)

f = ['apple', 'banana', 'apple', 'banana']

kind = set(f)
print(kind)
