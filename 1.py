from sys import argv

script_name, production, rate, bonus = argv

print(f'ЗП = {float(production) * float(rate)} + премия {float(bonus)} = '
      f'{float(production) * float(rate) + float(bonus)}')
