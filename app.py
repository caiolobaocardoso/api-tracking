import requests
import sys
import pandas as pd

# Opcional de extrair codigos de planilhas
path_excel = r'C:\Users\042000026\Documents\workspace\api-correios\17track\correios.xlsx'
rastreio = []
df = pd.read_excel(path_excel, sheet_name="POSTADO")
list_code_track = df['CODIGO'].values.tolist()
rastreio.append[0,1]


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