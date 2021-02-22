'''
Instruções:
1 - Para usar o BOT pela primeira vez, é necessário escanear o QRCode com o celular
2 - O Bot só irá funcionar se seu celular estiver online com o WhatsApp aberto 
'''

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import time
import schedule

from config import WHATSAPP_PHONE_URL
from config import CHROME_PROFILE_PATH


class WhatsAppBot:

    def __init__(self):
        self.browser = None 
        self.options = webdriver.ChromeOptions()
        self.options.add_argument(CHROME_PROFILE_PATH)

    def SendMessage(self, message, phone):
        
        '''Open Browser'''
        self.browser = webdriver.Chrome(options=self.options)
        
        url = WHATSAPP_PHONE_URL + phone
        self.browser.get(url)
        time.sleep(5)
        curr_element = self.browser.find_element_by_id("action-button")
        curr_element.click()
        time.sleep(1)
        curr_element = self.browser.find_element_by_xpath("//*[text()='use o WhatsApp Web']")
        curr_element.click()
        time.sleep(4)
        curr_element = self.browser.find_elements_by_class_name("_3FRCZ")
        curr_element = curr_element[1]   #todo fazer de forma mais elegante
        curr_element.send_keys(message)
        curr_element.send_keys(Keys.ENTER)
        
        '''Close Browser'''
        self.browser.close()