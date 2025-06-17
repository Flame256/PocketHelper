import os
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
from apscheduler.schedulers.background import BackgroundScheduler

TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Привет! Я твой PocketHelper.")

def scheduled_task():
    print("Выполняется запланированная задача.")

if __name__ == "__main__":
    app = ApplicationBuilder().token(TELEGRAM_TOKEN).build()
    app.add_handler(CommandHandler("start", start))

    scheduler = BackgroundScheduler()
    scheduler.add_job(scheduled_task, "interval", minutes=60)
    scheduler.start()

    app.run_polling()
