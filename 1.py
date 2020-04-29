from time import strptime


class Data:

    @classmethod
    def conversion(cls, date_str):
        my_date = [int(el) for el in date_str.split('-')]
        return Data.validator(my_date)

    @staticmethod
    def validator(date):
        my_date = '-'.join(map(str, date))
        try:
            valid_date = strptime(my_date, '%d-%m-%y')
            return (f'{valid_date.tm_mday}.{valid_date.tm_mon}.{valid_date.tm_year}')
        except ValueError:
            return ('Invalid date!')


d = Data()
print(Data.conversion('1-12-13'))
print(d.conversion('1-13-20'))
print(d.conversion('31-12-85'))
