def function_fac(n):
    if n==0:
        fac=1
        print(fac)
    else:
        fac=n
        while n>1:
            fac=fac*(n-1)
            n=n-1
        print("factorial is: "+str(fac))
anynum=int(input("enter any num for factorial:"))
function_fac(anynum)

def function_max(x):
    # print(x)
    i=0
    for items in x:
        if items>x[i]:
            i+=1
    return items

num=int(input("how many no: "))
i=0
list1=[]
while i<num:
   inputs=int(input("enter the no: "))
   list1.append(inputs)
   i=i+1
print("max of them is: " +str(function_max(list1)))

import re
def funtion_string(string1):
    alphabets=re.findall('\S',string1)
    return alphabets
any_string=input("enter a string lower and uppercase:")
list_alphabets=funtion_string(any_string)
lower=0
upper=0
for alphabet in list_alphabets:
    if alphabet.islower():
        lower+=1
    else:
        upper+=1
print("lower is "+str(lower)+" upper is "+ str(upper))

import re
def function_string(list_hypen1):
    list_hypen1.sort()
    string_sorted='-'.join(list_hypen1)
    print(string_sorted)


input_hypen=input("Enter hypen seperated string:")
list_hypen=input_hypen.split("-")
# list_hypen=re.findall('\S+?-',input_hypen)
# print(list_hypen)
function_string(list_hypen)