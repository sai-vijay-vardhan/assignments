t = (10, 20, 30, 40, 50, 20, 60)

# 1
print(t.count(20))

# 2
print(t.index(40))

# 3
lst = list(t)
lst.append(70)
t = tuple(lst)

# 4
print(t[2:6])

# 5
t = t + (80, 90)

# 6
print(t * 2)

# 7
print(50 in t)

# 8
a, b, c, d, e, f, g, *rest = t
print(a, b, rest)

# 9 (Error)
# t[0] = 100 TypeError (Immutable)

# 10
nested = (1, 2, (3, 4))
print(nested[2][1])  # 4
