from config import TOKEN
from telegram.ext import Application, CommandHandler, MessageHandler, ConversationHandler, filters, CallbackQueryHandler
from telegram import ReplyKeyboardMarkup, InlineKeyboardMarkup, InlineKeyboardButton
from db import Database
import logging
import random

data = Database('game.db')

# Запускаем логгирование
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.DEBUG
)

logger = logging.getLogger(__name__)



async def start(update, context):
    keyboard = [[InlineKeyboardButton('Вход', callback_data='catalog')],
                [InlineKeyboardButton('Инструкция', callback_data='instruction'),
                 InlineKeyboardButton('О боте', callback_data='about')]]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text("Привет. Я твой бот-помощник.\nВыбери кнопку", reply_markup=reply_markup)
    return 1

async def catalog(update, context):
    query = update.callback_query
    await query.answer()
    keyboard = [[InlineKeyboardButton('Биология', callback_data='biology'),
                 InlineKeyboardButton('История', callback_data='history')]]
    markup = InlineKeyboardMarkup(keyboard)
    await query.edit_message_text("Теперь ты можешь выбрать нужную тебе категорию:", reply_markup=markup)
    return 2

async def replic(update, context):
    query = update.callback_query
    await query.answer()
    keyboard = [[InlineKeyboardButton('Вернуться в меню', callback_data='catalog')],
                [InlineKeyboardButton('Инструкция', callback_data='instruction')]]
    markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text('Извините, но я вас не понял. Попробуйте ещё раз.', reply_markup=markup)
    return 1

ANSWER = ''

async def biology(update, context):
    query = update.callback_query
    await query.answer()
    question = data.biology_questions()
    global ANSWER
    ANSWER = data.biology_answers(question)
    ansbutton = InlineKeyboardButton(ANSWER, callback_data='answer')
    button = InlineKeyboardButton('Неверно', callback_data='disanswer')
    ins = InlineKeyboardButton('Инструкция', callback_data='instruction')
    back = InlineKeyboardButton('Веруться в меню', callback_data='catalog')
    rand = random.choice([1, 2])
    if rand == 1:
        markup = InlineKeyboardMarkup([[ansbutton, button], [ins, back]])
        await query.edit_message_text(f'Вопроc: {question}', reply_markup=markup)
        return 3
    markup = InlineKeyboardMarkup([[button, ansbutton], [ins, back]])
    await query.edit_message_text(f'Вопроc: {question}', reply_markup=markup)
    return 4

async def biology_answers(update, context):
    query = update.callback_query
    await query.answer()
    keyboard = [[InlineKeyboardButton('Продолжить', callback_data='biology'),
                 InlineKeyboardButton('Вернуться в меню', callback_data='catalog')],
                [InlineKeyboardButton('Инструкция', callback_data='instruction')]]
    markup = InlineKeyboardMarkup(keyboard)
    if update.callback_query.data == 'answer':
        await query.edit_message_text(f'Верно!', reply_markup=markup)
    else:
        await query.edit_message_text(f'Правильный ответ: {ANSWER}', reply_markup=markup)
    return 5

async def history(update, context):
    query = update.callback_query
    await query.answer()
    question = data.history_questions()
    global ANSWER
    ANSWER = data.history_answers(question)
    ansbutton = InlineKeyboardButton(ANSWER, callback_data='answer')
    button = InlineKeyboardButton('Неверно', callback_data='disanswer')
    ins = InlineKeyboardButton('Инструкция', callback_data='instruction')
    back = InlineKeyboardButton('Вернуться в меню', callback_data='catalog')
    rand = random.choice([1, 2])
    if rand == 1:
        markup = InlineKeyboardMarkup([[ansbutton, button], [ins, back]])
        await query.edit_message_text(f'Вопроc: {question}', reply_markup=markup)
        return 6
    markup = InlineKeyboardMarkup([[button, ansbutton], [ins, back]])
    await query.edit_message_text(f'Вопроc: {question}', reply_markup=markup)
    return 7

async def history_answers(update, context):
    query = update.callback_query
    await query.answer()
    keyboard = [[InlineKeyboardButton('Продолжить', callback_data='history'),
                 InlineKeyboardButton('Вернуться в меню', callback_data='catalog')],
                [InlineKeyboardButton('Инструкция', callback_data='instruction')]]
    markup = InlineKeyboardMarkup(keyboard)
    if update.callback_query.data == 'answer':
        await query.edit_message_text(f'Верно!', reply_markup=markup)
    else:
        await query.edit_message_text(f'Правильный ответ: {ANSWER}', reply_markup=markup)
    return 8

async def instruction(update, context):
    query = update.callback_query
    await query.answer()
    keyboard = [[InlineKeyboardButton('Вернуться в меню', callback_data='catalog')],
                [InlineKeyboardButton('О боте', callback_data='about')]]
    markup = InlineKeyboardMarkup(keyboard)
    await query.edit_message_text("1. Просто жми на нужные кнопки.\n"
    "2. Если вы выбрали категорию 'Биология', то пиши слова или словосочетания без точек на конце.\n"
    "3. Если ты выбрал категорию 'История', то пиши дату или даты(через дифиз) без точек.", reply_markup=markup)
    return 9  # Константа, означающая конец диалога.
    # Все обработчики из states и fallbacks становятся неактивными.

async def about(update, context):
    query = update.callback_query
    await query.answer()
    keyboard = [[InlineKeyboardButton('Вернуться в меню', callback_data='catalog')],
                [InlineKeyboardButton('Инструкция', callback_data='instruction')]]
    markup = InlineKeyboardMarkup(keyboard)
    await query.edit_message_text("Данный бот придуман для повышения знаний детей и взрослых.\n"
                                    "Надеемся мы помогли усвоить вам чуть больше школьной программы",
                                  reply_markup=markup)
    return 10

def main():
    app = Application.builder().token(TOKEN).build()

    conv_handler = ConversationHandler(
        # Точка входа в диалог.
        # В данном случае — команда /start. Она задаёт первый вопрос.
        entry_points=[CommandHandler('start', start)],

        # Состояние внутри диалога.
        # Вариант с двумя обработчиками, фильтрующими текстовые сообщения.
        states={
            # Функция читает ответ на первый вопрос и задаёт второй.
            1: [
                CallbackQueryHandler(catalog, pattern="^" + 'catalog' + "$"),
                CallbackQueryHandler(instruction, pattern="^" + 'instruction' + "$"),
                CallbackQueryHandler(about, pattern="^" + 'about' + "$"),
                ],
            2: [
                CallbackQueryHandler(biology, pattern="^" + 'biology' + "$"),
                CallbackQueryHandler(history, pattern="^" + 'history' + "$"),
                ],
            3: [
                CallbackQueryHandler(biology_answers, pattern="^" + 'answer' + "$"),
                CallbackQueryHandler(biology_answers, pattern="^" + 'disanswer' + "$"),
                CallbackQueryHandler(instruction, pattern="^" + 'instruction' + "$"),
                CallbackQueryHandler(catalog, pattern="^" + 'catalog' + "$"),
                ],
            4: [
                CallbackQueryHandler(biology_answers, pattern="^" + 'disanswer' + "$"),
                CallbackQueryHandler(biology_answers, pattern="^" + 'answer' + "$"),
                CallbackQueryHandler(instruction, pattern="^" + 'instruction' + "$"),
                CallbackQueryHandler(catalog, pattern="^" + 'catalog' + "$"),
                ],
            5: [
                CallbackQueryHandler(biology, pattern="^" + 'biology' + "$"),
                CallbackQueryHandler(catalog, pattern="^" + 'catalog' + "$"),
                CallbackQueryHandler(instruction, pattern="^" + 'instruction' + "$"),
                ],
            6: [
                CallbackQueryHandler(history_answers, pattern="^" + 'disanswer' + "$"),
                CallbackQueryHandler(history_answers, pattern="^" + 'answer' + "$"),
                CallbackQueryHandler(instruction, pattern="^" + 'instruction' + "$"),
                CallbackQueryHandler(catalog, pattern="^" + 'catalog' + "$"),
                ],
            7: [
                CallbackQueryHandler(history_answers, pattern="^" + 'answer' + "$"),
                CallbackQueryHandler(history_answers, pattern="^" + 'disanswer' + "$"),
                CallbackQueryHandler(instruction, pattern="^" + 'instruction' + "$"),
                CallbackQueryHandler(catalog, pattern="^" + 'catalog' + "$"),
                ],
            8: [
                CallbackQueryHandler(history, pattern="^" + 'history' + "$"),
                CallbackQueryHandler(catalog, pattern="^" + 'catalog' + "$"),
                CallbackQueryHandler(instruction, pattern="^" + 'instruction' + "$"),
                ],
            9: [
                CallbackQueryHandler(catalog, pattern="^" + 'catalog' + "$"),
                CallbackQueryHandler(about, pattern="^" + 'about' + "$"),
                ],
            10: [
                CallbackQueryHandler(catalog, pattern="^" + 'catalog' + "$"),
                CallbackQueryHandler(instruction, pattern="^" + 'instruction' + "$"),
                ]
        },

        # Точка прерывания диалога. В данном случае — команда /stop.
        fallbacks=[CommandHandler('start', start)]
    )
    app.add_handler(conv_handler)
    app.run_polling()

if __name__ == '__main__':
    main()