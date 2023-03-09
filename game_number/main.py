import telebot
from telebot import types
import random


token = '6075266239:AAFzRuelyl4jr503H6H5tHXryeGHh1WuOyw'

bot = telebot.TeleBot(token)

keyboard = types.ReplyKeyboardMarkup()
button1 = types.KeyboardButton('Играть')
button2 = types.KeyboardButton('Нет')
keyboard.add(button1,button2)

@bot.message_handler(commands=['start', 'game'])
def start_message(message):
    message2 = bot.send_message(message.chat.id, 'Привет, начнем игру?', reply_markup=keyboard)
    bot.register_next_step_handler(message, check_answer)


def check_answer(message):
    if message.text == 'Играть':
        bot.send_message(message.chat.id, 'Ok тогда вот правила: нужно угадатьчисло от 1 до 10 за 3 попытки')
        number = random.choice(range(1, 11))
        game(message, 3, number)
    else:
        bot.send_message(message.chta.id, 'Хорошо, пока!')

def game(messege, attempts, number):
    message2 = bot.send_message(messege.chat.id, 'Введите число: ')
    bot.register_next_step_handler(message2, check_number, attempts-1, number)

def check_number(message, attempts, number):
    if message.text == str(number):
        bot.send_message(message.chat.id, 'Поздравляю, ты выиграл!!')
    elif attempts == 0:
        bot.send_message(message.chat.id, 'Сoрри у тебя закончились попытки')
        start_message(message)
    else:
        bot.send_message(message.chat.id, f'Не вено, у тебя осталось {attempts} попыток, попробуй ещё раз ввести число')
        game(message,attempts, number)

bot.polling()

# @bot.message_handler(commands=['start'])
# def start_message(message):
#     print('!!!!!!!!')
#     bot.send_message(message.chat.id, 'Bot started')
#     bot.register_next_step_handler(message, answer_text)

# def answer_text(message):#message.text == 'hi!
#     print(message.text, '!!!!!!!!')
#     if message.text.lower() == 'hi!':
#         bot.send_message(message.chat.id, 'привет!')
#     elif message.text.lower() == 'bye!':
#         bot.send_message(message.chat.id, 'пока!!')
#     bot.register_next_step_handler(message, answer_text)

# bot.polling()  

# @bot.message_handler(commands=['start'])
# def john(message):
#     print('!!!!!!!!')
#     bot.send_message(message.chat.id, 'Bведите свое ФИО')
#     bot.register_next_step_handler(message, answer_user)

# def answer_user(message):#message.text == 'hi!
#     print(message.text, '!!!!!!!!')
#     if message.text.lower() == 'hi!':
#         bot.send_message(message.chat.id, f'Здравствуйте {message.text}')
#         bot.send_message(message.chat.id, 'Test bot!')
 

# bot.polling()  