import os
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters, CallbackContext

# Admin chat ID sini o'zgartiring
ADMIN_CHAT_ID = '1205534758'

# /start buyrug'iga javob beradigan funksiya
async def start(update, context: CallbackContext):
    await update.message.reply_text("Assalom alaykum, men sizga qanday yordam bera olaman?")

# Botga kelgan xabarlarni adminlarga yuboradigan funksiya
async def forward_to_admin(update, context: CallbackContext):
    user_name = update.message.from_user.full_name
    user_id = update.message.from_user.id

    if update.message.photo:
        file_id = update.message.photo[-1].file_id
        file = await context.bot.get_file(file_id)
        file_url = file.file_path
        caption = "Rasm"
    elif update.message.video:
        file_id = update.message.video.file_id
        file = await context.bot.get_file(file_id)
        file_url = file.file_path
        caption = "Video"
    elif update.message.document:
        file_id = update.message.document.file_id
        file = await context.bot.get_file(file_id)
        file_url = file.file_path
        caption = "Fayl"
    else:
        user_message = update.message.text
        caption = f"Matnli xabar: {user_message}"
        file_url = None

    await context.bot.send_message(
        chat_id=ADMIN_CHAT_ID,
        text=f"Yangi xabar:\n\nFoydalanuvchi: {user_name} (ID: {user_id})\n{caption}\n\n{file_url if file_url else ''}"
    )

    await update.message.reply_text("Xabaringiz yuborildi! Lazizbek Quvondiqov tez orada siz bilan bog'lanadi.")

# Botni ishga tushirish
if __name__ == '__main__':
    # Bot tokenini kiritish
    token = '7481098564:AAFHOFwoL15UnqcL6TCJiSaJ2MIXD60OV8I'

    application = ApplicationBuilder().token(token).build()

    start_handler = CommandHandler('start', start)
    application.add_handler(start_handler)

    message_handler = MessageHandler(filters.ALL & ~filters.COMMAND, forward_to_admin)
    application.add_handler(message_handler)

    application.run_polling()
