my_list = [16, 5.2, 3+5j, 'text', False, None, (1,2,3), ['a', 'b'], set('barabekus'), frozenset('mrborisov'),
           {"first": 1, 2: 'second', 3: None}, bytes(10)]
list_of_types = []
for element in my_list:
    list_of_types.append(type(element))
for i in enumerate(list_of_types):
    print(i)
