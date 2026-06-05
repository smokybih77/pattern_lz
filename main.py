from tasks import HouseBuilder, Dish, Combo, Light, LightOnCommand, LightOffCommand, Remote


# 1
print('Строитель')
builder = HouseBuilder()
house = builder.set_walls('картонные').set_roof('соломенная').set_windows('панорамные').build()     # по цепочке строим дом, 
print(house)


# 2
print('\n Компоновщик')
# создаем блюда
pizza = Dish('пицца', 34)
cola = Dish('кола', 4)
fries = Dish('фри', 5)
# создаем комбо и добавляем в него еду
combo_lunch = Combo('обеденное комбо')
combo_lunch.add(pizza)
combo_lunch.add(cola)
# и добавляем в большой сет ранее созданное комбо
big_set = Combo('большой сет')
big_set.add(combo_lunch)
big_set.add(fries)
big_set.show()      # вывод



# 3
print('\n Команда')
lamp = Light()
cmd_on = LightOnCommand(lamp)       # команда включение
cmd_off = LightOffCommand(lamp)     # выключения
remote = Remote()
# добавляем в очередь команды на включение и выключение света
remote.add(cmd_on)      
remote.add(cmd_off)
# запуск
remote.run()