for i in range(10):
    if(i==8):
        break
    print(i,end=' ')
print()
for i in range(11):
    if(i==8):
        print("Exclude 8")
        continue
    print(i,end=' ')
   