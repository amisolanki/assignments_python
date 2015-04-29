list1=[1,2,3,4,5,6,'a','xyz']
list2=[7,8,9,10,['e','f'],100]

list1.append(list2)

print("*************After the append operation*********")
for i in list1:
    print(i)

print("************After the extend operation***********")
list1.extend(list2)
for i in list1:
    print(i)




