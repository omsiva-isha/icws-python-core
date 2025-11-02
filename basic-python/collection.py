# Online Python compiler (interpreter) to run Python online.
# Write Python 3 code in this online editor and run it.
mylist=[1,2,3,4,4,5]
mylist[4]=5
mylist[5]=6
mylist.append(7)
del mylist[2]
print(mylist)
print(mylist[4])

mylist=(1,2,3,4,4,5)

print(mylist)
print(mylist[4])

mylist={1,2,3,4,4,5}
mylist.remove(4)
mylist.add(6)
print(mylist)

my_dict={"name":"siva","age":24}
my_dict["grade"]="A"
print(my_dict["name"])
my_dict["age"]=42
print(my_dict)

mylist=["apple","orange","gooseberry"]

print("========Loop==========")
for i in mylist:
    print(i)
print("=====range==========")
for i in range(3):
    print(mylist[i])
    
for i in range(0,10,2):
    print(i)
print("=====range in reverse==========")
for i in range(10,-1,-1):
    print(i)

my_dict={"name":"siva","age":24}
my_dict["grade"]="A"
print(my_dict["name"])
my_dict["age"]=42
print(my_dict)

for k in my_dict:
    print("key=",k," values =",my_dict[k])
    print(f"key={k}  values ={my_dict[k]}")

for v in my_dict.values():
    print( "values =",v)
    
for key, value in my_dict.items():
    print(f"{key}: {value}")


n=20
for i in range(2,n+1):
    count =0
    for j in range(2,i):
        if(i%j==0):
            count=1
            break
    if count==0:
        print(f"{i} is prime number")

for i in range(n+1):
    if(i%2==0):
        continue
    print(f"{i} is odd number")
    