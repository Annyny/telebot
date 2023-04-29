from config import TOKEN
from telegram.ext import Application, CommandHandler, MessageHandler, ConversationHandler, filters, CallbackQueryHandler
from telegram import ReplyKeyboardMarkup, InlineKeyboardMarkup, InlineKeyboardButton
import logging

# Запускаем логгирование
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.DEBUG
)

logger = logging.getLogger(__name__)


async def start(update, context):
    keyboard = [
        [
            InlineKeyboardButton("Вход", callback_data=str(first_entrance)),
            InlineKeyboardButton("Регистрация", callback_data=str(registration)),
        ]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    # Send message with text and appended InlineKeyboard
    await update.message.reply_text("Привет. Я бот-магазин игрушек. Вы зарегистрированы?", reply_markup=reply_markup)
    # Tell ConversationHandler that we're in state `FIRST` now
    return 1

async def first_entrance(update, context):
    query = update.callback_query
    await query.answer()
    await query.edit_message_text(text="Вход\nВведите ваш логин:")
    return 2

async def second_entrance(update, context):
    keyboard = [
        [
            InlineKeyboardButton("Забыли пароль?", callback_data=str(registration)),
        ]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text(text="Вход\nВведите ваш пароль:", reply_markup=reply_markup)
    return 3

async def registration(update, context):
    await update.message.reply_text("Регистрация\nНапишите ваш логин:")
    return 1


# async def first_response(update, context):
#     # Это ответ на первый вопрос.
#     # Мы можем использовать его во втором вопросе.
#     locality = update.message.text
#     await update.message.reply_text(
#         f"Какая погода в городе {locality}?")
#     # Следующее текстовое сообщение будет обработано
#     # обработчиком states[2]
#     return 2

async def second_response(update, context):
    # Ответ на второй вопрос.
    # Мы можем его сохранить в базе данных или переслать куда-либо.
    weather = update.message.text
    logger.info(weather)
    await update.message.reply_text("Спасибо за участие в опросе! Всего доброго!")
    return ConversationHandler.END  # Константа, означающая конец диалога.
    # Все обработчики из states и fallbacks становятся неактивными.


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
                CallbackQueryHandler(first_entrance),
                CallbackQueryHandler(registration),
                ],
            # Функция читает ответ на второй вопрос и завершает диалог.
            2: [MessageHandler(filters.TEXT & ~filters.COMMAND, second_entrance)],
            3: [MessageHandler(filters.TEXT & ~filters.COMMAND, second_entrance)]
        },

        # Точка прерывания диалога. В данном случае — команда /stop.
        fallbacks=[CommandHandler('stop', stop)]
    )
    app.add_handler(conv_handler)
    app.run_polling()

if __name__ == '__main__':
    main()