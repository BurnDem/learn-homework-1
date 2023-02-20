"""

Домашнее задание №1

Условный оператор: Возраст

* Попросить пользователя ввести возраст при помощи input и положить 
  результат в переменную
* Написать функцию, которая по возрасту определит, чем должен заниматься пользователь: 
  учиться в детском саду, школе, ВУЗе или работать
* Вызвать функцию, передав ей возраст пользователя и положить результат 
  работы функции в переменную
* Вывести содержимое переменной на экран

"""


def main(age):
    if age < 7:
      return 'Вы должны быть в дестком саду'
    elif age >= 7 and age <= 17:
      return 'Вы должны учиться в школе'
    elif age >= 18 and age < 23:
      return 'Вы должны учиться в ВУЗЕ'
    else:
      return 'Вы должны работать'

if __name__ == "__main__":
    age = int(input('Введите свой возраст: '))
    desc_age = main(age)
    print(desc_age)