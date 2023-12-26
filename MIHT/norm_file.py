import telebot
import random
import time
from data import database

def Help(message):
    bot.send_message(message.chat.id, "Я умею гадать на любовь, карьеру, отношения....")
    bot.send_message(message.chat.id, "для того, чтобы я это сделал отправь одно из следующий сообщений (пока я не умею отправлять кнопки):")
    bot.send_message(message.chat.id, "на отношение человека к вам")
    bot.send_message(message.chat.id, "на карьеру")
    bot.send_message(message.chat.id, "на ситуацию")
    bot.send_message(message.chat.id, "на любовь")
    bot.send_message(message.chat.id, "карта дня")
    return

def ForPerson(message):
    bot.send_message(message.chat.id, "Задумайте конкретного человека, про которого хотите узнать.")
    time.sleep(5)
    card = []
    card.append(random.randint(0, 77))
    card_x = random.randint(0, 77)
    for i in range(2):
        while (card_x in card):
            card_x = random.randint(0, 77)
        card.append(card_x)
    bot.send_photo(message.chat.id, open('images/c_' + str(card[0]) + '.jpeg', 'rb'))
    bot.send_message(message.chat.id, text="Общее впечатление: " + f"{database[card[0]][1]}")
    bot.send_photo(message.chat.id, open('images/c_' + str(card[1]) + '.jpeg', 'rb'))
    bot.send_message(message.chat.id, text="Чувства, которые испытывает человек: " + f"{database[card[1]][1]}")
    bot.send_photo(message.chat.id, open('images/c_' + str(card[2]) + '.jpeg', 'rb'))
    bot.send_message(message.chat.id, text="Подсознательное восприятие: " + f"{database[card[2]][1]}")
    bot.register_next_step_handler(message, str(a))
    bot.send_message(message.chat.id, text=a)
    return

def Career(message):
    bot.send_message(message.chat.id, "Задумайте конкретное занятие или дело, которое вас интересует.")
    time.sleep(5)
    card = []
    card.append(random.randint(0, 77))
    card_x = random.randint(0, 77)
    for i in range(5):
        while (card_x in card):
            card_x = random.randint(0, 77)
        card.append(card_x)
    bot.send_photo(message.chat.id, open('images/c_' + str(card[0]) + '.jpeg', 'rb'))
    bot.send_message(message.chat.id, text="Что вы хотите получить от работы прямо сейчас: " + f"{database[card[0]][2]}")
    bot.send_photo(message.chat.id, open('images/c_' + str(card[1]) + '.jpeg', 'rb'))
    bot.send_message(message.chat.id, text="Что или кто мешает вам: " + f"{database[card[1]][2]}")
    bot.send_photo(message.chat.id, open('images/c_' + str(card[2]) + '.jpeg', 'rb'))
    bot.send_message(message.chat.id, text="Что тянет вас назад: " + f"{database[card[2]][2]}")
    bot.send_photo(message.chat.id, open('images/c_' + str(card[3]) + '.jpeg', 'rb'))
    bot.send_message(message.chat.id, text="Что толкает вас вперед: " + f"{database[card[3]][2]}")
    bot.send_photo(message.chat.id, open('images/c_' + str(card[4]) + '.jpeg', 'rb'))
    bot.send_message(message.chat.id, text="Что вы можете получить от этой работы: " + f"{database[card[4]][2]}")
    bot.send_photo(message.chat.id, open('images/c_' + str(card[5]) + '.jpeg', 'rb'))
    bot.send_message(message.chat.id, text="Основополагающие факторы: " + f"{database[card[5]][2]}")
    return

def Situation(message):
    bot.send_message(message.chat.id, "Задумайте вопрос в формате <<что будет в/от/на...>>")
    time.sleep(5)
    card = []
    card.append(random.randint(0, 77))
    card_x = random.randint(0, 77)
    for i in range(3):
        while (card_x in card):
            card_x = random.randint(0, 77)
        card.append(card_x)
    bot.send_photo(message.chat.id, open('images/c_' + str(card[0]) + '.jpeg', 'rb'))
    bot.send_message(message.chat.id, text="Cуть проблемы: " + f"{database[card[0]][3]}")
    bot.send_photo(message.chat.id, open('images/c_' + str(card[1]) + '.jpeg', 'rb'))
    bot.send_message(message.chat.id, text="Что делать не стоит: " + f"{database[card[1]][3]}")
    bot.send_photo(message.chat.id, open('images/c_' + str(card[2]) + '.jpeg', 'rb'))
    bot.send_message(message.chat.id, text="Совет, к которому стоит прислушаться: " + f"{database[card[2]][3]}")
    bot.send_photo(message.chat.id, open('images/c_' + str(card[3]) + '.jpeg', 'rb'))
    bot.send_message(message.chat.id, text="Исход, если последовать советам: " + f"{database[card[3]][3]}")
    return

def Love(message):
    bot.send_message(message.chat.id, "на любовь...")
    time.sleep(5)
    card = []
    card.append(random.randint(0, 77))
    card_x = random.randint(0, 77)
    for i in range(6):
        while (card_x in card):
            card_x = random.randint(0, 77)
        card.append(card_x)
    bot.send_photo(message.chat.id, open('images/c_' + str(card[0]) + '.jpeg', 'rb'))
    bot.send_message(message.chat.id, text="Карта прошлого (что было): " + f"{database[card[0]][1]}")
    bot.send_photo(message.chat.id, open('images/c_' + str(card[1]) + '.jpeg', 'rb'))
    bot.send_message(message.chat.id, text="Карта настоящего (что есть): " + f"{database[card[1]][1]}")
    bot.send_photo(message.chat.id, open('images/c_' + str(card[2]) + '.jpeg', 'rb'))
    bot.send_message(message.chat.id, text="Что на сердце: " + f"{database[card[2]][1]}")
    bot.send_photo(message.chat.id, open('images/c_' + str(card[3]) + '.jpeg', 'rb'))
    bot.send_message(message.chat.id, text="Какие мысли в голове: " + f"{database[card[3]][1]}")
    bot.send_photo(message.chat.id, open('images/c_' + str(card[4]) + '.jpeg', 'rb'))
    bot.send_message(message.chat.id, text="Что помогает: " + f"{database[card[4]][1]}")
    bot.send_photo(message.chat.id, open('images/c_' + str(card[5]) + '.jpeg', 'rb'))
    bot.send_message(message.chat.id, text="Что препятствует: " + f"{database[card[5]][1]}")
    bot.send_photo(message.chat.id, open('images/c_' + str(card[6]) + '.jpeg', 'rb'))
    bot.send_message(message.chat.id, text="Карта будущего (что будет): " + f"{database[card[6]][1]}")
    return

def CardOfTheDay(message):
    bot.send_message(message.chat.id, "ваша карта дня")
    card = random.randint(0, 77)
    bot.send_message(message.chat.id, text=f"{database[card][0]}")
    bot.send_photo(message.chat.id, open('images/c_' + str(card) + '.jpeg', 'rb'))
    bot.send_message(message.chat.id, text=f"{database[card][3]}")
    return

def Error(message):
    bot.send_message(message.chat.id, "у нас нет такой команды:(")
    bot.send_message(message.chat.id, "если не знаешь, что делать, напиши /help")
    return


TOKEN = "6272412631:AAGU_a4ku3WGLRje_Tl9Qnm13lgZfGynkBs"
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(content_types=['text'])
def cashier(message):
    text = message.text
    if (text == "/help"):
        Help(message)
    elif (text == "на отношение человека к вам"):
        ForPerson(message)
    elif (text == "на карьеру"):
        Career(message)
    elif (text == "на ситуацию"):
        Situation(message)
    elif (text == "на любовь"):
        Love(message)
    elif (text == "карта дня"):
        CardOfTheDay(message)
    else:
        Error(message)

bot.polling(none_stop=True)
