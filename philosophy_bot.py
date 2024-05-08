#Это телеграм-бот-философ

import telebot

# Замените 'YOUR_BOT_TOKEN_HERE' на токен вашего бота
TOKEN = '6653567814:AAGHDgkOxzdKd30Echewz3OuYL-Z19jInjo'
bot = telebot.TeleBot(TOKEN)


# Обработка команды /start
@bot.message_handler(commands=['start'])
def send_welcome(message):
  bot.reply_to(
      message,
      "Привет! Я философский бот. Спроси меня о смысле жизни, происхождении вселенной или законах мира."
  )


# Обработка текстовых сообщений
@bot.message_handler(func=lambda message: True)
def echo_all(message):
  text = message.text.lower()
  if 'смысл жизни' in text:
    bot.reply_to(message, "Смысл жизни - 42.")
  elif 'происхождение вселенной' in text:
    bot.reply_to(
        message,
        "Вселенная возникла в результате Большого Взрыва около 13.8 миллиардов лет назад."
    )
  elif 'законы мира' in text:
    bot.reply_to(
        message,
        "Законы мира управляются физическими законами, которые мы все еще пытаемся полностью понять."
    )
  else:
    bot.reply_to(
        message,
        "Это довольно глубокий вопрос. Давай обсудим что-нибудь полегче.")


# Запуск бота
bot.polling()
