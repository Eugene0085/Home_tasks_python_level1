# Автор: Кондратенко Евгений
# Задание №1 Easy

User_list = [int(i) for i in input('Введите список ').split()]
New_list = [i**2 for i in User_list]
print(New_list)

#Задание №2 Easy

Fruit_list1 = [str(i) for i in input("Введите первый список фруктов ").split()]
Fruit_list2 = [str(j) for j in input("Введите второй список фруктов ").split()]
Compare_list = list(set(Fruit_list1) & set(Fruit_list2))# пересечение множеств
print(Compare_list)

#Задание №3 Easy


Digit_list = [int(i) for i in input('Введите список ').split()]
 Modified_list = [i for i in Digit_list if i % 3 == 0 and i >= 0 and i % 4 != 0]
 print(Modified_list)




