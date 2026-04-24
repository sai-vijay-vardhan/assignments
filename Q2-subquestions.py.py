data = [10, 20, 30, 40, 50, 20, 30, 60, 70, 80, 90]

# 1. append()
data.append([100, 110])

# 2. extend()
data.extend([120, 130])

# 3. insert()
data.insert(2, 25)

# 4. remove()
data.remove(20)

# 5. pop()
last_element = data.pop()

# 6. count()
count_30 = data.count(30)

# 7. index()
index_40 = data.index(40)

# 8. reverse()
data.reverse()

print("List after operations:", data)
print("Popped:", last_element)
print("Count of 30:", count_30)
print("Index of 40:", index_40)