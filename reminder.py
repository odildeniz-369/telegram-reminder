import asyncio
from telegram import Bot
from datetime import datetime

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

async def send_reminder(message):
    bot = Bot(token=TOKEN)
    for chat_id in GROUPS:
        try:
            await bot.send_message(chat_id=chat_id, text=message)
            print(f"Reminder envoye au groupe {chat_id}")
        except Exception as e:
            print(f"Erreur pour le groupe {chat_id} : {e}")


async def main():
    bot = Bot(token=TOKEN)
    day = datetime.utcnow().day
    
    if day == 1:
        message = MESSAGE_DEBUT_MOIS
    else:
        message = MESSAGE_FIN_MOIS

    for chat_id in GROUPS:
        try:
            await bot.send_message(chat_id=chat_id, text=message)
            print(f"Reminder envoye au groupe {chat_id}")
        except Exception as e:
            print(f"Erreur pour le groupe {chat_id} : {e}")

if __name__ == "__main__":
    asyncio.run(main())
