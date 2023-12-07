letter= "Hey my name is {1} and I am from {0}"
country="India"
name="Harry"

print(letter.format(country,name))
print(f"Hey my name is {name} and I am from {country}")

txt="For only {price:.2f} dollars!"
print(txt.format(price=49.0999))
price=49.09999
txt=f"For only {price:.2f} dollars!"
print(txt)

print(f"{2*30}", type(f"{2*30}"))