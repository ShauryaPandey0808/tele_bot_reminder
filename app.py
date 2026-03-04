import os
import asyncio
from datetime import time
from telegram.ext import ApplicationBuilder, ContextTypes

BOT_TOKEN = os.getenv("BOT_TOKEN")
CHAT_ID = os.getenv("CHAT_ID")

async def morning(context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(
        chat_id=CHAT_ID,
        text="🌅 Good Morning Shaurya! Time to wake up!"
    )

async def night(context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(
        chat_id=CHAT_ID,
        text="🌙 Sleep time! Stop coding now 😴"
    )

async def main():
    app = ApplicationBuilder().token(BOT_TOKEN).build()

    # Schedule reminders
    app.job_queue.run_daily(morning, time(hour=7, minute=0))
    app.job_queue.run_daily(night, time(hour=23, minute=0))

    print("Reminder Bot Running 24/7...")
    await app.run_polling()

if __name__ == "__main__":
    asyncio.run(main())