#   страница 163
"""
Напиши программу, которая спрашивает у пользователя пять имен. Програм-
ма должна хранить имена в списке и выводить их все в конце. Она должна
выглядеть примерно так:
Введи пять имен:
Тоня
Паша
Коля
Миша
Витя
Имена: Тоня Паша Коля Миша Витя
"""
"""
Измени программу из вопроса 1 так, чтобы она выводила оригинальный
список имен и отсортированный.
"""
"""
nameList = []
print("Введи пять имен (нажимай клавишу Enter после каждого имени):")
for i in range(5):
name = input()
nameList.append(name)
print("Имена:", nameList)
print("Замени одно имя. Какое? (1-5):", end=' ')
replace = int(input())
new = input("Новое имя: ")
nameList[replace - 1] = new
print("Имена:", nameList)
"""
#   Дан произвольный список.
#   Представьте его в обратном порядке.

newList = [1, 2, 3, 4, 5]
newList.sort(reverse=True)
print(newList)

#   Напишите функцию change(lst), которая принимает список и меняет местами его первый и последний элемент.
#   В исходном списке минимум 2 элемента.

