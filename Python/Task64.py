# Задача №65. Решение в группах
# Написать EDA для датасета про пингвинов
# Необходимо:
# ● Использовать 2-3 точечных графика
# ● Применить доп измерение в точечных графиках, используя
#     аргументы hue, size, stile
# ● Использовать PairGrid с типом графика на ваш выбор
# ● Изобразить Heatmap
# ● Использовать 2-3 гистограммы

import seaborn as sns

import pandas as pd

df = pd.read_csv(
    'https://raw.githubusercontent.com/timothypesi/Data-Sets-For-Machine-Learning-/main/california_housing_train.csv')

penguins = sns.load_dataset("penguins")
penguins.head()

sns.scatterplot(data=penguins, x='bill_length_mm',
                y='bill_depth_mm', hue='sex', size=5)

sns.scatterplot(data=penguins, x='body_mass_g',
                y='flipper_length_mm', hue='sex', style='island')

sns.scatterplot(data=penguins, x='bill_length_mm',
                y='flipper_length_mm', hue='body_mass_g', style='island', size=5)

list_p = ['bill_length_mm',	'bill_depth_mm',
          'flipper_length_mm',	'body_mass_g',	'sex']
pg = sns.PairGrid(penguins[list_p])
pg.map(sns.scatterplot)

sns.histplot(data=penguins, x='bill_length_mm')

sns.histplot(data=penguins, x='body_mass_g')

sns.histplot(data=penguins, x='flipper_length_mm')

test = penguins.head(3).pivot('bill_length_mm',	'bill_depth_mm', 'body_mass_g')
sns.heatmap(test, annot=True)
