list1=[]
list2=[]
num=int(input("Enter number of items\n"))
n=int(input("Enter number\n"))
for i in range(num):
    
    if(n!=-1):
        list1.append(n)
    else:
        break
print(list1)
for i in range(len(list1)):
    if (list1[i]%2)==0:
        list2.append(list1[i])

print(list2)
    
