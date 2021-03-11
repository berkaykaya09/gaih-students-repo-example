#Homework 1
list1 = [1,3,5,7,9]
list2 = [0,2,4,6,8]
list1.extend(list2)
list1.sort()

list1=[x*2 for x in list1]
print(list1)

for i in list1:
    i+=0
    i=print(type(i))