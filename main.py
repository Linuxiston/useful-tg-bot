# Bot for internal using with useful functions
# Author: Shukrullo Turgunov
# Contact: https://t.me/Shukrullo
# E-mail: shookrullo@gmail.com

import os
from datetime import datetime
from dotenv import load_dotenv
import requests
import telebot

from hadis import pick_random_quote

# loading .env file
dotenv_path = os.path.join(os.path.dirname(__file__), '.env')
if os.path.exists(dotenv_path):
    load_dotenv(dotenv_path)

bot = telebot.TeleBot(os.environ.get('BOT_TOKEN', ''), parse_mode=None)


# handling start command
@bot.message_handler(commands=['start'])
def welcome(message):
    bot.reply_to(message, "Salom! Siz /start buyrug'ini yubordingiz!")


# handle super group left and join messages
@bot.message_handler(content_types=['new_chat_members', 'left_chat_member', 'new_chat_title',
                                    'new_chat_photo', 'delete_chat_photo'])
def delete_messages(message):
    bot.delete_message(message.chat.id, message.id)
    if message.content_type == 'new_chat_members':
        first_name = message.from_user.first_name or ''
        last_name = message.from_user.last_name or ''
        bot.send_message(
            message.chat.id,
            f"Assalomu alaykum {first_name} {last_name}! Davramizga xush kelibsiz!")


# prayer times
@bot.message_handler(commands=['namoz'])
def prayer_times(message):
    today = datetime.now().strftime("%d-%m-%Y")
    resp = requests.get("http://api.aladhan.com/v1/timingsByCity/{}?city=Tashkent&country=UZ&method=6&school=1".format(today))

    data = resp.json()

    print("Ma'lumotlar olindi")
    times = data['data']['timings']
    date = data['data']['date']['gregorian']['date']
    
    times = f"""
    🕋 Namoz vaqtlari
    🕒 Sana: {date}

    🌏 Mintaqa: Toshkent
    ☀️ Quyosh: {times['Sunrise']}
    🌇 Quyosh botishi: {times['Sunset']}

    🕔 Bomdod (Saharlik): {times['Fajr']}
    🕛 Peshin: {times['Dhuhr']}
    🕔 Asr: {times['Asr']}
    🕕 Shom (Iftor): {times['Maghrib']}
    🕗 Hufton: {times['Isha']}

    ☝️📖 {pick_random_quote()}

    ☺️ Kanalimizga obuna bo'ling - @qoriya 
    """
    bot.reply_to(message, times)


bot.polling()
