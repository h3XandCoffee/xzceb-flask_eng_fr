import os
import json
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from dotenv import load_dotenv

load_dotenv()

apikey = os.environ['apikey']
url = os.environ['url']
version = os.environ['version']

authenticator = IAMAuthenticator(apikey)
language_translator = LanguageTranslatorV3(
    version=version,
    authenticator=authenticator
)

language_translator.set_service_url(url)

def englishToFrench (englishText):
    """
    " English to French translation.
    """
    if englishText in (None, ''):
        englishText = "Text for translation not provided. Please provide the text for translation!"

    translation = language_translator.translate(
        text=englishText,
        model_id='en-fr').get_result()
    return translation['translations'][0]['translation']

def frenchToEnglish(frenchText):
    """
    " French to English translation.
    """
    if frenchText in (None, ''):
        frenchText = "Texte à traduire non fourni. Veuillez fournir le texte à traduire!"

    translation = language_translator.translate(
        text=frenchText,
        model_id='fr-en').get_result()
    return translation['translations'][0]['translation']
