# Задача 40: Определить среднюю стоимость дома, где кол-во людей от 0 до 500 (population)

import pandas as pd

df = pd.read_csv('sample_data/california_housing_train.csv')

df[
    (df['population'] > 0) &
    (df['population'] < 500)
].median_house_value.mean()
