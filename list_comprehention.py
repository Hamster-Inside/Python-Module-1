my_list = [1, 2, 3]
# new_list = [2,4,6]

new_list = []
for x in my_list:
    new_list.append(x * 2)

# list comprehention:

new_list2 = [x * 2 for x in my_list]
