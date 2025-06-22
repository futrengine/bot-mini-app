import telebot
import os
from telebot import types

TOKEN = os.environ.get("BOT_TOKEN")
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    markup = types.InlineKeyboardMarkup()
    web_app = types.WebAppInfo("https://futrengine.github.io/spinwheel")
    markup.add(types.InlineKeyboardButton("🎰 Open Spin", web_app=web_app))
    bot.send_message(message.chat.id, "Tap below to spin the wheel!", reply_markup=markup)

bot.infinity_polling()
