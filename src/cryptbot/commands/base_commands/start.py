import logging

from telegram import ForceReply, Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ContextTypes
from ...superficial.strings.message_text import Messages





async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Send a message when the command /start is issued."""
    user = update.effective_user
    
    start_buttons = [
        [
            InlineKeyboardButton(
                "🤖 Help", callback_data="help"
            ),
            InlineKeyboardButton(
                "📚 Commands", callback_data="commands"
            ),
        ],
        [
            InlineKeyboardButton(
                "Services", callback_data="services"
            ),
            InlineKeyboardButton(
                "Projects", callback_data="about"
            ),
            InlineKeyboardButton(
                "Reports", callback_data="reports"
            )
        ],
        [
            InlineKeyboardButton(
                "🔐 About", callback_data="about"
            ),
            InlineKeyboardButton(
                "Settings", callback_data="settings"
            )
    ]
]
    start_keyboard = InlineKeyboardMarkup(start_buttons)
    
    await update.message.reply_html(
        Messages.START_MESSAGE,
        reply_markup=ForceReply(selective=True),
        reply_markup=start_keyboard
    )