import os
import pandas as pd
from telegram import Update, ReplyKeyboardMarkup, KeyboardButton
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters, CallbackContext
import logging
from datetime import datetime

# Initialize logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO,
)

# Admin contact details and links
ADMIN_CONTACT = "947779891"
admin = "@Lazizbek_Quvondiqov"
GROUP_LINK = "https://t.me/School_Bridge"
YOUTUBE_LINK = "https://youtube.com/yourchannel"
INSTAGRAM_LINK = "https://instagram.com/yourprofile"
VIDEO_1_LINK = "https://yourvideo1link.com"
VIDEO_2_LINK = "https://yourvideo2link.com"

# Log user info with timestamp to Excel (excluding user ID)
def log_user_info(update: Update):
    user = update.message.from_user
    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    user_data = {
        'First Name': user.first_name,
        'Last Name': user.last_name,
        'Username': user.username,
        'Timestamp': timestamp
    }
    
    # Append data to an Excel file
    file_exists = os.path.exists('bot_users.xlsx')
    df = pd.DataFrame([user_data])
    
    with pd.ExcelWriter('bot_users.xlsx', mode='a' if file_exists else 'w', engine='openpyxl') as writer:
        df.to_excel(writer, index=False, header=not file_exists, sheet_name='Users')

async def show_users(update: Update, context: CallbackContext):
    # Check if the Excel file exists
    if os.path.exists('bot_users.xlsx'):
        df = pd.read_excel('bot_users.xlsx')
        logs = df.to_string(index=False)
        await update.message.reply_text(logs or "Hech qanday foydalanuvchi ma'lumotlari yo'q.")
    else:
        await update.message.reply_text("Hech qanday foydalanuvchi ma'lumotlari yo'q.")

# /start command handler
async def start(update: Update, context: CallbackContext):
    log_user_info(update)  # Log user info
    reply_keyboard = [
        [KeyboardButton("Admin bilan bog'lanish")],
        [KeyboardButton("Online guruh")],
        [KeyboardButton("Bir nechta kursimiz videolarini ko'rish")],
        [KeyboardButton("YouTube kanal")],
        [KeyboardButton("Instagram")],
        [KeyboardButton("Foydalanuvchilarni ko'rish")]  # Add button to view users
    ]
    markup = ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True, resize_keyboard=True)
    await update.message.reply_text("Assalom alaykum! Kursimizga xush kelibsiz. Qaysi xizmatdan foydalanmoqchisiz?", reply_markup=markup)

# Contact admin
async def contact_admin(update: Update, context: CallbackContext):
    await update.message.reply_text(f"Admin bilan bog'lanish telifon: {ADMIN_CONTACT}, Telegram: {admin}")

# Show group link
async def show_group(update: Update, context: CallbackContext):
    await update.message.reply_text(f"Online guruhimiz: {GROUP_LINK}")

# Show YouTube link
async def show_youtube(update: Update, context: CallbackContext):
    await update.message.reply_text(f"YouTube kanalimiz: {YOUTUBE_LINK}")

# Show Instagram link
async def show_instagram(update: Update, context: CallbackContext):
    await update.message.reply_text(f"Instagram profilimiz: {INSTAGRAM_LINK}")

# Show course videos
async def show_videos(update: Update, context: CallbackContext):
    await update.message.reply_text("Kurs videolarini ko'rish:\n"
                                    f"1. Video 1: {VIDEO_1_LINK}\n"
                                    f"2. Video 2: {VIDEO_2_LINK}\n\n"
                                    "Agar darslarni maqul topsangiz, ro'yhatdan o'tish uchun admin bilan bog'laning.")

# Main function to run the bot
if __name__ == '__main__':
    token = '7232918320:AAF1VenP8qry_1r-NEJWjSwBO4eJauCk6Xk'  # Replace with your bot token

    application = ApplicationBuilder().token(token).build()

    application.add_handler(CommandHandler('start', start))
    application.add_handler(MessageHandler(filters.Regex('^Admin bilan bog\'lanish$'), contact_admin))
    application.add_handler(MessageHandler(filters.Regex('^Online guruh$'), show_group))
    application.add_handler(MessageHandler(filters.Regex('^YouTube kanal$'), show_youtube))
    application.add_handler(MessageHandler(filters.Regex('^Instagram$'), show_instagram))
    application.add_handler(MessageHandler(filters.Regex('^Bir nechta kursimiz videolarini ko\'rish$'), show_videos))
    application.add_handler(CommandHandler('users', show_users))  # Command to show users

    application.run_polling()
