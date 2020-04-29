from my_validator import validator


class Store:
    def __init__(self, name):
        self.name = name
        self.count_tech = {'printer': 0, 'scanner': 0, 'copier': 0}
        self.tech = {}
        self.inv_num = 100

    def __str__(self):
        return f'На складе {self.count_tech} \n{self.tech}'

    def add_tech(self, obj_of_tech):
        """
        Записываем в словарь self.tech значения объекта техники: тип, марка, модель, дата покупки.
        """
        count = self.count_tech[obj_of_tech.type]
        self.count_tech[obj_of_tech.type] = count + 1
        self.tech[self.inv_num] = [obj_of_tech.type, obj_of_tech.mark, obj_of_tech.model, obj_of_tech.date, self.name]
        self.inv_num += 1
        return self.name

    def transfer(self, tech_inv, department):
        tech_info = self.tech[tech_inv]
        count = self.count_tech[tech_info[0]]
        self.count_tech[tech_info[0]] = count - 1
        tech_info = tech_info[:-1]
        tech_info.append(department)
        self.tech.update({tech_inv: tech_info})
        print('Техника перенесена')
        return

    @classmethod
    def recept(cls):
        is_stop = True
        while is_stop:
            print('Добро пожаловать в убежише № 13')
            print('В убежище есть один склатд Main Store')
            operation = input('Что тебе надо, житель убежища? 1 - добавить технику, 2 - взять технику '
                              '4 - чтобы закончить работу\n')
            if int(operation) == 1:
                tech_input = input('Что вы принесли? 1 - printer, 2 - scanner, 3 - copier 4 - чтобы закончить работу\n')

                if int(tech_input) == 1:
                    tech_input = 'printer'
                elif int(tech_input) == 2:
                    tech_input = 'scanner'
                elif int(tech_input) == 3:
                    tech_input = 'copier'
                elif int(tech_input) == 4:
                    is_stop = False
                count_of_tech = input('Сколько техники вы принесли? ')
                while True:
                    if count_of_tech.isdigit():
                        print(Store.recept_add_tech(tech_input, count_of_tech))
                        break
                    else:
                        print('вы ввели не допустимое значение')
                        count_of_tech = input('Сколько техники вы принесли? ')
            elif int(operation) == 2:
                print(store_1.count_tech)
                print(store_1.tech)
                tech_inv = int(input('Введи инвентарный номер устройства: '))
                department = input('Введите код отдела 1 - IT, 2 - FIN:\n')
                if department == '1':
                    department = 'IT'
                else:
                    department = 'FIN'
                store_1.transfer(tech_inv, department)
                print(store_1)
            elif int(operation) == 4:
                is_stop = False
                print(store_1)

    @classmethod
    def recept_add_tech(cls, type, count):
        for i in range(int(count)):
            print(f'Добавим {type}: ')
            mark = input(f'введите производителя {type}а:\n')
            model = input(f'введите модель {type}а:\n')
            date = input('введите дату покупки в формате d-m-y:\n')
            while True:
                date = validator(date)
                if date == False:
                    print('Выввели не правильную дату')
                    date = input('введите дату покупки в формате d-m-y:\n')
                else:
                    break

            if type == 'printer':
                tech = Printer('printer', mark, model, date, store_1)
            elif type == 'scanner':
                tech = Scanner('scanner', mark, model, date, store_1)
            elif type == 'copier':
                tech = Copier('copier', mark, model, date, store_1)
        return 'Техника добавлена'


class OrgTech:
    def __init__(self, type, mark, model, date, store_obj, inv_num=0):
        self.type = type
        self.mark = mark
        self.model = model
        self.date = date
        self.inv_num = inv_num
        self.locate = store_obj.add_tech(self)


class Printer(OrgTech):
    pass


class Scanner(OrgTech):
    pass


class Copier(OrgTech):
    pass


store_1 = Store('Main Store')
Store.recept()
