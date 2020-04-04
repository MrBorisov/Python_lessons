my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
index = 0
for i in range(1, len(my_list), 2):
    my_list[index], my_list[index + 1] = my_list[index + 1], my_list[index]
    index += 2
print(my_list)
