import random
import pandas as pd

# Создание DataFrame
lst = ['robot'] * 10
lst += ['human'] * 10
random.shuffle(lst)
data = pd.DataFrame({'whoAmI':lst})

# Создание нового столбца для каждого уникального значения в 'whoAmI'
for value in data['whoAmI'].unique():
   data[value] = (data['whoAmI'] == value).astype(int)

# Удаление столбца 'whoAmI'
data = data.drop('whoAmI', axis=1)

print(data.head())
