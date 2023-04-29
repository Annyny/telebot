from config import TOKEN
from telegram.ext import Application, CommandHandler, MessageHandler, ConversationHandler, filters, CallbackQueryHandler
from telegram import ReplyKeyboardMarkup, InlineKeyboardMarkup, InlineKeyboardButton
from db import Database
import logging

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
    global ANSWER
    ANSWER = ''
    keyboard = [[InlineKeyboardButton('Биология', callback_data='biology'),
                 InlineKeyboardButton('История', callback_data='history')],
                [InlineKeyboardButton('Инструкция', callback_data='help')]]
    markup = InlineKeyboardMarkup(keyboard)
    await query.edit_message_text("Теперь ты можешь выбрать нужную тебе категорию:", reply_markup=markup)
    return 2

async def replic(update, context):
    await update.message.reply_text('Извините, но я вас не понял. Попробуйте ещё раз.')
    return 1

ANSWER = ''

async def biology(update, context):
    query = update.callback_query
    await query.answer()
    global ANSWER
    question = data.biology_questions()
    ANSWER = data.biology_answers(question)
    await query.edit_message_text(f'Вопроc: {question}')
    return 4

async def biology_second(update, context):
    # keyboard = [[InlineKeyboardButton('Продолжить', callback_data='biology'),
    #              InlineKeyboardButton('Вернуться к каталогу', callback_data='catalog')],
    #             [InlineKeyboardButton('Инструкция', callback_data='help')]]
    #
    global ANSWER
    question = data.biology_questions()
    ANSWER = data.biology_answers(question)
    await update.message.reply_text(f'Вопроc: {question}')


async def biology_answers(update, context):
    # keyboard = [[InlineKeyboardButton('Продолжить', callback_data='biology'),
    #              InlineKeyboardButton('Вернуться к каталогу', callback_data='catalog')],
    #             [InlineKeyboardButton('Инструкция', callback_data='help')]]
    #
    if update.message.text == ANSWER:
        await update.message.reply_text(f'Верно!')
        return 5
    await update.message.reply_text(f'Правильный ответ: {ANSWER}')
    return 5

async def history(update, context):
    print(2343545)
    global ANSWER
    print(54654656)
    question = data.history_questions()
    ANSWER = data.history_answers(question)
    await update.message.reply_text(f'Вопроc: {question}')
    return 7

async def history_answers(update, context):
    if update.message.text == ANSWER:
        await update.message.reply_text(f'Верно!')
        return 3
    await update.message.reply_text(f'Попробуй ещё раз')
    return 5


async def instruction(update, context):
    # Ответ на второй вопрос.
    # Мы можем его сохранить в базе данных или переслать куда-либо.
    weather = update.message.text
    logger.info(weather)
    await update.message.reply_text("Спасибо за участие в опросе! Всего доброго!")
    return ConversationHandler.END  # Константа, означающая конец диалога.
    # Все обработчики из states и fallbacks становятся неактивными.

async def back(update, context):
    await update.message.reply_text("Всего доброго!")
    return 1

async def about(update, context):
    await update.message.reply_text("Всего доброго!")
    return ConversationHandler.END

async def stop(update, context):
    await update.message.reply_text("Всего доброго!")
    return ConversationHandler.END

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
                CallbackQueryHandler(catalog),
                CallbackQueryHandler(instruction),
                CallbackQueryHandler(about),
                ],
            2: [
                CallbackQueryHandler(biology),
                CallbackQueryHandler(history),
                CallbackQueryHandler(instruction),
                ],
            4: [MessageHandler(filters.TEXT & ~filters.COMMAND, biology_answers)],
            5: [MessageHandler(filters.TEXT & ~filters.COMMAND, biology_second)],
            6: [MessageHandler(filters.TEXT & ~filters.COMMAND, history)],
            7: [MessageHandler(filters.TEXT & ~filters.COMMAND, history_answers)],
            9: [MessageHandler(filters.TEXT & ~filters.COMMAND, biology)],
        },

        # Точка прерывания диалога. В данном случае — команда /stop.
        fallbacks=[CommandHandler('stop', stop)]
    )
    app.add_handler(conv_handler)
    app.run_polling()

if __name__ == '__main__':
    main()