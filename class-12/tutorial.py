fruit ="mango"
len1=len(fruit)
print("Length of the string is:",len1)

pie="applepie"
print(pie[:5]) #Slicing from Start
print(pie[5:]) #Slicing from End
print(pie[2:6]) #Slicing in between
print(pie[-8:]) #Slicing using negative index
print(pie[len(pie)-8:]) #Slicing using negative index
print(pie[-3:-2]) #Slicing using negative index

alpha="abcd"
for i in alpha:
    print(i)

print(pie[6])

nm= "harry"
print(nm[-4:-2])