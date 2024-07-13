
from telegram import Update
from telegram.ext import ContextTypes

async def add_project_help(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Send a message when the command /help is issued."""
    await update.message.reply_text("P")


async def add_project(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    # 