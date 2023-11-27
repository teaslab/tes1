import logging
from telegram import Update 
from telegram.ext import ApplicationBuilder, CommandHandler

import handlers
import db

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

def register_handlers(app):
    app.add_handler(CommandHandler("start", handlers.start))

def main():
    app = ApplicationBuilder().token("6623783128:AAFuG_Gu8uXlJWmk0cAVvaHcpJexuypEI1c").build()
    
    db.init()
    register_handlers(app)
    
    app.run_polling()

if __name__ == "__main__":
    main()