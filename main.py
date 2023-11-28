# Задача 44: В ячейке ниже представлен код,
# генерирующий DataFrame, которая состоит всего из 1 столбца.
# Ваша задача перевести его в one hot вид.
# Сможете ли вы это сделать без get_dummies?
#
# import random
# lst = ['robot'] * 10
# lst += ['human'] * 10
# random.shuffle(lst)
# data = pd.DataFrame({'whoAmI':lst})
# data.head()

import random
import pandas as pd

# Создаем DataFrame
lst = ['robot'] * 10
lst += ['human'] * 10
random.shuffle(lst)
data = pd.DataFrame({'whoAmI': lst})

# Создаем новый столбец для каждого уникального значения в whoAmI
for value in data['whoAmI'].unique():
   data[value] = (data['whoAmI'] == value).astype(int)

# Удаляем столбец whoAmI
data = data.drop('whoAmI', axis=1)

print(data.head())
