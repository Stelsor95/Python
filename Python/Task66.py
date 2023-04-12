# Задача №67. Решение в группах
# 1. Создать новый столбец в таблице с
# пингвинами, который будет отвечать за
# показатель длины клюва пингвина.
# high - длинный(от 42)
# middle - средний(от 35 до 42)
# low - маленький(до 35)

import seaborn as sns

import pandas as pd

df = pd.read_csv(
    'https://raw.githubusercontent.com/timothypesi/Data-Sets-For-Machine-Learning-/main/california_housing_train.csv')

penguins = sns.load_dataset("penguins")
penguins.head()

penguins.loc[penguins.bill_length_mm >= 42, 'height_group'] = 'hight'
penguins.loc[(penguins.bill_length_mm > 35) & (
    penguins.bill_length_mm < 42), 'height_group'] = 'middle'
penguins.loc[penguins.bill_length_mm <= 35, 'height_group'] = 'low'
penguins.head()
