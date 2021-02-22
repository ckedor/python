''' 
    Arquivo de testes para o WhatsAppBot.
'''

from whatsapp_bot import WhatsAppBot

bot = WhatsAppBot()
bot.OpenBrowser()
bot.SendMessage("Ola", "11981479635")
bot.CloseBrowser()