import os

import telebot
import random
import consts
import urllib
from urllib.request import Request, urlopen
#import shelvetry

from quiz import count, generate
from prime import  isprime, inventing
from polynom import creating
from shelvetry import setgame
from radius import deciding
from telebot import types
from shelvetry import getanswer, incscore, decscore, getscore, getdif


bot = telebot.TeleBot("339799773:AAFoi-coRmh7k_b1QGGOK9-7yBLJyOzrj1A")
bot.send_message(120363877, "Начинай")

markupstart = types.ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True)
@bot.message_handler(commands=['start'])
def starting(message):

    markupstart.row("/game", "/trigonometry")
    #markupstart.row("/trigonometry")
    markupstart.row("/logarithm", "/derivativetable")
    #markupstart.row("/derivativetable")
    markupstart.row("/integral", "/randombook")
    #markupstart.row("/randombook")
    markupstart.row("/randomwiki", "/primetheory")
    markupstart.row("/polynomialtheory")
    bot.send_message(message.chat.id, consts.startstr, reply_markup=markupstart)



@bot.message_handler(commands=['game'])
def chosedif(message):
    from shelvetry import setgame
    bot.send_message(message.chat.id, 'Welcome to the victorina.' )
    markup = types.ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True)
    markup.row("/difficult1")
    markup.row("/difficult2")
    markup.row("/difficult3")
    keyboard_hider = types.ReplyKeyboardRemove()
    bot.send_message(message.chat.id, consts.gamestr, reply_markup=markup)
    setgame(message.chat.id)

    #sendingtask()
    #upd = bot.get_updates()
    #diff = message.text
    #game(diff)


@bot.message_handler(commands=['quit'])
def chosedif(message):
    from shelvetry import endgame
    bot.send_message(message.chat.id, 'Goodbye!')
    endgame(message.chat.id)
    bot.send_message(message.chat.id, consts.quitstr, reply_markup=markupstart)

@bot.message_handler(commands=['trigonometry'])
def trig_pict(message):
    directory = "D:/Users/Opsymonroe/Images/botphoto"
    img = open(directory + '/' + 'trigonom.jpg', 'rb')
    bot.send_chat_action(message.from_user.id, 'upload_photo')
    bot.send_photo(message.from_user.id, img)
    bot.send_message(message.from_user.id, consts.wikitrig)

@bot.message_handler(commands=['logarithm'])
def trig_pict(message):
    directory = "D:/Users/Opsymonroe/Images/botphoto"
    img = open(directory + '/' + 'logarifm.jpg', 'rb')
    bot.send_chat_action(message.from_user.id, 'upload_photo')
    bot.send_photo(message.from_user.id, img)
    bot.send_message(message.from_user.id, consts.wikilog)

@bot.message_handler(commands=['derivativetable'])
def trig_pict(message):
    directory = "D:/Users/Opsymonroe/Images/botphoto"
    img = open(directory + '/' + 'proizv.png', 'rb')
    bot.send_chat_action(message.from_user.id, 'upload_photo')
    bot.send_photo(message.from_user.id, img)
    bot.send_message(message.from_user.id, consts.wikider)
    bot.send_message(message.from_user.id, consts.wikidertable)

@bot.message_handler(commands=['integral'])
def trig_pict(message):
    directory = "D:/Users/Opsymonroe/Images/botphoto"
    img = open(directory + '/' + 'pervoobr.jpg', 'rb')
    bot.send_chat_action(message.from_user.id, 'upload_photo')
    bot.send_photo(message.from_user.id, img)
    bot.send_message(message.from_user.id, consts.wikiint)
    bot.send_message(message.from_user.id, consts.wikiinttable)


@bot.message_handler(commands=['primetheory'])
def trig_pict(message):
    bot.send_message(message.from_user.id, consts.wikiprime)


@bot.message_handler(commands=['polynomialtheory'])
def trig_pict(message):
    bot.send_message(message.from_user.id, consts.wikipoly)
    bot.send_message(message.from_user.id, consts.wikiquad)

@bot.message_handler(commands=['randombook'])
def trig_pict(message):
    directory = "D:/Users/Opsymonroe/Documents/botdocs"
    allbooks = os.listdir(directory)
    randbook = random.choice(allbooks)
    doc = open(directory + '/' + randbook, 'rb')
    bot.send_chat_action(message.from_user.id, 'upload_photo')
    bot.send_document(message.from_user.id, doc)


@bot.message_handler(commands=['randomwiki'])
def trig_pict(message):
    req = Request("https://en.wikipedia.org/wiki/Special:Random", headers={'User-Agent': 'Mozilla/5.0'})
    webpage = urllib.request.urlopen(req)
    wiki = webpage.geturl()
    bot.send_message(message.from_user.id, wiki)



from shelvetry import setdif
@bot.message_handler(commands=['difficult1'])
def chosedif(message):
    setdif(message.chat.id, message.text[-1])
    sendingtask(message.chat.id, message.text[-1])

@bot.message_handler(commands=['difficult2'])
def chosedif(message):
    setdif(message.chat.id, message.text[-1])
    sendingtask(message.chat.id, message.text[-1])

@bot.message_handler(commands=['difficult3'])
def chosedif(message):
    setdif(message.chat.id, message.text[-1])
    sendingtask(message.chat.id, message.text[-1])

    #upd = bot.get_updates()
    #diff = message.text
    #game(diff)

def sendingtask(id, diff):
    from quiz import count, generate
    from prime import  isprime, inventing
    from polynom import creating
    from shelvetry import setans
    from radius import deciding
    bool = False
    keyboard_hider = types.ReplyKeyboardRemove()
    mode = random.randint(0, 10)
    mode = mode % 4
    if (mode == 0):
        s = generate(diff)
        setans(id, 0, s)
        bot.send_message(id, s, reply_markup=keyboard_hider)
    if ( mode == 1):
        s = inventing(diff)
        setans(id, 1, s)
        bot.send_message(id, 'Is {} prime? True/False'.format(s), reply_markup=keyboard_hider)
    if(mode == 2):
        s = creating(diff)
        setans(id, 2, s)
        bot.send_message(id, 'Send multiplication of the roots of {}'.format(s), reply_markup=keyboard_hider)
    if ( mode == 3):
        s = deciding(diff)
        setans(id, 3, s)
        bot.send_message(id, s, reply_markup=keyboard_hider)

"""Чел, просто расслабься, будь что будет. Тебе некуда торопиться, у тебя все хорошо.
    Просто сделай отправку всех сообщений отдельно, а чтение отдельно, тогда все будет хорошо."""

@bot.message_handler(func=lambda message: True, content_types=['text'])
def game(message):

    ans = getanswer(message.chat.id)
    if not ans:
        bot.send_message(message.chat.id, 'Type /game to start')
        return
    if(str(ans).lower() ==  message.text.lower()):
        incscore(message.chat.id)
        bot.send_message(message.chat.id, 'Great! Your score now is ' + str(getscore(message.chat.id)) + '.')
    else:
        decscore(message.chat.id)
        bot.send_message(message.chat.id, 'Bad! Right answer is ' + str(ans) + ', and your score now is' +
                         str(getscore(message.chat.id)) + '.')

    sendingtask(message.chat.id, getdif(message.chat.id))



if __name__ == '__main__':
    bot.polling(none_stop=True)

