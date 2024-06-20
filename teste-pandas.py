import pandas as pd

path_excel = 'C:/Users/042000026/Documents/workspace/api-correios/17track/correios.xlsx'

rastreio = []
df = pd.read_excel(path_excel, sheet_name="POSTADO")
list_code_track = df['CODIGO'].values.tolist()
rastreio.append(0)

print(rastreio)