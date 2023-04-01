import telebot
from config import TOKEN, admin_id
from telebot import types

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    kb = types.InlineKeyboardMarkup(row_width=2)
    btn = types.InlineKeyboardButton(text='Роллы', callback_data='btn1')
    btn1 = types.InlineKeyboardButton(text='Суши', callback_data='btn2')
    kb.add(btn, btn1)
    bot.send_message(message.chat.id, 'приветик', reply_markup=kb)

@bot.callback_query_handler(func=lambda callback: callback.data)
def check_callback_data(callback):
    if callback.data == 'btn1':
        kb = types.InlineKeyboardMarkup(row_width=2)
        btn = types.InlineKeyboardButton(text='Роллы', callback_data='btn1')
        btn1 = types.InlineKeyboardButton(text='Суши', callback_data='btn2')
        kb.add(btn, btn1)
        bot.edit_message_text(chat_id=callback.message.chat.id, message_id=callback.message.id,
                         text='Роллы\n<b>ФИЛАДЕЛЬФИЯ</b>\n<i>лососьб сырб огурец</i>\nCnjbvjcnm:100', parse_mode='HTML', reply_markup=kb)
        # bot.send_message(admin_id, callback.message.text)

bot.polling()