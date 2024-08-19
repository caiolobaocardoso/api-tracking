import requests
import sys
import pandas as pd

rastreio = []

path_excel = 'codigos.xlsx'
df = pd.read_excel(path_excel, sheet_name='POSTADO')
codigos_rastreio = df.values.tolist()
rastreio.append(codigos_rastreio)


#Payload do request
for codigo in rastreio:
  url = "https://api.17track.net/track/v2.2/register"
  payload =  [
                  {
        "number": f"{codigo}",
        "auto_detection": True,
        "lang": "en"
        }
        ] 

  headers = {
        "content-type": "application/json",
        "17token": "E04997BA7983691F681C6DAA8DFDAC2C"
    }
  response = requests.request("POST", url, json=payload, headers=headers)

  #output do arquivo
  with open("output.json", "w") as f:
      f.write(f'\n{response.text}')
  