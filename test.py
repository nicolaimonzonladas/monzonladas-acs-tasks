list1 = [2,5,15,36,47]
list2 = [18,39,42]

sorted_list =[]

print(list1)
print(list2)

while list1 and list2:
    if list1[0] <  list2[0]:
        sorted_list.append(list1.pop(0))
    else:
        sorted_list.append(list2.pop(0))

sorted_list += list1
sorted_list += list2

print(sorted_list)

# print(sorted(list1 + list2))