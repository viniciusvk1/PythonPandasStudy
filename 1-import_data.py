import pandas as pd

# 1- Importando dados .xlsx
data = pd.read_excel("data/VendaCarros.xlsx")
print(data)

# 2- Lista os primeiros registros
print(data.head())

# 3- Lista os ultimos registros
print(data.tail())

# 4- Contagem de valores por fabricante
print(data["Fabricante"].value_counts())