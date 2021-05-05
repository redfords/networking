from ibm_watson import LanguageTranslatorV3

url_lt = 'https://gateway.watsonplatform.net/language-translator/api'

apikey_lt = '...'

version_lt = '2018-05-01'

# create a language translator object
language_translator = LanguageTranslatorV3(iam_apikey = apikey_lt, url = url_lt, version = version_lt)

language_translator.list_identifiable_languages().get_result()
# {'language': 'en', 'name': 'English'}
# {'language': 'es', 'name': 'Spanish'}

recognized_text = 'hello this is python'

translation_response = language_translator.translate(text = recognized_text, model_id = 'en-es')
translation = translation_response.get_result()

# translation
# {'translations': [{'translation': 'Hola esta es la piton'}], 'word_count': 4, 'character_count': 21}

spanish_translation = translation['translations'][0]['translation']


