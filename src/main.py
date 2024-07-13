import logging

from telegram import Update
from telegram.ext import Application, ApplicationBuilder, CommandHandler, ContextTypes, ConversationHandler
from cryptbot.commands.base_commands.start import start

from cryptbot.commands.base_commands.help import help_command
from cryptbot.commands.management_commands.project_management_commands.add_project import add_project, add_project_help
from cryptbot.commands.management_commands.scope_management_commands.add_to_scope import add_to_scope



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
    add_project_convsersation_handler = ConversationHandler(
        entry_points=[
                CommandHandler("add_project", add_project),
            ],
        states={
            ASKING_PROJECT_NAME: [
                CallbackQueryHandler(),
            
        },
    )
    
    application.add_handler(add_project_convsersation_handler)
    application.run_polling(allowed_updates=Update.ALL_TYPES)
    
if __name__ == "__main__":
    main()