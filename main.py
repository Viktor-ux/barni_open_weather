import requests
import telebot
import json

bot = telebot.TeleBot('6340229131:AAEsA_4wB-4m1s5iFPTJ5_rw_JRN2lh-Yfc')
API = 'f1796d22955dbfa8bbc4bcc875eb1eab'

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, 'Привет! Чтобы узнать погоду, напиши свой город!')

@bot.message_handler(content_types=['text'])
def weather(message):
    city_name = message.text.lower().strip()
    weather = requests.get(f'https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={API}&units=metric')
    perevod = json.loads(weather.text)
    temp = int(perevod["main"]["temp"])
    bot.reply_to(message, f'Сейчас ровно {temp} °C')

bot.polling(none_stop = True)
