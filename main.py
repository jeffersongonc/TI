# Automação de encaminhamento de mensagens no Whatsapp
# Usando a funcionalidade nativa do Whatsapp de encaminhar mensagem
# Encaminhar de 5 em 5 mensagens

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

service = Service(ChromeDriverManager().install())