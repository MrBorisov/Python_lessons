"""Сложно отладить отлаживать такие решения."""
my_list = [i for i in range(20, 241) if not i % 20 or not i % 21]
print(my_list)

"""Преаерка"""
my_list = []
for i in range(20, 241):

    if not i % 20 or not i % 21:
        my_list.append(i)
print(my_list)
