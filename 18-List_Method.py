l = [1, 2, 5, 12, 8, 7, 99, 70, 1, 1, 5, 6]
# l.append(6)
# print(l)
# l.sort()
# print(l)
# l.sort(reverse=True)
# print(l)
# l.reverse()
# print(l)
print(l.index(70))
print(l.count(1))
m = l.copy()
m[0] = 0
print(m)
print(l)
l.insert(1, 899)
print(l)
m = [900, 100, 1110]
k = l+m
print(k)
l.extend(m)
print(l)
