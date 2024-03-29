
import database as database
import datetime as datetime
import secrets

def createdId(data):
  data_length = len(data)
  last_itemId = data[data_length - 1]["Id"]
  return last_itemId + 1

def createdDate():
  return datetime.datetime.now()

def createToken():
  return secrets.token_hex(16)

def validateToken(user_key):
  if 'Tokens' in database.local.keys():
    for token in database.local["Tokens"]:
      if token['UserKey'] == user_key:
        return True
  return  False


'''
request.args

É usado para obter os parâmetros da query string.
'''