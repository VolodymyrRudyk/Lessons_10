L = [None] * 100
print(L)

print(type(L))                 #Типи: класом L є list
print(type(type))

if type(L) == type([]):        #перевірка типу при необхідності...
    print('yes')

if type(L) == list:            #використання імені класу
    print('yes')

if isinstance(L, list):        #об'єктно-орієнтована перевірка
    print('yes')