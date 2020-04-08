def sum_of_max(arg_1, arg_2, arg_3):
    """
    Суммирует два наибольших аргумента
    :return: число
    """
    args = [arg_1, arg_2, arg_3]
    return sum(args) - min(args)


print(sum_of_max(1, 2, 3))
