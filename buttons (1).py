from telebot import types

def get_main_menu():
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add(types.KeyboardButton("Купить"), types.KeyboardButton("Продать"))
    return markup
