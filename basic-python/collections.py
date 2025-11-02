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
        if i%2== 0 :
            continue 
        if sum>100:
            break       
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

def fibinoci(n):
    a,b,c=0,1,""
    for i in range(n):
        c=c+str(a)+","
        a,b=b,a+b
    return c

def fibinoci(n):
    a,b=0,1
    print(a,",",b,end=",")
    for i in range(n-2):
        c=a+b
        print(c,end=",")
        a,b=b,c
        
       
    return c

def fibinoci_kum(n):
    a,b=0,1
    for i in range(n):
        print(a,end=",")
        a,b=b,a+b

        
def fib_lst(n):
    fib=[0,1]
    if n<=0:
        return []
    if n==1:
        return[0]
    if n==2:
        return[0,1]
   
   
    for i in range(n-2):
        fib.append(fib[-1]+fib[-2])
    return fib

def fibnoci_lst(n):
    if(n<=0):
        return []
    elif(n==1):
        return [0]
    elif(n==2):
        return [0,1]
    else:
        ls=fibnoci_lst(n-1)
        ls.append(ls[-1]+ls[-2])
        return ls



num=5
print("factorial is ====",fact(num))
print("factorial is ====",fact_recursive(num))
print("fibnoci series\n",fibinoci(num))
print("fibnoci series using recursion and list",fibnoci_lst(num))
print("fib kum",fibinoci_kum(num))
print("fib lst",fib_lst(num))
        

