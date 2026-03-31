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
    -1003674545815,
    -1003275633416,
    -1003610612747,
    -1002305889635,
    -1002409970793,
    -1002421490648,
    -1003674545815,
    -1003662037269,
    -1002563979963,
    -1002106012693,
    -1002287307946,
    -1003742618269,
]

MESSAGE_FIN_MOIS = """
📋 موعد التقرير

تذكير بضرورة إدخال التقرير الشهري على النظام SFSS 📊

يرجى التأكد من إدخال التقرير قبل نهاية اليوم ⏰

شكراً لتعاونكم 🙏
"""

MESSAGE_DEBUT_MOIS = """
📋 موعد التقرير

تذكير بضرورة إدخال التقرير الشهري على النظام SFSS 📊

اليوم هو اخر يوم لادخال التقرير ⏰

شكراً لتعاونكم 🙏
"""

async def send_reminder(message):
    bot = Bot(token=TOKEN)
    for chat_id in GROUPS:
        try:
            await bot.send_message(chat_id=chat_id, text=message)
            print(f"Reminder envoye au groupe {chat_id}")
        except Exception as e:
            print(f"Erreur pour le groupe {chat_id} : {e}")

async def main():
    scheduler = AsyncIOScheduler()

    # Dernier jour du mois à 12h Kuwait (9h UTC)
    scheduler.add_job(
        send_reminder,
        trigger="cron",
        day="last",
        hour=9,
        minute=0,
        args=[MESSAGE_FIN_MOIS]
    )

    # 1er jour du mois à 12h Kuwait (9h UTC)
    scheduler.add_job(
        send_reminder,
        trigger="cron",
        day=1,
        hour=9,
        minute=0,
        args=[MESSAGE_DEBUT_MOIS]
    )

    scheduler.start()
    print("Bot demarre !")
    await asyncio.Event().wait()

if __name__ == "__main__":
    asyncio.run(main())
