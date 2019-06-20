# -*- coding: utf-8 -*-
import json
import requests
#import telebot
#import parsing_zadanie_money as par

token = 'Вставте ваш токен'
URL = 'https://api.telegram.org/bot'
global last_upd 
last_upd  = 0
def get_updates():
    #my_url = 'https://api.telegram.org/bot'+token+'/GetUpdates'
    my_url = URL+token+'/GetUpdates'
    r = requests.get(my_url)
    return r.json()

def get_message():
    data = get_updates()
    last_obj = data['result'][-1]
    update_id = last_obj['update_id']
    chat_id = last_obj['message']['chat']['id']
    message_text = last_obj['message']['text']
    
    message = {'chat_id': chat_id,
               'text':message_text}
    return message

def send_message(chat_id,text):
 
    url = URL + token+ '/sendmessage?chat_id={}&text={}'.format(chat_id,text)
    requests.get(url)
'''
def get_money():
    url = 'http://www.nbrb.by/API/ExRates/Rates?Periodicity=0'
    response = requests.get(url).json()
    print(response)
 '''   
def main():
   ''' 
    answer = get_message()
    print(answer)
    chat_id = answer['chat_id']
    send_message(chat_id,'Чё надо')
    #d = get_updates()
    #print(get_message())
   '''
   answer = get_message()
   chat_id = answer['chat_id']
   mny = par.getting_money()
   #mny_answ = str(mny[0]) + ' курс ' + str(mny[1]) + ' рублей за 1 Евро, ' + str(mny[2]) + ' за 1 доллар'
   text = answer['text']
   
   #get_money()
   
   if 'ничего' in text:
       send_message(chat_id,'Вали')
    
   if 'курс' in text:
       send_message(chat_id,'mny_answ' )
   
'''
    with open('updates.json','w') as file:
        json.dump(d ,file ,indent = 2, ensure_ascii = False)
'''
if __name__ == '__main__':
    main()
