from .bot import bot

def Error(message):
    """sends an error message
    Args:
        message (class 'telebot.types.Message'): message from user.
    Returns:
        None.
    """
    bot.send_message(message.chat.id, "у нас нет такой команды:(")
    bot.send_message(message.chat.id, "если не знаешь, что делать, напиши /help")
    return