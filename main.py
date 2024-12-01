   # Словари и множества

   # 1.Работа со словарем
my_dict = {'Vasya': 1975, 'Egor': 1999, 'Masha': 2002}
   # Вывод словаря на экран
print(my_dict)
   # Вывод существующего значения по ключу
print('Existing value:', my_dict['Masha'])
   # Вывод несуществующего значения по ключу
print('Not existing value:', my_dict.get('Kamila', 'Такого значения нет'))
   # Добавление двух произвольных пар в словарь
my_dict.update({'Oleg': 1972, 'Anna': 1982})
print(my_dict)
   # Удалите одной из пар в словаре по существующему ключу
   # и вывод значения из этой пары на экран
s = my_dict.pop('Masha')
print('Modified dictionary:', my_dict)
print(s)

   # 2. Работа со множеством
my_set = {'утро', 'день', 'утро', 'день', 'день', 12, 24, 12, (1, 2), (1, 2)}
   # Вывод множества на экран
print(my_set)
   # Добавление двух произвольных элементов
my_set.update(['вечер', 36])
print(my_set)
   # Удаление одного любого элемента из множетва
my_set.remove((1, 2))
   # Вывод на экран измененного множества
print('Modified set:', my_set)