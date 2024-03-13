import pandas as pd

data = pd.read_csv(
    "data\Sleep_health.csv",
    index_col = 'Person ID'
    )
# print(data.head())
# print(data.info())
# print(data.describe())

'''Analisis de edades'''
# print(data['Gender'].value_counts())

data.loc[data['Age'] <= 40, 'Age_group'] = 'Adult'
data.loc[data['Age'] >= 41, 'Age_group'] = 'Older adult'

# print(data.head())
# print(data.tail())

# print(data['Age_group'].value_counts())
# print(data.groupby('Gender')['Age'].agg(['mean', 'std']))

'''Analisis de Ocupaciones'''
# print(data.groupby('Occupation')['Gender'].value_counts())
# print(data['Sleep Duration'].min(), data['Sleep Duration'].max())

# print(data.groupby('Gender')[['Sleep Duration', 'Quality of Sleep']].mean())
# occ_qua = data.groupby('Occupation')[['Sleep Duration', 'Quality of Sleep']].mean()
# print(occ_qua.sort_values(by='Quality of Sleep'))

# occ_bmi = data.groupby('Occupation')['BMI Category'].value_counts()
# print(occ_bmi.sort_values())

'''Analisis Actividad Fisica'''
# occ_act = data.groupby('Occupation')[['Daily Steps', 'Physical Activity Level', 'Sleep Duration', 'Quality of Sleep']].mean()
# print(occ_act.sort_values(by='Daily Steps'))
