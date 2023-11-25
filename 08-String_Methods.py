# Strings are immutable i.e they cannot be changed but creates a copy and then changes it
a='harry'
print(len(a))
print(a.upper())
print(a.lower())
b='!!harry!!!!'
print(b.rstrip('!'))
c='sanjay'
print(c.replace('sanjay','john'))
d='!!!sanjay !!!nayak'
print(d.split(" "))
blog='introduction tO jS'
(print(blog.capitalize()))

str1='welcome to the console'
print(str1.center(50))
print(d.count('a'))

str2='Welcome to the console!!!'
print(str2.endswith('!!!'))
print(str2.endswith('to',4,10))         #can use .startswith() also
print(str2.find('e'))
print(str2.find('to'))
# u can also use str1.index() which is same as str1.find() but instead of returning -1 as the output when a character is not present,it returns an error
str3='sanjaynayak1224'
print(str3.isalnum())
print(str2.isalnum())
print(str3.isalpha())
print(str2.islower())
print(str2.isupper())
print(str2.isprintable())
print(str2.isspace())
print(str2.istitle())   #returns true if first letter of each of word is in capitals
print(str3.swapcase())
print(str3.title())

