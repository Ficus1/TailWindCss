import requests
import misc
import json

token = misc.token

# https://api.telegram.org/bot5679913288:AAE8P497msazUMCn-EejUJ0DTglpq74BwHs/sendmessage?chat_id=626437301&text=hi
URL = 'https://api.telegram.org/bot' + token + '/'


def get_updates():
  url = URL + 'getupdates'
  r = requests.get(url)
  return r.json()


def get_message():
    data = get_updates()

    chat_id = data['result'][-1]['message']['chat']['id']
    message_text = data['result'][-1]['message']['text']

    message = {'chat_id': chat_id,               'text': message_text}
    return message


def send_message(chat_id, text='Wait a second, please...'):
    url = URL + 'sendmessage?chat_id={}&text={}'.format(chat_id, text)


def main():
   d = get_updates()
   with open('updates.json', 'w') as file:
       json.dump(d, file, indent=2, ensure_ascii=False)
       send_message()


if __name__ == 'main':
  main()