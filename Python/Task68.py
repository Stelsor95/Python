# Задача №69. Решение в группах
# 1. Изобразить гистограмму по flipper_length_mm
# с оттенком height_group. Сделать анализ

import seaborn as sns

import pandas as pd

df = pd.read_csv(
    'https://raw.githubusercontent.com/timothypesi/Data-Sets-For-Machine-Learning-/main/california_housing_train.csv')

penguins = sns.load_dataset("penguins")
penguins.head()

sns.displot(penguins, x='flipper_length_mm', hue='height_group')
