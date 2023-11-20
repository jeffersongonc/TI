from deep_translator import GoogleTranslator
import os
from dotenv import load_dotenv

# When there is a need to use an API key
basedir = os.path.abspath(os.path.dirname(__file__))
load_dotenv(os.path.join(basedir, '.env'))
TRANSLATE_API_KEY = os.environ.get("TRANSLATE_API_KEY=") or "NONE"

#Use on source or target Acronym country 'pt' or Name country'portuguese'
translate = GoogleTranslator(source='pt', target='en')

text = "Seu texto"

print(translate.translate(text))