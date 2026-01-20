# Executado no COLAB
import pandas as pd

# Extrair os dados do CSV e converte para uma lista de dicionários
df = pd.read_csv('./data/users.csv')
users = df.to_dict(orient='records')

# Transformação enriquecendo a coluna Name e ordenar por ela
for user in users:
  user['Name'] = user['firstName'] + " " + user['lastName']

users.sort(key=lambda x: x['Name'])

# Carregar o resultado enriquecido
df1 = pd.DataFrame(users)
df1.to_csv('./data/users_enriched.csv', index=False)