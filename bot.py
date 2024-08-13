from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, CallbackQueryHandler, MessageHandler, filters, \
    CallbackContext

# Bot tokenini kiriting
TOKEN = '7455399323:AAGHEurlI8ykd12V-8-KTiv7gYKBlG9lfb4'


async def start(update: Update, context: CallbackContext) -> None:
    keyboard = [
        [InlineKeyboardButton("Salom", callback_data='1')],
        [InlineKeyboardButton("Yordam", callback_data='2')]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text('Salom! Men Notcoin botiman. Qanday yordam bera olaman?', reply_markup=reply_markup)


async def button(update: Update, context: CallbackContext) -> None:
    query = update.callback_query
    await query.answer()

    if query.data == '1':
        await query.edit_message_text(text="Salom! Siz 'Salom' tugmasini bosdingiz.")
    elif query.data == '2':
        await query.edit_message_text(text="Bu yordam xabari. Nima qilishni xohlaysiz?")


async def help_command(update: Update, context: CallbackContext) -> None:
    await update.message.reply_text('Bu yordam xabari. Nima qilishni xohlaysiz?')


async def echo(update: Update, context: CallbackContext) -> None:
    await update.message.reply_text(update.message.text)


def main() -> None:
    # ApplicationBuilder orqali botni yarating
    application = ApplicationBuilder().token(TOKEN).build()

    # Handlerlarni qo'shing
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("help", help_command))
    application.add_handler(CallbackQueryHandler(button))
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, echo))

    # Botni ishga tushiring
    application.run_polling()


if __name__ == '__main__':
    main()
