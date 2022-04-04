# Телеграм-бот v.002 - бот создаёт меню
#import BotGames
import bs4
import os
import random
import requests
import telebot
from telebot import types

# BotGames   # pyTelegramBotAPI 4.3.1

# from menuBot import menu


bot = telebot.TeleBot('5212339655:AAGsTq8kzvoXI69MtoGXP6Pm02gH7fzLuX4')  # Создаем экземпляр бота


# Функция, обрабатывающая команду /start

@bot.message_handler(commands=["start"])
def start(message, res=False):
    chat_id = message.chat.id
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("главное меню")
    btn2 = types.KeyboardButton("помощь")
    markup.add(btn1, btn2)
    bot.send_message(chat_id, text="здарова, {0.first_name}! я бот с приколами".format(message.from_user), reply_markup=markup)


@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    chat_id = message.chat.id
    ms_text = message.text

    if ms_text == "главное меню" or ms_text == "Главное меню" or ms_text == "Вернуться в главное меню":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("приколы")
        back = types.KeyboardButton("помощь")
        markup.add(btn1, back)
        bot.send_message(chat_id, text="Вы в главном меню", reply_markup=markup)
    elif ms_text == "приколы":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("случайный мем")
        btn2 = types.KeyboardButton("анекдот")
        btn3 = types.KeyboardButton("подлая еврейская музыка")
        btn4 = types.KeyboardButton("Прислать собаку")
        btn5 = types.KeyboardButton("опоссум")
        back = types.KeyboardButton("Вернуться в главное меню")
        markup.add(btn1, btn2, btn3, btn4, btn5, back)
        bot.send_message(chat_id, text="выберите смешнявку", reply_markup=markup)
    elif ms_text == "/meme" or ms_text == "случайный мем":
        bot.send_message(chat_id, text="ваша картинка для настроения!")
        DIR = 'memes'
        bot.send_photo(chat_id, open(os.path.join(DIR, random.choice(os.listdir(DIR))), 'rb'))
    elif ms_text == "анекдот":
        DIR = 'анекдот'
        file = open(os.path.join(DIR, random.choice(os.listdir(DIR))), 'rb')
        bot.send_message(chat_id, text=file)
    elif ms_text == "/dog" or ms_text == "Прислать собаку":
        contents = requests.get('https://random.dog/woof.json').json()
        urlDOG = contents['url']
        bot.send_photo(chat_id, photo=urlDOG, caption="собака")
    elif ms_text == "опоссум":
        bot.send_photo(chat_id, photo=get_pos(), caption="опоссум")
    elif ms_text == "подлая еврейская музыка":
        bot.send_message(chat_id, text="включаю подлую еврейскую музыку...")
        bot.send_audio(chat_id, open("подлая еврейская музыка.mp3", 'rb'))
    elif ms_text == "помощь" or ms_text == "/help":
        bot.send_message(chat_id, "автор бота Маркова Екатерина 1-МД-5")
        key1 = types.InlineKeyboardMarkup()
        btn1 = types.InlineKeyboardButton(text="Напишите автору", url="https://t.me/rxnp1c")
        key1.add(btn1)
        DIR = 'ава'
        bot.send_photo(message.chat.id, open(os.path.join(DIR, random.choice(os.listdir(DIR))), 'rb'), reply_markup=key1)
    else:
        bot.send_message(chat_id, text='почему ты написал:"' + ms_text + '"?')


def get_pos():
    array_pos = []
    req_pos = requests.get('https://bestrandoms.com/get-random-possum-memes-you-had-no-idea-you-needed')
    soup = bs4.BeautifulSoup(req_pos, "html.parser")
    result_find = soup.find('img', class_='img-responsive')
    for result in result_find:
        array_pos.append(result)
    return array_pos[0]


bot.polling(none_stop=True, interval=0)  # Запускаем бота

print()
