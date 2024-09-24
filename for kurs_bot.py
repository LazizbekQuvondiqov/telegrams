from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters, CallbackContext
import logging

# Initialize logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO,
)

# Admin and bot details
ADMIN_CHAT_ID = '1205534758'  # Replace with the admin's chat ID
USER_IDS = {}  # Dictionary to keep track of users and their messages

# /start command handler with inline buttons
async def start(update: Update, context: CallbackContext):
    # Inline keyboard with multiple options
    keyboard = [
        [InlineKeyboardButton("🗣 Online guruh", url="https://t.me/School_Bridge")],
        [InlineKeyboardButton("📺 YouTube kanal", url="https://youtube.com/yourchannel")],
        [InlineKeyboardButton("📸 Instagram", url="https://instagram.com/yourprofile")],
        [InlineKeyboardButton("🎥 Kurs videolarini ko'rish", url="https://yourvideospage.com")],
        [InlineKeyboardButton("👨‍💼 Admin bilan bog'lanish", url="https://t.me/Lazizbek_Quvondiqov")]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)

    # Send welcome message with the buttons
    await update.message.reply_text(
        "Assalom alaykum! Kursimizga xush kelibsiz. Quyidagi tugmalar orqali turli xizmatlardan foydalanishingiz mumkin:",
        reply_markup=reply_markup
    )

# Forward text messages to admin and store user info
async def forward_to_admin(update: Update, context: CallbackContext):
    if update.message and update.message.text:
        user_name = update.message.from_user.full_name
        user_id = update.message.from_user.id
        user_message = update.message.text

        # Save the user ID and name for later reference
        USER_IDS[user_id] = user_name

        # Send the message to the admin
        await context.bot.send_message(
            chat_id=ADMIN_CHAT_ID,
            text=f"Yangi matnli xabar:\n\nFoydalanuvchi: {user_name} (ID: {user_id})\n\n{user_message}"
        )

        # Confirm message received by the user
        await update.message.reply_text("Xabaringiz yuborildi! Lazizbek Quvondiqov tez orada siz bilan bog'lanadi.")

# Function to send a reply from admin to the user
async def reply_to_user(update: Update, context: CallbackContext):
    # Check if the message is coming from the admin chat
    if update.message.chat_id == int(ADMIN_CHAT_ID):
        try:
            # Admin's reply format: /reply user_id message
            command_parts = update.message.text.split(' ', 2)
            user_id = int(command_parts[1])  # Extract the user ID from the command
            admin_message = command_parts[2]  # The message admin wants to send

            # Send the message to the user
            await context.bot.send_message(
                chat_id=user_id,
                text=f"Admin javobi: {admin_message}"
            )

            # Confirm to the admin that the message was sent
            await update.message.reply_text(f"Javob foydalanuvchiga yuborildi: {USER_IDS.get(user_id, 'Foydalanuvchi')}")

        except (IndexError, ValueError):
            await update.message.reply_text("Foydalanuvchiga javob yuborish uchun format:\n /reply user_id xabar")

    else:
        await update.message.reply_text("Siz admin emassiz!")

# Function to list all users who interacted with the bot
async def list_users(update: Update, context: CallbackContext):
    # Check if the message is coming from the admin
    if update.message.chat_id == int(ADMIN_CHAT_ID):
        if USER_IDS:
            user_list = "\n".join([f"{user_name} (ID: {user_id})" for user_id, user_name in USER_IDS.items()])
            await update.message.reply_text(f"Botdan foydalanganlar:\n\n{user_list}")
        else:
            await update.message.reply_text("Hozircha hech kim botdan foydalanmadi.")
    else:
        await update.message.reply_text("Siz admin emassiz!")

# Main function to run the bot
if __name__ == '__main__':
    token = '7232918320:AAF1VenP8qry_1r-NEJWjSwBO4eJauCk6Xk'  # Replace with your bot token

    application = ApplicationBuilder().token(token).build()

    # Command handlers
    application.add_handler(CommandHandler('start', start))
    application.add_handler(CommandHandler('users', list_users))  # Admin command to list users

    # Message handler for forwarding only text messages to admin
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, forward_to_admin))

    # Message handler for admin replies
    application.add_handler(MessageHandler(filters.Regex('^/reply '), reply_to_user))

    # Run the bot
    application.run_polling()
