from telegram import Update
from telegram.ext import ContextTypes

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(
        "Нажми /start", 
        reply_markup=buttons()
    )
    
def buttons():
    # генерация кнопок
    pass