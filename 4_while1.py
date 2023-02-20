"""

Домашнее задание №1

Цикл while: hello_user

* Напишите функцию hello_user(), которая с помощью функции input() спрашивает 
  пользователя “Как дела?”, пока он не ответит “Хорошо”
   
"""


def hello_user():
    while True:
        user_mood = input("Как дела: ")
        if user_mood == "Хорошо":
            print('OK')
            break
        else:
            user_mood
    
if __name__ == "__main__":
    hello_user()