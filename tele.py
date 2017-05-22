import os

import telebot
import random
#import shelvetry

from telebot import types
bot = telebot.TeleBot("339799773:AAFoi-coRmh7k_b1QGGOK9-7yBLJyOzrj1A")
bot.send_message(120363877, "Начинай")

class Difficulty:
    def __init__(self, hard):
        self.dif  = hard
        self.chat_id = 0
    def setdif(self, hard):
        self.dif = hard
    def getdif(self):
        return self.dif
    def set_id(self, ch_id):
        self.chat_id = ch_id
    def get_id(self):
        return self.chat_id

slozh = Difficulty(1)

@bot.message_handler(commands=['start'])
def starting(message):
    markupstart = types.ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True)
    markupstart.row("/game")
    markupstart.row("/trigonometry")
    markupstart.row("/logarithm")
    markupstart.row("/derivativetable")
    markupstart.row("/integral")
    markupstart.row("/randombook")
    bot.send_message(message.chat.id, "Hi, Choose what you want", reply_markup=markupstart)



@bot.message_handler(commands=['game'])
def chosedif(message):

    bot.send_message(message.chat.id, 'Welcome to the victorina.' )
    markup = types.ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True)
    slozh.set_id(message.chat.id)
    markup.row("/difficult1")
    markup.row("/difficult2")
    markup.row("/difficult3")
    keyboard_hider = types.ReplyKeyboardRemove()
    bot.send_message(message.chat.id, "Choose the difficulty from 1 to 3. "
                                " You can also change the difficulty at any moment by"
                                " sending /difficult№, and /quit for ending", reply_markup=markup)

    #sendingtask()
    #upd = bot.get_updates()
    #diff = message.text
    #game(diff)


@bot.message_handler(commands=['quit'])
def chosedif(message):
    from shelvetry import endgame
    bot.send_message(message.chat.id, 'Goodbye!')
    endgame(message.chat.id)


@bot.message_handler(commands=['trigonometry'])
def trig_pict(message):
    directory = "D:/Users/Opsymonroe/Images/botphoto"
    img = open(directory + '/' + 'trigonom.jpg', 'rb')
    bot.send_chat_action(message.from_user.id, 'upload_photo')
    bot.send_photo(message.from_user.id, img)

@bot.message_handler(commands=['logarithm'])
def trig_pict(message):
    directory = "D:/Users/Opsymonroe/Images/botphoto"
    img = open(directory + '/' + 'logarifm.jpg', 'rb')
    bot.send_chat_action(message.from_user.id, 'upload_photo')
    bot.send_photo(message.from_user.id, img)

@bot.message_handler(commands=['derivativetable'])
def trig_pict(message):
    directory = "D:/Users/Opsymonroe/Images/botphoto"
    img = open(directory + '/' + 'proizv.png', 'rb')
    bot.send_chat_action(message.from_user.id, 'upload_photo')
    bot.send_photo(message.from_user.id, img)

@bot.message_handler(commands=['integral'])
def trig_pict(message):
    directory = "D:/Users/Opsymonroe/Images/botphoto"
    img = open(directory + '/' + 'pervoobr.jpg', 'rb')
    bot.send_chat_action(message.from_user.id, 'upload_photo')
    bot.send_photo(message.from_user.id, img)


@bot.message_handler(commands=['randombook'])
def trig_pict(message):
    directory = "D:/Users/Opsymonroe/Documents/botdocs"
    allbooks = os.listdir(directory)
    randbook = random.choice(allbooks)
    doc = open(directory + '/' + randbook, 'rb')
    bot.send_chat_action(message.from_user.id, 'upload_photo')
    bot.send_document(message.from_user.id, doc)



@bot.message_handler(commands=['difficult1'])
def chosedif(message):
    slozh.setdif(1)
    sendingtask(message.text[-1])

@bot.message_handler(commands=['difficult2'])
def chosedif(message):

    slozh.setdif(2)
    sendingtask(message.text[-1])

@bot.message_handler(commands=['difficult3'])
def chosedif(message):
    slozh.setdif(3)
    sendingtask(message.text[-1])

    #upd = bot.get_updates()
    #diff = message.text
    #game(diff)

def sendingtask(diff):
    from quiz import count, generate
    from prime import guessing, isprime, inventing
    from polynom import creating
    from shelvetry import setGame
    from radius import deciding
    bool = False
    keyboard_hider = types.ReplyKeyboardRemove()
    mode = random.randint(0, 10)
    mode = mode % 4
    if (mode == 0):
        s = generate(diff)
        setGame(slozh.get_id(), 0, s)
        bot.send_message(slozh.get_id(), s, reply_markup=keyboard_hider)
    if ( mode == 1):
        s = inventing(diff)
        setGame(slozh.get_id(), 1, s)
        bot.send_message(slozh.get_id(), 'Is {} prime? True/False'.format(s), reply_markup=keyboard_hider)
    if(mode == 2):
        s = creating(diff)
        setGame(slozh.get_id(), 2, s)
        bot.send_message(slozh.get_id(), 'Send multiplication of the roots of {}'.format(s), reply_markup=keyboard_hider)
    if ( mode == 3):
        s = deciding(diff)
        setGame(slozh.get_id(), 3, s)
        bot.send_message(slozh.get_id(), s, reply_markup=keyboard_hider)

"""Чел, просто расслабься, будь что будет. Тебе некуда торопиться, у тебя все хорошо.
    Просто сделай отправку всех сообщений отдельно, а чтение отдельно, тогда все будет хорошо."""

@bot.message_handler(func=lambda message: True, content_types=['text'])
def game(message):
    from shelvetry import getanswer
    ans = getanswer(message.chat.id)
    if not ans:
        bot.send_message(message.chat.id, 'Type /game to start')
        return
    if(str(ans).lower() ==  message.text.lower()):
        bot.send_message(message.chat.id, 'Great!')
    else:
        bot.send_message(message.chat.id, 'Bad!')
    sendingtask(slozh.getdif())



if __name__ == '__main__':
    bot.polling(none_stop=True)

