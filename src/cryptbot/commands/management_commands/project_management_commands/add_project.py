
from telegram import Update
from telegram.ext import ContextTypes
from ....db.models.base.project import Project
async def add_project_help(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Send a message when the command /help is issued."""
    await update.message.reply_text("P")


async def ask_user_for_project_name(update: Update, context: ContextTypes.DEFAULT_TYPE) -> str:
    """
    A function that is called when the user sends the /add_project command.
    It asks the user to enter a project name, and creates it in the database.
    """
    text = "What would you like to name your project?\n\nPlease reply with your project name:"

    await update.callback_query.message.reply_text(text)
    


async def add_project(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """
    A function that is called when the user sends the /add_project command.
    It asks the user to enter a project name, and creates it in the database.
    """
    
    # Ask the user to enter a project name
    # by sending a message to the user
    # containing the text "Enter a project name:"
    await update.message.reply_text("Enter a project name:")

    # Save the project name in the database
    # by creating a new instance of the Project model
    # and calling the save() method on it
    project_name = update.message.text
    project = Project(name=project_name)
    await project.save()
    
    # Send a message to the user with the project name
    # to confirm that the project was created
    await update.message.reply_text(f"Project {project_name} Created")
    
    
