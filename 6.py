goods = []  # Список товаров
analytics = {}  # словарь аналитики
list_of_names = []  # список названий товаров
list_of_price = []  # список цен
list_of_count = []  # список количества
list_of_size = []  # список едениц измерения
# В цикле вводим товары
for i in range(int(input('Введите количество товаров: '))):
    good = {}
    good.update({'Название': input('Введите название товара: '), 'Цена': input('Введите цену товара: '),
                 'Количество': input('Введите количество товара: '), 'Ед': input('Введите еденицы измерения товара: ')})
    goods.append((i + 1, good))
# В цикле перебераем знацения в словарь аналитики
for i in goods:
    list_of_names.append(i[1].get('Название'))
    list_of_price.append(i[1].get('Цена'))
    list_of_count.append(i[1].get('Количество'))
    list_of_size.append(i[1].get('Ед'))
    list_of_size = list(set(list_of_size))
analytics.update({"Название": list_of_names, "Цена": list_of_price, "Количество": list_of_count, "Ед": list_of_size})
print(analytics)
