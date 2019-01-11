#wap to compare two list and return same elements in another list
list_one=[1,2,3,4]
list_two=[2,3,4,5,6]
list_three=[]
for i in list_one:
    for j in list_two:
        if i==j:
            list_three.append(j)
print(list_three)

#wap to list a divisor of a num
list=[]
num=int(input("enter a num:"))
for i in range(1,num):
    if num%i==0:
        list.append(i)
list.append(num)
print(list)

