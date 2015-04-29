l1=[i for i in range(1,11)]
print("The list l1 contains the values:")
print(l1)

print()

l2=[i for i in range(10,101,10)]
print("The list l2 contains the values:")
print(l2)

print()

l3=['python','django','flask','string','function','classes']
print("The list l3 contains the values:")
print(l3)

print()

l4={'l1':l1,'l2':l2,'l3':l3}
print("The list l4 contains the values:")
print(l4)

print()

main_list=[l1,l2,l3]
#main_list.append(l1)
#main_list.append(l2)
#main_list.append(l3)

print("The list main_list contains the values:")
print(main_list)

print()

l5=l1*2
print("The list l5 contains the values:")
print(l5)
print()
main_list.append(l5)

print("After appending the l5 list to the main_list")
print(main_list)
print()

occurence=main_list.count(1)
print("Occurence of the 1 in main_list is",occurence)

