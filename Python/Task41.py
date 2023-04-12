# Задача 42: Узнать какая максимальная households в зоне минимального значения population

import pandas as pd

df = pd.read_csv('sample_data/california_housing_train.csv')

min_population = df.population.min()
df[
    df['population'] == min_population
].households.max()
