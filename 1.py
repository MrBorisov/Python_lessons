from sys import argv

script_name, production, rate, bonus = argv
try:
   production, rate, bonus = map(int, argv[1:])
   print(f'ЗП = {production * rate} + премия {bonus} = '
   f'{production * rate + bonus}')
except ValueError:
      print('Введены не привильные параметры')