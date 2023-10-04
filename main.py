import telebot
import datetime
import os

import HomeWorks
from BotFunc import *
import HomeWorks as hm
from CalcDeter import CalcDeter
import FizLab
import dt

deltaweek = -5          #-5 это разница между учебными неделями и календарными
time = datetime.datetime.now()
week,weekday = time.isocalendar().week-deltaweek,time.isocalendar().weekday
time = (time.hour, time.minute)

bot = telebot.TeleBot('6099652584:AAE5tCtp0cYSO-aLqrcbY0kBOOyIuCnAZNw')

Commands=[]


@bot.message_handler(commands=['start'])
def start(message):
    try:
        os.mkdir('chats/'+str(message.chat.id))
        bot.send_message(message.chat.id,'Создана папка)', message_thread_id=message.message_thread_id, reply_to_message_id=message.id)
    except Exception as err:
        print(err,message.text)
        bot.send_message(message.chat.id, err, message_thread_id=message.message_thread_id,
                         reply_to_message_id=message.id)


@bot.message_handler(commands=['info'])
def start(message):
    bot.send_message(message.chat.id,'пошел нахуй, я спать', message_thread_id=message.message_thread_id, reply_to_message_id=message.id)

@bot.message_handler(commands=['UPD'])
def start(message):
    t=str(message.text).split(' ')
    bot.send_message(message.chat.id,'Обновление...', message_thread_id=message.message_thread_id, reply_to_message_id=message.id)
    try:
        dt.UPD(t[1],t[2],str(message.chat.id))
        bot.send_message(message.chat.id, 'Готово', message_thread_id=message.message_thread_id,
                         reply_to_message_id=message.id)
    except Exception as err:
        print(str(err)+str(message.text))
        bot.send_message(message.chat.id, 'Ошибка', message_thread_id=message.message_thread_id,
                         reply_to_message_id=message.id)


@bot.message_handler(commands=['talk'])
def start(message):
    bot.send_message(message.chat.id,'СПАСИБО', message_thread_id=message.message_thread_id) #, reply_to_message_id=message.id

@bot.message_handler(commands=['DevFullList'])
def start(message):
    for q in CreateFullList(str(message.chat.id)):
        bot.send_message(message.chat.id, str(q), message_thread_id=message.message_thread_id)

@bot.message_handler(commands=['day', 'день'])
def start(message):
    try:
        t=str(message.text).split(' ')
        bot.send_message(message.chat.id, StrFromDL(CreateDayList(t[1],t[2],str(message.chat.id))), message_thread_id=message.message_thread_id)
    except Exception as err:
        print(str(err)+'\n'+str(message.text)+'\n')
        bot.send_message(message.chat.id, err, message_thread_id=message.message_thread_id,
                         reply_to_message_id=message.id)

@bot.message_handler(commands=['today', 'сегодня'])
def start(message):
    try:
        bot.send_message(message.chat.id, StrFromDL(CreateDayList(week,weekday,str(message.chat.id))), message_thread_id=message.message_thread_id)
    except Exception as err:
        print(str(err)+'\n'+str(message.text)+'\n')
        bot.send_message(message.chat.id, err, message_thread_id=message.message_thread_id,
                         reply_to_message_id=message.id)

@bot.message_handler(commands=['tomorrow', 'завтра'])
def start(message):
    try:
        bot.send_message(message.chat.id, StrFromDL(CreateDayList(week+(weekday+1)//7,(weekday+1)%7,str(message.chat.id))), message_thread_id=message.message_thread_id)
    except Exception as err:
        print(str(err)+'\n'+str(message.text)+'\n')
        bot.send_message(message.chat.id, err, message_thread_id=message.message_thread_id,
                         reply_to_message_id=message.id)

@bot.message_handler(commands=['the_day_after_tomorrow', 'послезавтра'])
def start(message):
    try:
        bot.send_message(message.chat.id, StrFromDL(CreateDayList(week+(weekday+2)//7,(weekday+2)%7,str(message.chat.id))), message_thread_id=message.message_thread_id)
    except Exception as err:
        print(str(err)+'\n'+str(message.text)+'\n')
        bot.send_message(message.chat.id, err, message_thread_id=message.message_thread_id,
                         reply_to_message_id=message.id)

@bot.message_handler(commands=['dev'])
def start(message):
    print(message)

@bot.message_handler(commands=['ping'])
def start(message):
    try:
        bot.send_message(message.chat.id, '@'+message.from_user.username, message_thread_id=message.message_thread_id, reply_to_message_id=message.id)
    except Exception as err:
        print(str(err)+'\n'+str(message.text)+'\n')
        bot.send_message(message.chat.id, err, message_thread_id=message.message_thread_id,
                         reply_to_message_id=message.id)

@bot.message_handler(commands=['sub'])
def start(message):
    try:
        if message.chat.id == -1001663977041:
            bot.send_message(message.chat.id,'Спасибо за подписку', message_thread_id=message.message_thread_id, reply_to_message_id=message.id)
            NewSub(message.from_user.username)
        else:
            bot.send_message(message.chat.id,'Не доступно в вашем чате(', message_thread_id=message.message_thread_id, reply_to_message_id=message.id)
    except Exception as err:
        print(str(err)+'\n'+str(message.text)+'\n')
        bot.send_message(message.chat.id, err, message_thread_id=message.message_thread_id,
                         reply_to_message_id=message.id)

@bot.message_handler(commands=['sub'])
def start(message):
    try:
        if message.chat.id == -1001663977041:
            bot.send_message(message.chat.id,'Спасибо за подписку', message_thread_id=message.message_thread_id, reply_to_message_id=message.id)
            NewSub(message.from_user.username)
        else:
            bot.send_message(message.chat.id,'Не доступно в вашем чате(', message_thread_id=message.message_thread_id, reply_to_message_id=message.id)
    except Exception as err:
        print(str(err)+'\n'+str(message.text)+'\n')
        bot.send_message(message.chat.id, err, message_thread_id=message.message_thread_id,
                         reply_to_message_id=message.id)

@bot.message_handler(commands=['hm1.1.2'])
def start(message):
    try:
        t=message.text.split(' ')
        s=''
        for q in hm.HomeWork_1d1d2(t[1],t[2],t[3],t[4],t[5]):
            s+='\n'+ListToStr(q).replace('set()','{∅}')
        bot.send_message(message.chat.id, s, message_thread_id=message.message_thread_id,
                             reply_to_message_id=message.id)
    except Exception as err:
        print(str(err)+'\n'+str(message.text)+'\n')
        bot.send_message(message.chat.id, err, message_thread_id=message.message_thread_id,
                         reply_to_message_id=message.id)

@bot.message_handler(commands=['hm1.2.2'])
def start(message):
    try:
        t=message.text.split(' ')[1]
        bot.send_message(message.chat.id, HomeWorks.HomeWork_1d2d2(t), message_thread_id=message.message_thread_id,
                             reply_to_message_id=message.id)
    except Exception as err:
        print(str(err)+'\n'+str(message.text)+'\n')
        bot.send_message(message.chat.id, err, message_thread_id=message.message_thread_id,
                         reply_to_message_id=message.id)

@bot.message_handler(commands=['опр'])
def start(message):
    try:
        t=message.text.split('\n')
        L=[]
        for q in t:
            if q[1]!='о':
                L.append(list(map(int, q.split(' '))))
        bot.send_message(message.chat.id, CalcDeter(L), message_thread_id=message.message_thread_id, reply_to_message_id=message.id)
    except:
        bot.send_message(message.chat.id, 'imbisil syntax', message_thread_id=message.message_thread_id,
                         reply_to_message_id=message.id)

@bot.message_handler(commands=['FixLab2d07'])
def start(message):
    try:
        t=message.text.split(' ')
        L=t[1:]
        tga,B=FizLab.LabS2d07(L[0], L[1], L[2])
        bot.send_message(message.chat.id, 'tg(a)= '+str(tga[0])+', '+str(tga[1])+'\nB= '+str(B[0])+', '+str(B[1]), message_thread_id=message.message_thread_id, reply_to_message_id=message.id)
    except:
        bot.send_message(message.chat.id, 'imbisil syntax', message_thread_id=message.message_thread_id,
                         reply_to_message_id=message.id)


bot.polling(none_stop=True)