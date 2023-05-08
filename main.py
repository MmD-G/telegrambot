import telebot
from telegrambot import start

bot=telebot.TeleBot("5976022503:AAE9_SqTIZV5UlwWNa4UJbRtZWvsKrhnir4")

@bot.message_handler(commands= ["start"])
def welcome(message):
    telegrambot.start(message.chat.id)


bot.infinity_polling()