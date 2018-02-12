from sinesp_client import SinespClient
import requests
import telepot
from telepot.loop import MessageLoop
import json

requests.packages.urllib3.disable_warnings()
bot = telepot.Bot("465979573:AAFwwtWK0dfuy6f25kFFNzqQ4TZ0-roKiCI")

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
    try:
        texto = '@PlacaInfoBot\n\n'
        texto += 'Placa: ' + str(info['plate']) + '\n'
        texto += 'Marca/Modelo: ' + str(info['model']) + '\n'
        texto += 'Chassis: ' + str( info['chassis']) + '\n'
        texto += 'Cor: ' + str(info['color']) + '\n'
        texto += 'Ano de Fabricação: ' + str(info['year']) + '\n'
        texto += 'Modelo de Fabricação: ' + str(info['model_year']) + '\n'
        texto += 'Cidade - Estado: ' + str(info['city']) + " - " + str(info['state']) + '\n'
        texto += 'Status: ' + str(info['status_message']) + '\n\n'
        texto += 'Dados do SINESP'
        bot.sendMessage(chat, texto)
    except IndexError:
        bot.sendMessage(chat, 'Erro ao buscar a placa informada, verifique se está correta')
        pass

    #print(texto)

MessageLoop(bot, handle).run_forever()
#print(json.dumps(consulta('PPA1234'), indent=4))
