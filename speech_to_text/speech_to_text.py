from ibm_watson import SpeechToTextV1

url_s2t = "https://stream.watsonplatform.net/speech-to-text/api"

iam_apikey_s2t = "..."

# create a speech-to-text adapter object
s2t = SpeechToTextV1(iam_apikey = iam_apikey_s2t, url = url_s2t)

filename = "hello_this_is_python.wav"
# read the file in binary format
with open(filename, mode = "rb") as wav:
    response = s2t.recognize(audio = wav, content_type = 'audio/wav')

# response.result
# {'results': [{'alternatives': [{'confidence': 0.91, 'transcript': 'hello this is python'}],
# 'final': True}], 'result_index': 0}

recognized_text = response.result['results'][0]["alternatives"][0]["transcript"]
# recognized_text : 'hello this is python'
