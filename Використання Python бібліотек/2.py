import pandas as pd
import matplotlib.pyplot as plt

try:
    fixed_df = pd.read_csv('comptagevelo20162.csv', sep=',', parse_dates=['Date'], dayfirst=True, index_col='Date')
except Exception as err:
    print(err)
    fixed_df = pd.DataFrame()


if 'Unnamed: 1' in fixed_df.columns:
    fixed_df = fixed_df.drop(['Unnamed: 1'], axis=1)

#Відображення графіка
plt.style.use('ggplot')
plt.rcParams['figure.figsize'] = (15, 10)

fixed_df.plot(figsize=(15, 10))
plt.show()

#Визначення найпопулярнішого місяця
most_popular_month = fixed_df.groupby(pd.Grouper(freq='M')).sum().sum(axis=1).idxmax().month_name()
max_count = fixed_df.groupby(pd.Grouper(freq='M')).sum().sum(axis=1).max()

print('Найбільш популярний місяць у велосипедистів:', end=' ')
print(f"{most_popular_month} {max_count}")