from operator import itemgetter



lis = [{ "name" : "Karthik Chandler", "age" : 22},  
{ "name" : "Manjeet", "age" : 20 }, 
{ "name" : "Nikhil" , "age" : 19 }]
print(lis)
print("\n\n\n")
print("\nSorting by age\n")
print (sorted(lis,key=itemgetter('age')))
