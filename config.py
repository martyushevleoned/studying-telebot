from telebot import types

TOKEN = '1930787466:AAERwu1bGmJXd2jkgTwrjTDBK0kLUD6SW0s'


class Keyboard(object):
    main_key = types.InlineKeyboardMarkup()
    main_key.add(types.InlineKeyboardButton(text='дз', callback_data='day_key'))
    main_key.add(types.InlineKeyboardButton(text='расписание', callback_data='get_schedule'))

    back_key = types.InlineKeyboardMarkup()
    back_key.add(types.InlineKeyboardButton(text='назад', callback_data='back'))

    day_key = types.InlineKeyboardMarkup()
    day_key.add(types.InlineKeyboardButton(text='понедельник', callback_data='0'))
    day_key.add(types.InlineKeyboardButton(text='вторник', callback_data='1'))
    day_key.add(types.InlineKeyboardButton(text='среда', callback_data='2'))
    day_key.add(types.InlineKeyboardButton(text='четверг', callback_data='3'))
    day_key.add(types.InlineKeyboardButton(text='пятница', callback_data='4'))
    day_key.add(types.InlineKeyboardButton(text='суббота', callback_data='5'))
    day_key.add(types.InlineKeyboardButton(text='воскресенье', callback_data='6'))
    day_key.add(types.InlineKeyboardButton(text='назад', callback_data='back'))
