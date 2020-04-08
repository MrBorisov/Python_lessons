def add_anketa(name, secondname, birth, city, email, phone):
    """
    Принимает значения: имя, фамилия, год рождения, город проживания, email, телефон
    :return: словарь со значениями
    """
    anketa = dict(Имя=name, Фамилия=secondname, Год_рождения=birth, Город_проживания=city, Email=email,
                  Телефон=phone)
    return anketa


print(add_anketa('Дмитрий', 'Черный', '15.01.1986', 'Город', 'mrborisovv@gmail.com', '+79444459326'))
