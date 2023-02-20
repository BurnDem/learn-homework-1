"""
Домашнее задание №1

Использование библиотек: ephem

* Установите модуль ephem
* Добавьте в бота команду /planet, которая будет принимать на вход
  название планеты на английском, например /planet Mars
* В функции-обработчике команды из update.message.text получите
  название планеты (подсказка: используйте .split())
* При помощи условного оператора if и ephem.constellation научите
  бота отвечать, в каком созвездии сегодня находится планета.

"""
import logging
import ephem
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from datetime import date

logging.basicConfig(format='%(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO,
                    filename='bot.log')

def greet_user(update, context):
    text = 'Вызван /start'
    print(text)
    update.message.reply_text(text)


def get_planet(update, context):
    update.message.reply_text('Введите название тела на английском с большой буквы')
    text = update.message.text
    planet = text.split()
    ephem_name = getattr(ephem, 'name')
    for user_planet in planet:
        if hasattr(ephem, user_planet):
            today = date.today()
            ephem_planet = getattr(ephem, user_planet) 
            planet_by_time = ephem_planet(today)
            which_constellation = ephem.constellation(planet_by_time)
            update.message.reply_text(f'{ephem_planet} находится в созвездии {which_constellation}')
        else:
            update.message.reply_text(f'Не могу найти такое тело: {user_planet}')

def main():
    mybot = Updater(settings.API_KEY, use_context=True)

    dp = mybot.dispatcher
    dp.add_handler(CommandHandler("start", greet_user))
    dp.add_handler(CommandHandler("planet", get_planet))
    dp.add_handler(MessageHandler(Filters.text, get_planet))

    mybot.start_polling()
    mybot.idle()


if __name__ == "__main__":
    main()