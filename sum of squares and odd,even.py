n=int(input("enter the number of elements:"))
mylist=[]
i=0
odd=0
even=0
while(i<n):
    m=int(input("enter the number"))
    mylist.append(m)
    i+=1
    print("the given list is:",mylist)
    for i in mylist:
        if(i%2==0):
            even+=i**2
        else:
            odd+=i**2
print("(",odd",",even,")") 
