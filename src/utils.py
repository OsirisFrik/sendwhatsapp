import json
import pandas
import urllib
import webbrowser
from ui import requestSheetName

def findIndex(arr, key, val):
  # Find index in array
  index = -1
  for i, sell in enumerate(arr):
    if sell[key] == val:
      index = i
  
  return index

def getData(path):
  if path.endswith('.csv'):
    data = (pandas.read_csv(path)).to_json(orient='records')
  else:
    sheetName = requestSheetName()
    data = (pandas.read_excel(path, sheet_name=sheetName)).to_json(orient='records')

  return json.loads(data)

def spaceSize(data):
  size = len('Product')
  spaces = ''
  
  for d in data:
    l = len(d['product'])
    if l > size:
      size = l
  
  x = 0
  
  while x < size:
    spaces += ' '
    x += 1
  
  return spaces

def getSpaces(data, space):
  length = len(data)
  spaceLength = len(space)
  result = spaceLength + (spaceLength - length)
  
  spaces = ''
  
  i = 0
  while i < result:
    spaces += ' '
    i += 1
    
  return spaces

def formatMessage(data):
  # Format message to send
  space = spaceSize(data['products'])
  
  msg = 'Producto' + space + 'Precio\n'
  
  for b in data['products']:
    spaceP = getSpaces(b['product'], space)
    msg += b['product'] + spaceP + str(b['price']) + '\n'
  
  msg += '\nTotal' + getSpaces('total', space) + str(data['total'])

  return msg

def sendUrl(data):
  # Format and open whatsapp link
  url = 'whatsapp://send?phone=+52' + str(data['phone']) + '&text=' + urllib.parse.quote_plus(data['msg'])
  webbrowser.open(url)
