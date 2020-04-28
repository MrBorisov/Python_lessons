class Store:
    def __init__(self, name):
        self.name = name
        self.count_tech = {'printer': 0, 'scanner': 0, 'copier': 0}
        self.tech = {}
        self.inv_num = 100

    def add_tech(self, obj_of_tech):
        """
        Записываем в словарь self.tech значения объекта техники: тип, марка, модель, дата покупки.
        """
        count = self.count_tech[obj_of_tech.type]
        self.count_tech[obj_of_tech.type] = count + 1
        self.tech[self.inv_num] = [obj_of_tech.type, obj_of_tech.mark, obj_of_tech.model, obj_of_tech.date]
        self.inv_num += 1
        return self.name

    def transfer(self, tech_inv):
        tech_info = self.tech.pop(tech_inv)
        count = self.count_tech[tech_info[0]]
        self.count_tech[tech_info[0]] = count - 1
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
                print(Store.recept_add_tech(tech_input, count_of_tech))
            elif int(operation) == 2:
                print(store_1.count_tech)
                print(store_1.tech)
                tech_inv = int(input('Введи инвентарный номер устройства: '))
                store_1.transfer(tech_inv)
                print(f'На складе {store_1.tech}')
                print(f'количество техники на складе {store_1.count_tech}')
            elif int(operation) == 4:
                is_stop = False
                print(f'на складе {store_1.count_tech}')
                print(f'на складе {store_1.tech}')

    @classmethod
    def recept_add_tech(cls, type, count):
        for i in range(int(count)):
            print(f'Добавим {type}: ')
            mark = input(f'введите производителя {type}а:\n')
            model = input(f'введите модель {type}а:\n')
            date = input('введите дату покупки:\n')
            if type == 'printer':
                tech = Printer('printer', mark, model, date, store_1)
            elif type == 'scanner':
                tech = Scanner('scanner', mark, model, date, store_1)
            elif type == 'copier':
                tech = Copier('copier', mark, model, date, store_1)
        return 'Техника добавлена'


class Department(Store):
    def transfer(self, tech_inv, store_obj):
        """
        tech_info список с данными о технике из словаря self.tech, содержит: тип, марка, модель, дата покупки
        """
        tech_info = store_obj.tech.pop[tech_inv]
        count = store_obj.count_tech[tech_info[0]]
        store_obj.count_tech[tech_info[0]] = count - 1

        if tech_info[0] == 'printer':
            tech = Printer('printer', tech_info[1], tech_info[2], tech_info[3], self)
        elif tech_info[0] == 'scanner':
            tech = Scanner('scanner', tech_info[1], tech_info[2], tech_info[3], self)
        elif tech_info[0] == 'copier':
            tech = Copier('copier', tech_info[1], tech_info[2], tech_info[3], self)

    def add_tech(self, obj_of_tech):
        pass


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






