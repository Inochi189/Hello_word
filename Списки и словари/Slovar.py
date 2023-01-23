#   Кортеж – неизменяемый список
#   Вместо квадратных скобок используются круглые.
#   Поскольку кортежи неизменны, ты не можешь сортировать их, добавлять или
#   удалять элементы. Когда кортеж создан, он остается таким всегда.

my_tuple = ('red', 'green', 'blue')
print(my_tuple)

VanyaMarks = [55, 63, 77, 81]
DimaMarks = [63, 61, 67, 95]
DashaMarks = [97, 95, 92, 88]

mathMarks = [55, 65, 97]
scienceMarks = [63, 61, 65]
readingMarks = [77, 67, 92]
spellingMarks = [81, 72, 88]

classMark = [VanyaMarks, DimaMarks, DashaMarks]
print(classMark)

classMark = [[55, 63, 77, 81], [63, 61, 67, 95], [97, 95, 92, 88]]
print(classMark)

for studentMarks in classMark:
    print(studentMarks)

print(classMark[0][2])

"""
Словари
"""
phoneNumber = {"Ivan": "555-1231", "Masha": "555-1232", "Borya": "555-1233", "Jenya": "555-1234"}
print(phoneNumber)

print(phoneNumber['Masha'])

print(phoneNumber.keys())
print(phoneNumber.values())

print(list(phoneNumber.keys()))

print(list("Privet!"))

"""
Сортировка по ключу
"""
for key in sorted(phoneNumber.keys()):
    print((key, phoneNumber[key]))

"""
Сортировка по значению.
В данном случае, получив отсортированный список значений, мы нашли ключ
каждого из них. Затем мы просмотрели все ключи, пока не нашли тот, который
был связан с этим значением.
Также при работе со словарями
"""
for value in sorted(phoneNumber.values()):
    for key in phoneNumber.keys():
        if phoneNumber[key] == value:
            print(key, phoneNumber[key])

#   функция del для удаления элемента:

del phoneNumber['Ivan']
print(phoneNumber)

#   функцию clear() для удаления всех элементов (очистки словаря):

phoneNumber.clear()
print(phoneNumber)

phoneNumber = {"Ivan": "555-1231", "Masha": "555-1232", "Borya": "555-1233", "Jenya": "555-1234"}
if "Ivan" in phoneNumber:
    print('true')
else:
    print('else')
