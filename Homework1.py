#Homework 1
list1=list(range(1,10,2))
list2=list(range(0,10,2))
list3=list1+list2
list3=[x*2 for x in list3]

for i in list3:
    print(type(i))