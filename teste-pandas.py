import pandas as pd

path_excel = 'codigos.xlsx'

rastreio = []
df = pd.read_excel(path_excel, sheet_name="POSTADO")
list_code_track = df.values.tolist()
rastreio.append(list_code_track)

print(rastreio)