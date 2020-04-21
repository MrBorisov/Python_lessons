"""
Реализуйте базовый класс Car. У данного класса должны быть следующие атрибуты: speed, color, name, is_police (булево).
А также методы: go, stop, turn(direction), которые должны сообщать, что машина поехала, остановилась, повернула (куда).
Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar. Добавьте в базовый класс метод show_speed,
который должен показывать текущую скорость автомобиля. Для классов TownCar и WorkCar переопределите метод show_speed.
При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.
Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к атрибутам, выведите результат. Выполните
вызов методов и также покажите результат.

"""


class Car:
    def __init__(self, color, name, is_police):
        self.color = color
        self.name = name
        self.is_police = is_police
        self.speed = 0

    def go(self, v):
        self.speed = v
        print(f'Машина {self.name} поехала со скоростью {self.speed}')

    def stop(self):
        self.speed = 0
        print(f'Машина {self.name} остановилась')

    def trun(self, direction):
        self.direction = direction
        print(f'Машина {self.name} повернула {self.direction}')

    def show_speed(self):
        print(self.speed)


class TownCar(Car):

    def show_speed(self):
        if self.speed > 60:
            print(f'Вы превысили скорость, ваша скорость = {self.speed}')


class SportCar(Car):
    def go(self, v):
        if v < 120:
            print('Это спортивный автомобиль, он не предназначен для медленной езды')
            print('Давай газу!!!')
        else:
            self.speed = v
            print(f'Машина {self.name} поехала со скоростью {self.speed}')


class WorkCar(Car):

    def show_speed(self):
        if self.speed > 40:
            print(f'Вы превысили скорость, ваша скорость = {self.speed}')


class Police(Car):
    def __init__(self, color, name, is_police, police_flasher):
        super().__init__(color, name, is_police)
        self.police_flasher = police_flasher

    def pursuit(self):
        self.police_flasher = True

    def go(self, speed):
        self.speed = speed
        if self.police_flasher:

            print(f'{self.name} В погоню!!!')
        else:
            print(f'{self.name} Поехали.')

s = SportCar('Red', 'Ferrary', False)
print(f'{s.name} {s.color}')
s.go(80)
s.go(320)
print()
r = Police("black", "Robocop car", True, False)
print(f'{r.name} {r.color} {r.is_police} {r.police_flasher}')
r.go(50)
r.pursuit()
print(f'Мигалка!!! {r.police_flasher}')
r.go(50)
print()
cargo = WorkCar('yellow', 'Funcargo', False)
cargo.go(50)
cargo.show_speed()
cargo.stop()
cargo.go(40)
print()
t = TownCar('green', 'toyota', False)
t.go(70)
t.show_speed()
t.trun('left')
