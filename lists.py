first_list=[1,2,3,4]
first_list.append(5)
first_list.append(6)

second_list=[7,8,9,10,11]

first_list.extend(second_list)#just like javascript spread operator

first_list.insert(0,0)
first_list.reverse()
first_list.sort()

print(first_list.count(2))
print(first_list.index(2))
print(first_list)
