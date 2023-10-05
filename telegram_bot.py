import django
import telebot
from telebot import types
from api.models import TelegramBotToken
from django.conf import settings


os.environ['DJANGO_SETTINGS_MODULE'] = 'telegram_bot_project.settings'
django.setup()

bot = telebot.TeleBot('')

@bot.message_handler(commands=['start'])
def start(message):
    chat_id = message.chat.id
    bot.send_message(chat_id,"Добро пожаловать! Отправьте ваш токен для связи с вашим аккаунтом.")


@bot.message_handler(func=lambda message: not message.text.startswith('/'))
def handle_message(message):
    chat_id = message.chat.id
    text = message.text

    try:
        user_token = TelegramBotToken.objects.get(token=chat_id)
        user_profile = user_token.user
    except TelegramBotToken.DoesNotExist:
        bot.send_message(chat_id, "Ваш аккаунт не связан. Пожалуйста, отправьте свой токен сначала.")
        return

    Message.objects.create(user=user_profile, content=text)
    bot.send_message(chat_id, "Ваше сообщение было отправлено.")


def echo_all(message):
    chat_id = message.chat.id

    try:
        token = TelegramBotToken.objects.get(token=chat_id)
        user_profile = token.user
        bot.send_message(chat_id, f"{user_profile.username}, я получил от тебя сообщение:\n{message.text}")
    except TelegramBotToken.DoesNotExist:
        bot.send_message(chat_id, "Ваш аккаунт не связан. Пожалуйста, отправьте свой токен сначала.")


bot.polling(none_stop=True, interval=0)


