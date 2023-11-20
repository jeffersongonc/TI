# Automação de encaminhamento de mensagens no Whatsapp
# Usando a funcionalidade nativa do Whatsapp de encaminhar mensagem
# Encaminhar de 5 em 5 mensagens
#!pip install selenium pyperclip webdriver-manager
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

import pyperclip
import time
import os
from dotenv import load_dotenv

# inicializando variáveis

basedir = os.path.abspath(os.path.dirname(__file__))
load_dotenv(os.path.join(basedir, '.env'))
mensageiro = os.environ.get("MESSENGER") or 'NONE'
navigator_is_open = True #Manter o navegador aberto
web_adrress = ''
xpath_SEARCH_BUTTON = ''
xpath_SEARCH = ''
xpath_MESSAGE_TEXT = ''
class_MESSAGE_SELECT = ''
class_BTN_OPTIONS = ''
xpath_BTN_FORWARD = ''
xpath_BTN_SEND = ''
class_CONTEXT_MENU = ''
xpath_FORWARD_SEARCH = ''
xpath_BTN_CLICK_SEND = ''
mensagem = """Fala galera!
Teste de automação de mensagens.
"""
meucontato = os.environ.get("MY_CONTACT") or "NONE"
lista_contatos = ["Rico", "Banco Pan", "Banco Safra", "Banco BMG"]
tam_bloco = 3

def open_browse():
    service = Service(ChromeDriverManager().install())
    nav = webdriver.Chrome(service=service)
    return nav

def whatsapp():
    nav = open_browse()
    xpath_SEARCH_BUTTON = '//*[@id="side"]/div[1]/div/div/button/div[2]'
    xpath_SEARCH = '//*[@id="side"]/div[1]/div/div/div[2]/div/div[1]/p'
    xpath_MESSAGE_TEXT = '//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[1]/div[1]/div[1]/p'
    class_MESSAGE_SELECT = '_2AOIt'
    class_BTN_OPTIONS = '_3u9t-'    
    xpath_BTN_FORWARD = '//*[@id="app"]/div/span[4]/div/ul/div/li[4]/div'
    xpath_BTN_FORWARD_SEND = '//*[@id="main"]/span[2]/div/button[4]'
    xpath_FORWARD_SEARCH = '//*[@id="app"]/div/span[2]/div/div/div/div/div/div/div/div[1]/div/div/div[2]/div/div[1]'
    xpath_BTN_CLICK_SEND = '//*[@id="app"]/div/span[2]/div/div/div/div/div/div/div/span/div/div'
    meucontato = os.environ.get("MY_CONTACT") or "NONE"
    web_adrress = "https://web.whatsapp.com/"
    nav.get(web_adrress)
    time.sleep(60)

    nav.find_element('xpath', xpath_SEARCH_BUTTON).click()
    # escrever meu numero
    nav.find_element('xpath', xpath_SEARCH).send_keys(meucontato)
    time.sleep(1)
    # dar um enter
    nav.find_element('xpath', xpath_SEARCH).send_keys(Keys.ENTER)
    # clicar no campo de mensagem
    time.sleep(1)
    nav.find_element('xpath', xpath_MESSAGE_TEXT).click()
    # Escrever a mensagem
    time.sleep(1)
    pyperclip.copy(mensagem)
    nav.find_element('xpath', xpath_MESSAGE_TEXT).send_keys(Keys.CONTROL + "v")
    # dar enter ára enviar a mensagem
    time.sleep(1)
    nav.find_element('xpath', xpath_MESSAGE_TEXT).send_keys(Keys.ENTER)
    time.sleep(3)
    # encaminhar a mensagem para a lista de contatos
    # Definir quantidade de encaminhamentos
    if len(lista_contatos) % tam_bloco == 0:
        qt_blocos = int(len(lista_contatos) / tam_bloco)
    else:
        qt_blocos = int(len(lista_contatos) / tam_bloco) + 1

    for i in range(qt_blocos):
        i_inicial = i * tam_bloco
        i_final = (i + 1) * tam_bloco
        lista_enviar = lista_contatos[i_inicial:i_final]

        lista_elementos = nav.find_elements('class name', class_MESSAGE_SELECT)

        # Selecionar a última mensagem
        for item in lista_elementos:
            mensagem_fw = mensagem.replace("\n", "")
            texto = item.text.replace("\n", "")
            if mensagem_fw in texto:
                elemento = item

        # Posicionar na mensagem
        ActionChains(nav).move_to_element(elemento).perform()
        
        # Clicar no dropdown de opções
        elemento.find_element('class name', class_BTN_OPTIONS).click()
        time.sleep(1)
        # Clicar no encaminhar da lista de opções
        nav.find_element('xpath', xpath_BTN_FORWARD).click()
        time.sleep(1)
        # Clicar no encaminhar
        nav.find_element('xpath', xpath_BTN_FORWARD_SEND).click()
        time.sleep(1)
        # Varrer a lista de contatos até o limite de encaminhamentos por blocos
        for contato in lista_enviar:
            # Digitar o nome do contato
            nav.find_element('xpath', xpath_FORWARD_SEARCH).send_keys(contato)
            time.sleep(1)
            # Pressionar enter após digitar para marcar o envio
            nav.find_element('xpath', xpath_FORWARD_SEARCH).send_keys(Keys.ENTER)
            time.sleep(1)
            # Apagar o que contato digitou
            nav.find_element('xpath', xpath_FORWARD_SEARCH).send_keys(Keys.BACKSPACE)

        # Enviar a mensagem para o grupo de contatos do bloco
        nav.find_element('xpath', xpath_BTN_CLICK_SEND).click()
        time.sleep(2)
    
    while (navigator_is_open):
        pass

def telegram():
    nav = open_browse()
    web_adrress = "https://web.telegram.org/a/"
    xpath_SEARCH_BUTTON = '//*[@id="telegram-search-input"]'
    xpath_SEARCH = '//*[@id="telegram-search-input"]'
    xpath_MESSAGE_TEXT = '//*[@id="editable-message-text"]'
    class_MESSAGE_SELECT = 'can-select-text'
    class_CONTEXT_MENU = 'MessageContextMenu'
    xpath_FORWARD_SEARCH = '//*[@id="portals"]/div[2]/div/div/div[2]/div/div/div/div[1]/div/input'
    xpath_BTN_CLICK_SEND = '//*[@id="MiddleColumn"]/div[4]/div[2]/div[2]/div[2]/div[1]/button'
    meucontato = 'Saved Messages'
    nav.get(web_adrress)
    time.sleep(60)

    # enviar a mensagem para o meu número para poder depois encaminhar
    time.sleep(3)
    # clicar na lupa
    nav.find_element('xpath', xpath_SEARCH_BUTTON).click()
    # escrever meu numero
    nav.find_element('xpath', xpath_SEARCH).send_keys(meucontato)
    time.sleep(2)
    # dar um enter
    nav.find_element('xpath', xpath_SEARCH).send_keys(Keys.ENTER)
    # clicar no campo de mensagem 
    time.sleep(2)
    nav.find_element('xpath', xpath_MESSAGE_TEXT).click()
    # Escrever a mensagem
    time.sleep(2)
    pyperclip.copy(mensagem)
    nav.find_element('xpath', xpath_MESSAGE_TEXT).send_keys(Keys.CONTROL + "v")
    # dar enter ára enviar a mensagem
    time.sleep(2)
    nav.find_element('xpath', xpath_MESSAGE_TEXT).send_keys(Keys.ENTER)
    time.sleep(3)
    # encaminhar a mensagem para a lista de contatos
    for contato in lista_contatos:
        # clicar na lupa
        nav.find_element('xpath', xpath_SEARCH_BUTTON).click()
        time.sleep(2)
        nav.find_element('xpath', xpath_SEARCH).send_keys(Keys.BACKSPACE)
        # escrever meu numero
        nav.find_element('xpath', xpath_SEARCH).send_keys(meucontato)
        time.sleep(2)
        # dar um enter
        nav.find_element('xpath', xpath_SEARCH).send_keys(Keys.ENTER)
        # clicar no campo de mensagem
        time.sleep(2)
        lista_elementos = nav.find_elements('class name', class_MESSAGE_SELECT)

        # Selecionar a última mensagem
        for item in lista_elementos:
            mensagem_fw = mensagem.replace("\n", "")
            texto = item.text.replace("\n", "")
            if mensagem_fw in texto:
                elemento = item

        # Posicionar na mensagem
        ActionChains(nav).move_to_element(elemento).perform()
        time.sleep(2)
        # Clicar no dropdown de opções
        ActionChains(nav).context_click(elemento).perform()
        time.sleep(2)
        # Clicar no encaminhar da lista de opções
        lista_opcoes = nav.find_elements('class name', class_CONTEXT_MENU)
        for opcoes in lista_opcoes:
            if 'FORWARD' in opcoes.text.upper():
                fw = opcoes
                
        fw.find_element('class name', 'icon-forward').click()      
        time.sleep(3)
        nav.find_element('xpath', xpath_FORWARD_SEARCH).send_keys(contato)
        time.sleep(3)
        # Pressionar enter após digitar para marcar o envio
        nav.find_element('xpath', xpath_FORWARD_SEARCH).send_keys(Keys.ENTER)
        time.sleep(3)
        nav.find_element('xpath', xpath_BTN_CLICK_SEND).click()
        time.sleep(3)
    while (navigator_is_open):
        pass


#whatsapp() or telegram()