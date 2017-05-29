import os

import telebot
import random
import consts
import urllib
import shelve
from urllib.request import Request
from telebot import types
from shelvetry import getanswer, incscore, decscore, getscore, getdif


geoanswer = shelve.open("geoanswer")



bot = telebot.TeleBot(consts.bottoken)
bot.send_message(120363877, "Начинай")

markupstart = types.ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True)
@bot.message_handler(commands=['start'])
def starting(message):

    markupstart.row("/game", "/trigonometry")
    markupstart.row("/logarithm", "/derivativetable")
    markupstart.row("/integral", "/randombook")
    markupstart.row("/randomwiki", "/primetheory")
    markupstart.row("/polynomialtheory", "/geogame")
    bot.send_message(message.chat.id, consts.startstr, reply_markup=markupstart)



@bot.message_handler(commands=['game'])
def game_com(message):
    from shelvetry import setgame
    bot.send_message(message.chat.id, 'Welcome to the victorina.' )
    markup = types.ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True)
    markup.row("/difficult1")
    markup.row("/difficult2")
    markup.row("/difficult3")
    keyboard_hider = types.ReplyKeyboardRemove()
    bot.send_message(message.chat.id, consts.gamestr, reply_markup=markup)
    setgame(message.chat.id)

@bot.message_handler(commands=['quit'])
def quit_com(message):
    from shelvetry import endgame
    bot.send_message(message.chat.id, 'Goodbye!')
    endgame(message.chat.id)
    bot.send_message(message.chat.id, consts.quitstr, reply_markup=markupstart)


@bot.message_handler(commands=['quitgeo'])
def quit_geo(message):
    del geoanswer[str(message.chat.id)]
    bot.send_message(message.chat.id, 'Goodbye!')
    bot.send_message(message.chat.id, consts.quitstr, reply_markup=markupstart)


@bot.message_handler(commands=['trigonometry'])
def trig_theory(message):
    directory = "D:/Users/Opsymonroe/Images/botphoto"
    img = open(directory + '/' + 'trigonom.jpg', 'rb')
    bot.send_chat_action(message.from_user.id, 'upload_photo')
    bot.send_photo(message.from_user.id, img)
    bot.send_message(message.from_user.id, consts.wikitrig)

@bot.message_handler(commands=['logarithm'])
def log_theory(message):
    directory = "D:/Users/Opsymonroe/Images/botphoto"
    img = open(directory + '/' + 'logarifm.jpg', 'rb')
    bot.send_chat_action(message.from_user.id, 'upload_photo')
    bot.send_photo(message.from_user.id, img)
    bot.send_message(message.chat.id, consts.wikilog)

@bot.message_handler(commands=['derivativetable'])
def der_theory(message):
    directory = "D:/Users/Opsymonroe/Images/botphoto"
    img = open(directory + '/' + 'proizv.png', 'rb')
    bot.send_chat_action(message.chat.id, 'upload_photo')
    bot.send_photo(message.chat.id, img)
    bot.send_message(message.chat.id, consts.wikider)
    bot.send_message(message.chat.id, consts.wikidertable)

@bot.message_handler(commands=['integral'])
def int_theory(message):
    directory = "D:/Users/Opsymonroe/Images/botphoto"
    img = open(directory + '/' + 'pervoobr.jpg', 'rb')
    bot.send_chat_action(message.chat.id, 'upload_photo')
    bot.send_photo(message.chat.id, img)
    bot.send_message(message.chat.id, consts.wikiint)
    bot.send_message(message.chat.id, consts.wikiinttable)


@bot.message_handler(commands=['primetheory'])
def prime_theory(message):
    bot.send_message(message.chat.id, consts.wikiprime)


@bot.message_handler(commands=['polynomialtheory'])
def pol_theory(message):
    bot.send_message(message.chat.id, consts.wikipoly)
    bot.send_message(message.chat.id, consts.wikiquad)

@bot.message_handler(commands=['randombook'])
def rand_book(message):
    directory = "D:/Users/Opsymonroe/Documents/botdocs"
    allbooks = os.listdir(directory)
    randbook = random.choice(allbooks)
    doc = open(directory + '/' + randbook, 'rb')
    bot.send_chat_action(message.chat.id, 'upload_photo')
    bot.send_document(message.chat.id, doc)


@bot.message_handler(commands=['randomwiki'])
def rand_wiki(message):
    req = Request("https://en.wikipedia.org/wiki/Special:Random", headers={'User-Agent': 'Mozilla/5.0'})
    webpage = urllib.request.urlopen(req)
    wiki = webpage.geturl()
    bot.send_message(message.chat.id, wiki)



from shelvetry import setdif
@bot.message_handler(commands=['difficult1'])
def chosedif(message):
    setdif(message.chat.id, message.text[-1])
    sendingtas(message.chat.id, message.text[-1])

@bot.message_handler(commands=['difficult2'])
def chosedif(message):
    setdif(message.chat.id, message.text[-1])
    sendingtas(message.chat.id, message.text[-1])

@bot.message_handler(commands=['difficult3'])
def chosedif(message):
    setdif(message.chat.id, message.text[-1])
    sendingtas(message.chat.id, message.text[-1])

@bot.message_handler(commands=['geogame'])
def geogame(message):
    bot.send_message(message.chat.id, consts.geostart)
    geoanswer[str(message.chat.id)] = [0, 0]
    startgeo(message.chat.id)



@bot.message_handler(func=lambda message: True, content_types=['location'])
def location(message):
    from distance import distance, score
    geobase = shelve.open("D:/Users/Opsymonroe/Documents/botgeobase/geobase")
    mas = str(message.location).split(',')
    lat2 = mas[1][12: len(mas[1])-1]
    lon2 = mas[0][13: len(mas[1])]
    list = geoanswer[str(message.chat.id)]
    lat1 = geobase[geoanswer[str(message.chat.id)][0]][0]
    lon1 = geobase[geoanswer[str(message.chat.id)][0]][1]
    dist = distance(lat1, lon1, lat2, lon2)
    score1 = score(dist)
    list = geoanswer[str(message.chat.id)]
    score1 += float(list[1])
    list[1] = str(score1)
    geoanswer[str(message.chat.id)] = list
    bot.send_message(message.chat.id, message.from_user.first_name + ", Your guess was " + str(dist) + " km from correct location, and your score now is "
                     + str(geoanswer[str(message.chat.id)][1]))
    geobase.close()
    startgeo(message.chat.id)


def startgeo(id):
    geobase = shelve.open("D:/Users/Opsymonroe/Documents/botgeobase/geobase")
    keys = list(geobase.keys())
    lockey = random.choice(keys)
    list1 = geoanswer[str(id)]
    list1[0] = lockey
    geoanswer[str(id)] = list1
    geodir = "D:/Users/Opsymonroe/Images/botgeo/"
    img = open(geodir + lockey + '.jpg', 'rb')
    bot.send_chat_action(id, 'upload_photo')
    bot.send_photo(id, img)
    print(str(geobase[lockey]))
    geobase.close()

def sendingtas(id, diff):
    from quiz import count, generate
    from prime import  isprime, inventing
    from polynom import creating
    from shelvetry import setans
    from radius import deciding
    keyboard_hider = types.ReplyKeyboardRemove()
    mode = random.randint(0, 10)
    mode = mode % 4
    if (mode == 0):
        s = generate(id, diff)
        bot.send_message(id, s, reply_markup=keyboard_hider)
    if ( mode == 1):
        s = inventing(id, diff)
        bot.send_message(id, 'Is {} prime? True/False'.format(s), reply_markup=keyboard_hider)
    if(mode == 2):
        s = creating(id, diff)
        bot.send_message(id, 'Send multiplication of the roots of {}'.format(s), reply_markup=keyboard_hider)
    if ( mode == 3):
        s = deciding(id, diff)
        bot.send_message(id, s, reply_markup=keyboard_hider)

"""Чел, просто расслабься, будь что будет. Тебе некуда торопиться, у тебя все хорошо.
    Просто сделай отправку всех сообщений отдельно, а чтение отдельно, тогда все будет хорошо."""

@bot.message_handler(func=lambda message: True, content_types=['text'])
def game(message):
    print(message.chat.id)
    print(message.from_user.id)
    ans = getanswer(message.chat.id)
    if not ans:
        bot.send_message(message.chat.id, 'Type /game to start')
        return
    if(str(ans).lower() ==  message.text.lower()):
        incscore(message.chat.id)
        bot.send_message(message.chat.id, message.from_user.first_name + ', Great! Your score now is ' + str(getscore(message.chat.id)) + '.')
    else:
        decscore(message.chat.id)
        bot.send_message(message.chat.id,  message.from_user.first_name + ', Bad! Right answer is ' + str(ans) + ', and your score now is' + str(getscore(message.chat.id)) + '.')
    sendingtas(message.chat.id, getdif(message.chat.id))



if __name__ == '__main__':
    bot.polling(none_stop=True)

