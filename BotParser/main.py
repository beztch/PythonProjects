from src.parser import Parser
from src.help import Help
from src.error import Error
from src.bot import bot
import random

@bot.message_handler(content_types=['text'])
def cashier(message):
    """distributes by function in case what user send
    Args:
        message (class 'telebot.types.Message'): message from user.
    Returns:
        None.
    """
    print(type(message))
    text = message.text
    if (text.isdigit()):
        film, img = Parser(int(text))
        bot.send_message(message.chat.id, text=str(film))
        if (film == "Такого номера у нас в рейтинге нет("):
            img = open('images/sad_' + str(random.randint(1, 5)) + '.jpg', 'rb')
        bot.send_photo(message.chat.id, img)
    elif (text == "все" or text == "Все"):
        film, img = Parser(1)
        i = 2
        while film != "Такого номера у нас в рейтинге нет(":
            bot.send_message(message.chat.id, text=str(film))
            bot.send_photo(message.chat.id, img)
            film, img = Parser(i)
            i += 1
    elif (text == "/help"):
        Help(message)
    else:
        Error(message)

bot.polling(none_stop=True)
