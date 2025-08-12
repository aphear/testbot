import telebot
import os

TOKEN = os.getenv("7741869669:AAF0s1Z4Av-Pt_xnWWFIgP7kTGBE14uh-mw")  # Railway থেকে সেট হবে
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to(message, "✅ Bot is running 24/7 from Railway!")

bot.infinity_polling()
