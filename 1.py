def division(dividend, divider):
    """Возвращает результат деления
    Аргументы:
    dividend (float) делимое
    divider (float) делитель
    """
    try:
        return dividend / divider
    except ZeroDivisionError:
        return 'На ноль делить нельзя'


print(division(10.2, 2))
