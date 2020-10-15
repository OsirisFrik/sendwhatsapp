import os
from dotenv import load_dotenv

load_dotenv()

from utils import getData, findIndex, formatMessage, sendUrl
from twilio.rest import Client
from ui import requestFile

FROM_PHONE = os.environ.get('FROM_PHONE')
ACCOUNT_SID = os.environ.get('ACCOUNT_SID')
ACCOUNT_TOKEN = os.environ.get('ACCOUNT_TOKEN')

filePath = requestFile()
# filePath = '/Users/osirisfrik/Desktop/Archivo de Muestra.xlsx'
data = getData(filePath)
sells = []

print(data[0])

def sendMsg():
  client = Client(ACCOUNT_SID, ACCOUNT_TOKEN)
  for s in sells:
    s['msg'] = formatMessage(s)
    client.messages.create(
      to='whatsapp:+521' + str(s['phone']),
      from_=FROM_PHONE,
      body=s['msg']
    )
  

# def init():
  # for d in data:
    # index = findIndex(sells, 'id', d['id'])
  
    # if index > -1:
      # sells[index]['products'].append({
      #   'product': d['product'],
      #   'price': d['price']
      # })
      # sells[index]['total'] += d['price']
    # else:
      # sells.append({
      #   'id': d['id'],
      #   'phone': d['phone'],
      #   'customer': d['client'],
      #   'total': d['price'],
      #   'products': [{
      #     'product': d['product'],
      #     'price': d['price']
      #   }]
      # })
  # sendMsg()

# init()