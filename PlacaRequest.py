from sinesp_client import SinespClient
import requests
import telepot
from telepot.loop import MessageLoop
import json

requests.packages.urllib3.disable_warnings()
bot = telepot.Bot("465979573:AAEMqFejVBwqJaRBFsTBU-FBMba2Bk5eFcw")

def consulta(placa, chat):
    sc = SinespClient()
    #print(placa)
    info = sc.search(placa)
    retornaPlaca(info, chat)

def handle(msg):
    content_type, chat_type, chat_id = telepot.glance(msg)
    if content_type == 'text':
        if '/placa ' in msg['text']:
            consulta(msg['text'].replace('/placa ', ''), chat_id)
        elif '/start' in msg['text']:
            bot.sendMessage(chat_id, 'Para começar, me envie a placa do veículo com o comando /placa')
        elif msg['text'] == '/placa':
            bot.sendMessage(chat_id, 'Digite a placa logo após o comando')
        else:
            consulta(msg['text'], msg['chat']['id'])



def retornaPlaca(info, chat):
    texto = '@PlacaInfoBot\n\n'
    texto += 'Placa: ' + info['plate'] + '\n'
    texto += 'Marca/Modelo: ' + info['model'] + '\n'
    texto += 'Chassis: ' + info['chassis'] + '\n'
    texto += 'Cor: ' + info['color'] + '\n'
    texto += 'Ano de Fabricação: ' + info['year'] + '\n'
    texto += 'Modelo de Fabricação: ' + info['model_year'] + '\n'
    texto += 'Cidade - Estado: ' + info['city'] + info['state'] + '\n'
    texto += 'Status: ' + info['status_message'] + '\n\n'
    texto += 'Dados do SINESP'
    bot.sendMessage(chat, texto)
    #print(texto)

MessageLoop(bot, handle).run_forever()
#print(json.dumps(consulta('PPA1234'), indent=4))
