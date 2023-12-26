from .bot import bot

def Help(message):
    """sends help message
    Args:
        message (class 'telebot.types.Message'): message from user.
    Returns:
        None.
    """
    bot.send_message(message.chat.id, "Я умею выводить топ самых ожидаемых фильмов по мнению Кинопоиска")
    bot.send_message(message.chat.id, "просто напиши любую цифру или <<все>>, если интересует весь рейтинг")
    bot.send_message(message.chat.id, "если фильм с таким номером есть в списке, я его покажу")
    return