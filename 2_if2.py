"""

Домашнее задание №1

Условный оператор: Сравнение строк

* Написать функцию, которая принимает на вход две строки
* Проверить, является ли то, что передано функции, строками. 
  Если нет - вернуть 0
* Если строки одинаковые, вернуть 1
* Если строки разные и первая длиннее, вернуть 2
* Если строки разные и вторая строка 'learn', возвращает 3
* Вызвать функцию несколько раз, передавая ей разные праметры 
  и выводя на экран результаты

"""

def main(first, second):
    if first != str(first) or second != str(second):
        return 0
    elif first == second:
        return 1
    elif first != second and len(first) > len(second):
        return 2
    elif first != second and second == 'learn':
        return 3
    else:
        return 4

if __name__ == "__main__":
    print(main(1, "top"))
    print(main(1,1))
    print(main("chad", 1))
    print(main("top", "top"))
    print(main("supertop", "top"))
    print(main("top", "supertop"))
    print(main("top", "learn"))
