revenue = int(input('Введите выручку: '))
costs = int(input('Введите издержки: '))
profit = revenue - costs
if profit > 0:
    profitability = profit / revenue
    print(f'Ваша прибыль = {profit}, рентабельность = {profitability:.2f}')
elif profit < 0:
    losses = costs - revenue
    print(f'Ваши убытки = {losses}')
else:
    print('Вы вышли в ноль')

personal = int(input('Введите числиность сотрудников: '))
if profit > 0:
    profit_person = profit / personal
    print(f'Прибыль на сотрудника = {profit_person:.2f}')
else:
    print('У вас убыток, сожалею...')