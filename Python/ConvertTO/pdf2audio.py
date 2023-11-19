import pyttsx3
from PyPDF2 import PdfReader

text = ''
try:
    reader = PdfReader("audio.pdf")

    pages = reader.pages

    for page in pages:
        text += page.extract_text()

    #print(text)
except:
    print('Não foi possível abrir/encontrar o arquivo.')

try:
    engine = pyttsx3.init()
    engine.save_to_file(text, 'audio.mp3')
    #engine.say(text)
    engine.runAndWait()
except:
    print('Não foi possível criar o arquivo de audio.')