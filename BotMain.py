import telebot

Mybot = telebot.TeleBot('TOKEN')

@Mybot.message_handler(content_types='photo')
def send_photo_reply(message):
    Mybot.send_photo(message.chat_id, message.photo[-1].file_id)

Mybot.polling()