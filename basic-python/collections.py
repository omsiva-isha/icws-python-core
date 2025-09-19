lst=[23,45,67,89,34]
lst1=[]
stud_info={"name":"kumutha","age":21,"sex":"F","qualification":"bsc"}
address={"add1":"23 defrr","add2":"vinayagar kovil st","town":"sadivayal"}
stud_info["addr"]=address
lst.append(66)
print(lst)
print("student info  ",stud_info)


def get_info(lst):
    info={}
    sum=0
    for i in lst:
        sum=sum+i
    info["sum"]=sum
    info["count"]= len(lst)
    info["avg"] = sum/info["count"]

    return info

def get_sum(lst):
    
    return get_info(lst)["count"]


for k in stud_info:
    print("key="+ k,"value",stud_info[k])

sum=  get_sum(lst) 
print("sum===",sum)

print("information of list",get_info(lst))

for num in range(5,60,5):
    print(num)


def fact(num):
    fact=1
    for i in range(1,num+1):
        fact=fact*(i)
    return fact

def fact_recursive(num):
    print("insinsid fact to calculate",num)
    if num==1:
        return 1
    

    fact=num*fact_recursive(num-1)
    print(num,"! fact ",fact)
    return fact

num=5
print("factorial is ====",fact(num))
print("factorial is ====",fact_recursive(num))
        

