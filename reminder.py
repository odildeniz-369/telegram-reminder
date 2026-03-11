import asyncio
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from telegram import Bot

TOKEN = "8746997616:AAGeC_OvOmdseeYz9YQDavPz-l5O3ve_Tg4"

GROUPS = [
    -4156278698,
    -1002225773041,
    -4043849089,
    -4060990536,
    -4548714469,
    -4027874883,
    -4256736564,
    -4180034271,
    -4097089407,
    -4081031595,
    -1003120572371,
]

JOUR_ENVOI = "last"
HEURE = 9
MINUTES = 0

MESSAGE = """
📋 موعد التقرير

تذكير بضرورة إدخال التقرير الشهري على النظام SFSS 📊

يرجى التأكد من إدخال التقرير قبل نهاية اليوم ⏰

شكراً لتعاونكم 🙏
"""

async def send_monthly_reminder():
    bot = Bot(token=TOKEN)
    for chat_id in GROUPS:
        try:
            await bot.send_message(chat_id=chat_id, text=MESSAGE)
            print(f"Reminder envoye au groupe {chat_id}")
        except Exception as e:
            print(f"Erreur pour le groupe {chat_id} : {e}")

async def main():
    scheduler = AsyncIOScheduler()
    scheduler.add_job(
        send_monthly_reminder,
        trigger="cron",
        day=JOUR_ENVOI,
        hour=HEURE,
        minute=MINUTES
    )
    scheduler.start()
    print("Bot demarre !")
    await asyncio.Event().wait()

if __name__ == "__main__":
    asyncio.run(main())
