#Generate a list of the first Fibonacci numbers,
#0 being the first number. Then, apply the map function and a lambda expression 
#to cube each fibonacci number and print the list.

list_fabi=[0,1]
n=int(input("enter a num for total fab series: "))
i=0
while i<n-2:
    fabi=list_fabi[-1]+list_fabi[-2]
    list_fabi.append(fabi)
    i+=1
print(list_fabi)

map_obj=map(lambda x:x**3, list_fabi)
print(list(map_obj))
