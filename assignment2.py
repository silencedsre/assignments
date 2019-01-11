#wap to input names and count letters starting for a-z, case insensitive

# hint: make list of a-z
# make empty dict and assign 0
# take input
# uptade dict

list=[]
dict={}
for letters in range(97,123):
    list.append(chr(letters))
dict={i:0 for i in list}
for i in range(0,3):
    name=input("enter a name"+str(i)+":")
    name=name.lower()
    dict[name[0]]+=1
print(dict)