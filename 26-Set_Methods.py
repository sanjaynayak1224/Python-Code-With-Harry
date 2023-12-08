s1={1,2,5,6}
s2={3,6,7}
print(s1.union(s2))
print(s1.intersection(s2))

# Symmetric difference
s3=s1.symmetric_difference(s2)
print(s3)

#isdisjont
s4={1,2,3,4}
s5={5,6,7,8}
print(s4.isdisjoint(s5))


#issuperset and issubset
s6={1,2,3,4,5.6,7,8,9,10}
s7={8,9,10,1,7}
print(s6.issuperset(s7))
print(s7.issubset(s6))


#add
s8={1,2,3,4}
s8.add(9)
print(s8)

#update
s9={1,2,3,4}
s10={4,5,6}
s9.update(s10)
print(s9)

#remove
s11={1,2,3,4}
s11.remove(3)
print(s11)


#pop
cities={"Tokyo","Madrid","Berlin","Delhi"}
item=cities.pop()
print(cities)
print(item)


#clear-doesnt delete the entire set but  deletes all the items inside the set retaining the set structure
cities={1,2,3,4}
cities.clear()
print(cities)

#del-deletes the entire set(gives an error that the cities is not defined)
cities={1,2,3,4}
del cities
print(cities)






