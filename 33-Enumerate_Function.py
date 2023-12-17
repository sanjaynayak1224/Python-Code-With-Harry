marks=[12,56,32,98,12,45,1,4]

# index=0
# for mark in marks:
#     print(mark)
#     if(index==3):
#         print("Harry,awesome!")
#     index +=1

for index, mark in enumerate (marks):
# for index, mark in enumerate (marks,start=1):takes starting index as 1
    print(mark)
    if(index==3):
        print("Harry,awesome!")