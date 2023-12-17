dic={"Harry":"Human Being","Spoon":"Object"}
print(dic)
print(dic["Harry"])  #gives "KeyError"
#or
print(dic.get("Harry")) #doesnt throw error instead prints "None"
#or
for key in dic.keys():
    print(f"The Value Corresponding to the keys is {dic[key]}")
print(dic.keys())
print(dic.values())
print(dic.items())
#or
print('*'*81)
for key, value in dic.items():
    print(f"The Value Corresponding to the keys is {value}")
