def str_rev(str):
    str2=""
    print(str[::-1])
    for i in range(len(str)-1,-1,-1):
        print(str[i])
        str2=str2+str[i]
    return str2



def rev_str(str):
    
    for i in range(len(str)-1,-1,-1):
        yield str[i]
   
print("string reverse",str_rev("malayalam"))

for ch in rev_str("laavanya"):
    print(ch)


