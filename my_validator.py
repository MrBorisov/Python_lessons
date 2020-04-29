from time import strptime

def validator(date):
    try:
        list_date = [int(el) for el in date.split('.')]
    except ValueError:
        pass
    try:
        list_date = [int(el) for el in date.split('-')]
    except ValueError:
        pass

    try:
        my_date = '-'.join(map(str, list_date))
    except UnboundLocalError:
        return False
    try:
        valid_date = strptime(my_date, '%d-%m-%y')
        return (f'{valid_date.tm_mday}.{valid_date.tm_mon}.{valid_date.tm_year}')
    except ValueError:
        return False
