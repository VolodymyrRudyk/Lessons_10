class Worker:
    def __init__(self, name, pay):              #ініціалізація при створення
        self.name = name                        #self - новий об'єкт
        self.pay = pay
    def lastName(self):
        return self.name.split()[-1]            #розбиття строки по пробілам
    def giveRaise(self, percent):
        self.pay *= (1.0 + percent)             #оновлення pay на місці

bob = Worker('Bob Smith', 50000)                #створення двох екземплярів
sue = Worker('Sue Jones', 60000)                #кожен з них має атрибути name i pay

print(bob.lastName())                           #викликаємо метод: bob - це self
print(sue.lastName())

sue.giveRaise(.10)                              #оновлення атрибута pay в екземплярі sue
print(sue.pay)