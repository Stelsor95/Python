# Задача №59. Решение в группах
# 1. Проверить есть ли в файле пустые значения
# 2. Показать median_house_value где median_income < 2
# 3. Показать данные в первых 2 столбцах
# 4. Выбрать данные где housing_median_age < 20 и
# median_house_value > 70000

import pandas as pd

df = pd.read_csv(
    'https://raw.githubusercontent.com/timothypesi/Data-Sets-For-Machine-Learning-/main/california_housing_train.csv')

df.isnull().sum()

df.loc[df['median_income'] < 2, 'median_house_value']

for col in df.columns[:2]:
    print(df[col])

df[(df['housing_median_age'] < 20) & (df['median_house_value'] > 70000)]
