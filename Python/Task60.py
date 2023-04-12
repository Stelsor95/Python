# Задача №61. Решение в группах
# 1. Определить какое максимальное и минимальное
# значение median_house_value
# 2. Показать максимальное median_house_value, где
# median_income = 3.1250
# 3. Узнать какая максимальная population в зоне
# минимального значения median_house_value

import pandas as pd

df = pd.read_csv(
    'https://raw.githubusercontent.com/timothypesi/Data-Sets-For-Machine-Learning-/main/california_housing_train.csv')

df['median_house_value'].min(), df['median_house_value'].max()

df.describe()

df[df['median_income'] == 3.1250].median_house_value.max()

df[df['median_house_value'] == df.median_house_value.min()].population.max()
