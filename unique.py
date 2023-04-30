string=input('enter a string: ')
str=string.lower()
unique=set(str)
len=len(unique)
print("unique = ",end=" ")
for i in unique:
    print(i,end="")
    if len-1>0:
        print(",",end="")
        len=len-1
    
