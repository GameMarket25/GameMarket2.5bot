import telebot
from config import TOKEN, CHANNEL_ID
from buttons import get_main_menu

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    user = message.from_user
    bot.send_message(user.id,
        "🎮 Добро пожаловать в GameMarket 2.5!\n\n"
        "GameMarket 2.5 — топ-площадка для покупки и продажи аккаунтов игр 2025 года.\n"
        "Обязательно подпишитесь на наш канал: https://t.me/GameMarket_Accounts\n\n"
        "Выберите, что хотите сделать:",
        reply_markup=get_main_menu()
    )

@bot.message_handler(func=lambda message: message.text == "Купить")
def handle_buy(message):
    bot.send_message(message.chat.id, "Вы выбрали 'Купить'. Функция скоро будет доступна.")

@bot.message_handler(func=lambda message: message.text == "Продать")
def handle_sell(message):
    bot.send_message(message.chat.id, "Вы выбрали 'Продать'. Функция скоро будет доступна.")

bot.polling(none_stop=True)
