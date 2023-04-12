# Задача №63. Решение в группах
# 1. Изобразите отношение households к population с
# помощью точечного графика
# 2. Визуализировать longitude по отношения к
# median_house_value, используя линейный график
# 3. Представить гистограмму по housing_median_age
# 4. Изобразить гистограмму по median_house_value с
# оттенком housing_median_age

import seaborn as sns

import pandas as pd

df = pd.read_csv(
    'https://raw.githubusercontent.com/timothypesi/Data-Sets-For-Machine-Learning-/main/california_housing_train.csv')


sns.scatterplot(data=df, x='households', y='population')

sns.relplot(data=df, x='longitude', y='median_house_value', kind='line')

sns.histplot(data=df, x='housing_median_age')

sns.displot(data=df, x='median_house_value', hue='housing_median_age')
