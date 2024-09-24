from telegram import Update, ReplyKeyboardMarkup, KeyboardButton
from telegram.ext import Application, CommandHandler, MessageHandler, filters, CallbackContext
import time

# Havolalar
ADMIN_LINK = "https://youradminlink.com"
CHANNEL_LINK = "https://t.me/yourchannel"
YOUTUBE_LINK = "https://youtube.com/yourchannel"
INSTAGRAM_LINK = "https://instagram.com/yourprofile"
PAYMENT_LINK = "https://yourpaymentlink.com"  # To'lov havolasi

# Foydalanuvchilar ro'yxati
users = []

# /start komandasini ishlovchi funksiya
async def start(update: Update, context: CallbackContext) -> None:
    reply_keyboard = [
        [KeyboardButton("Kurs videolariga kirish"), KeyboardButton("To'lov qilish")],
        [KeyboardButton("Qo'llab-quvvatlash"), KeyboardButton("Statistika")],
        [KeyboardButton("FAQ"), KeyboardButton("Formula kitoblar")],
    ]
    markup = ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True)
    await update.message.reply_text("Salom! Kursimizga xush kelibsiz. Qaysi xizmatdan foydalanmoqchisiz?", reply_markup=markup)

# Kurs videolarini va havolalarni yuborish
async def show_videos(update: Update, context: CallbackContext) -> None:
    await update.message.reply_text(f"Admin bilan bog'lanish: {ADMIN_LINK}")
    await update.message.reply_text(f"Kanalimizga obuna bo'ling: {CHANNEL_LINK}")
    await update.message.reply_text(f"YouTube kanalimiz: {YOUTUBE_LINK}")
    await update.message.reply_text(f"Instagram profilingiz: {INSTAGRAM_LINK}")

    await update.message.reply_text("Foydalanuvchilarga ko'rish uchun 2 ta video:\n"
                                    "1. Video 1 (https://yourvideo1link.com/)\n"
                                    "2. Video 2 (https://yourvideo2link.com/)", parse_mode='Markdown')

# To'lov havolasi
async def payment(update: Update, context: CallbackContext) -> None:
    await update.message.reply_text(f"To'lov qilish uchun ushbu havolani bosing: {PAYMENT_LINK}")

# Qo'llab-quvvatlash tugmasi uchun funksiya
async def support(update: Update, context: CallbackContext) -> None:
    await update.message.reply_text(f"Agar muammo yoki savolingiz bo'lsa, admin bilan bog'laning: {ADMIN_LINK}")

# Statistika ko'rsatish
async def show_statistics(update: Update, context: CallbackContext):
    await update.message.reply_text(f"Jami foydalanuvchilar soni: {len(users)}")

# FAQ bo'limi
async def faq(update: Update, context: CallbackContext):
    await update.message.reply_text("FAQ:\n"
                                    "1. Kurs qancha davom etadi?\n"
                                    "2. Qanday to'lov usullari mavjud?\n"
                                    "3. Sertifikat olsam bo'ladimi?\n"
                                    "4. Kursga qanday kiraman?")

# Formula kitoblar bo'limi
async def formula_books(update: Update, context: CallbackContext):
    await update.message.reply_text("Formula kitoblar:\n"
                                    "1. Matematika Formulalari (https://mathformulas.com/)\n"
                                    "2. Fizika Formulalari (https://physicsformulas.com/)\n"
                                    "3. Kimyo Formulalari (https://chemistryformulas.com/)", parse_mode='Markdown')

# Avtomatik eslatma funksiyasi
async def send_reminder(context: CallbackContext):
    chat_id = context.job.context
    await context.bot.send_message(chat_id=chat_id, text="Kursdagi keyingi darsni o'tishni unutmang!")

# Ro'yxatdan o'tish tugagandan keyin 1 kunda eslatma yuborish
async def phone(update: Update, context: CallbackContext) -> None:
    context.user_data['phone'] = update.message.text
    users.append(context.user_data)
    await update.message.reply_text("Siz muvaffaqiyatli ro'yxatdan o'tdingiz!")
    context.job_queue.run_once(send_reminder, 86400, chat_id=update.message.chat_id)  # 86400 = 1 kun

# Handlerlar va asosiy funksiya
async def main() -> None:
    # Botni ishga tushirish
    application = Application.builder().token("7232918320:AAF1VenP8qry_1r-NEJWjSwBO4eJauCk6Xk").build()
    
    # Dastlabki sozlashni bajarish
    await application.initialize()

    # Handlerlar
    application.add_handler(CommandHandler("start", start))
    application.add_handler(MessageHandler(filters.Regex('^Kurs videolariga kirish$'), show_videos))
    application.add_handler(MessageHandler(filters.Regex('^To\'lov qilish$'), payment))
    application.add_handler(MessageHandler(filters.Regex('^Qo\'llab-quvvatlash$'), support))
    application.add_handler(MessageHandler(filters.Regex('^Statistika$'), show_statistics))
    application.add_handler(MessageHandler(filters.Regex('^FAQ$'), faq))
    application.add_handler(MessageHandler(filters.Regex('^Formula kitoblar$'), formula_books))

    # Botni ishlatish
    await application.start_polling()
    await application.idle()

# Asosiy kodni ishga tushirish
if __name__ == "__main__":
    import asyncio
    asyncio.run(main())
