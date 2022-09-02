import telebot
from config import keys, TOKEN
from classes import Exceptions, CryptoConverter

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands = ["start", "help"])
def help(message: telebot.types.Message):
    text = "Чтобы получить ответ, дайте команду боту в формате: \n<название валюты> \
<название второй валюты> \
<количество переводимой валюты> (через пробел) \n \
Чтобы увидеть список доступных валют, введите команду /values"
    bot.reply_to(message, text)

@bot.message_handler(commands = ["values"])
def values(message: telebot.types.Message):
    text = "Для перевода доступны следующие валюты:"
    for key in keys.keys():
        text = "\n".join((text, key, ))
    bot.reply_to(message, text)

@bot.message_handler(content_types = ["text", ])
def convert(message: telebot.types.Message):
    try:
        values = message.text.split(" ")

        if len(values) != 3:
            raise Exceptions("Неверный ввод.")

        val1, val2, amount = values
        sum = CryptoConverter.convert(val1, val2, amount)
    except Exceptions as e:
        bot.reply_to(message, f"Ошибка пользователя\n{e}")
    except Exception as e:
        bot.reply_to(message, f"Не удалось обработать команду\n{e}")
    else:
        text = f"Цена {amount} {val1} в {val2}: {sum}"
        bot.send_message(message.chat.id, text)

bot.polling()
