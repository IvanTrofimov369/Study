import telebot
bot = telebot.TeleBot("5512086789:AAHl0o7Huhh7NRo5oajlYMyTjodUvO1n-xY")
@bot.message_handler(commands=["start"])
def start(m, res=False):
    bot.send_message(m.chat.id, 'Я на связи, Напиши мне')
@bot.message_handler(content_types=["text"])
def handle_text(message):
    bot.send_message(message.chat.id, 'Вы написали: ' + message.text)
bot.polling(none_stop=True, interval=0)