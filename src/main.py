import logging

from telegram import Update
from telegram.ext import Application, ApplicationBuilder, CommandHandler, ContextTypes
from cryptbot.commands.base_commands.start import start
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO,
)

logging.getLogger("httpx").setLevel(logging.WARNING)
logging.getLogger(__name__)



# import commands




def main() -> None:
    application = Application.builder().token("TOKEN").build()
    
    #### COMMANDS HERE ####

    application.add_handler(CommandHandler("start", start))

    application.run_polling()