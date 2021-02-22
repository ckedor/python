import time
import schedule
from whatsapp_bot import WhatsAppBot
from datetime import datetime

def SendMessageBot():
    bot = WhatsAppBot()
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    message = "OLA: " + current_time
    bot.SendMessage(message, "11981479635")
 
schedule.every(1).minutes.do(SendMessageBot)

while True: 
    schedule.run_pending() 
    time.sleep(1)
