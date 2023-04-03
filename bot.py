# import telebot
# from config import TOKEN, admin_id
# from telebot import types
#
# bot = telebot.TeleBot(TOKEN)
#
# @bot.message_handler(commands=['start'])
# def start(message):
#     foto1 = open('gameover.png', 'rb')
#     kb = types.InlineKeyboardMarkup(row_width=2)
#     btn = types.InlineKeyboardButton(text='Роллы', callback_data='btn1')
#     btn1 = types.InlineKeyboardButton(text='Суши', callback_data='btn2')
#     kb.add(btn, btn1)
#     bot.send_photo(message.chat.id, foto1, 'приветик', reply_markup=kb)
#
# @bot.callback_query_handler(func=lambda callback: callback.data)
# def check_callback_data(callback):
#     if callback.data == 'btn1':
#         file = open('gameover.png', 'rb')
#         kb = types.InlineKeyboardMarkup(row_width=2)
#         btn = types.InlineKeyboardButton(text='<|', callback_data='btn1')
#         btn1 = types.InlineKeyboardButton(text='|>', callback_data='btn2')
#         btn2 = types.InlineKeyboardButton(text='корзина', callback_data='btn3')
#         btn3 = types.InlineKeyboardButton(text='добавить в корзину', callback_data='btn4')
#         btn4 = types.InlineKeyboardButton(text='меню', callback_data='btn5')
#         kb.add(btn, btn1)
#         bot.edit_message_media(media=telebot.types.InputMedia(type='photo', media=file, caption='Роллы\n<b>ФИЛАДЕЛЬФИЯ</b>\n<i>лососьб сырб огурец</i>\nCnjbvjcnm:100', parse_mode='HTML'), chat_id=callback.message.chat.id, message_id=callback.message.id, reply_markup=kb)
#         # bot.send_message(admin_id, callback.message.text)
#
# @bot.callback_query_handler(func=lambda callback: callback.data)
# def check_callback_data(callback):
#     if callback.data == 'btn1':
#         file = open('gameover.png', 'rb')
#         kb = types.InlineKeyboardMarkup(row_width=2)
#         btn = types.InlineKeyboardButton(text='<|', callback_data='btn1')
#         btn1 = types.InlineKeyboardButton(text='|>', callback_data='btn2')
#         btn2 = types.InlineKeyboardButton(text='корзина', callback_data='btn3')
#         btn3 = types.InlineKeyboardButton(text='добавить в корзину', callback_data='btn4')
#         btn4 = types.InlineKeyboardButton(text='меню', callback_data='btn5')
#         kb.add(btn, btn1)
#         bot.edit_message_media(media=telebot.types.InputMedia(type='photo', media=file, caption='Роллы\n<b>ФИЛАДЕЛЬФИЯ</b>\n<i>лососьб сырб огурец</i>\nCnjbvjcnm:100', parse_mode='HTML'), chat_id=callback.message.chat.id, message_id=callback.message.id, reply_markup=kb)
#
# bot.polling()import telebot
# from config import TOKEN, admin_id
# from telebot import types
#
# bot = telebot.TeleBot(TOKEN)
#
# @bot.message_handler(commands=['start'])
# def start(message):
#     foto1 = open('gameover.png', 'rb')
#     kb = types.InlineKeyboardMarkup(row_width=2)
#     btn = types.InlineKeyboardButton(text='Роллы', callback_data='btn1')
#     btn1 = types.InlineKeyboardButton(text='Суши', callback_data='btn2')
#     kb.add(btn, btn1)
#     bot.send_photo(message.chat.id, foto1, 'приветик', reply_markup=kb)
#
# @bot.callback_query_handler(func=lambda callback: callback.data)
# def check_callback_data(callback):
#     if callback.data == 'btn1':
#         file = open('gameover.png', 'rb')
#         kb = types.InlineKeyboardMarkup(row_width=2)
#         btn = types.InlineKeyboardButton(text='<|', callback_data='btn1')
#         btn1 = types.InlineKeyboardButton(text='|>', callback_data='btn2')
#         btn2 = types.InlineKeyboardButton(text='корзина', callback_data='btn3')
#         btn3 = types.InlineKeyboardButton(text='добавить в корзину', callback_data='btn4')
#         btn4 = types.InlineKeyboardButton(text='меню', callback_data='btn5')
#         kb.add(btn, btn1)
#         bot.edit_message_media(media=telebot.types.InputMedia(type='photo', media=file, caption='Роллы\n<b>ФИЛАДЕЛЬФИЯ</b>\n<i>лососьб сырб огурец</i>\nCnjbvjcnm:100', parse_mode='HTML'), chat_id=callback.message.chat.id, message_id=callback.message.id, reply_markup=kb)
#         # bot.send_message(admin_id, callback.message.text)
#
# @bot.callback_query_handler(func=lambda callback: callback.data)
# def check_callback_data(callback):
#     if callback.data == 'btn1':
#         file = open('gameover.png', 'rb')
#         kb = types.InlineKeyboardMarkup(row_width=2)
#         btn = types.InlineKeyboardButton(text='<|', callback_data='btn1')
#         btn1 = types.InlineKeyboardButton(text='|>', callback_data='btn2')
#         btn2 = types.InlineKeyboardButton(text='корзина', callback_data='btn3')
#         btn3 = types.InlineKeyboardButton(text='добавить в корзину', callback_data='btn4')
#         btn4 = types.InlineKeyboardButton(text='меню', callback_data='btn5')
#         kb.add(btn, btn1)
#         bot.edit_message_media(media=telebot.types.InputMedia(type='photo', media=file, caption='Роллы\n<b>ФИЛАДЕЛЬФИЯ</b>\n<i>лососьб сырб огурец</i>\nCnjbvjcnm:100', parse_mode='HTML'), chat_id=callback.message.chat.id, message_id=callback.message.id, reply_markup=kb)
#
# bot.polling()