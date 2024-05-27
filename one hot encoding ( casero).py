import pandas as pd
from sklearn.preprocessing import OneHotEncoder, StandardScaler
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.linear_model import LogisticRegression
from itertools import chain

# Ejemplo de DataFrame con características mixtas
data = {
    'edad': [25, 32, 47, 51],
    'salario': [50000, 60000, 52000, 58000],
    'genero': ['M', 'F', 'F', 'M'],
    'departamento': ['HR', 'Engineering', 'Marketing', 'HR']
}
df = pd.DataFrame(data)

X = df
y = [0, 1, 0, 1]  # Variable objetivo



numeric_features = [feature for feature in df.columns if df[feature].dtype != 'O']
categorical_features = [feature for feature in df.columns if df[feature].dtype == 'O']

# print columns
#print('We have {} numerical features : {}'.format(len(numeric_features), numeric_features))
#print('\nWe have {} categorical features : {}'.format(len(categorical_features), categorical_features))
columnas_interes = categorical_features



valores_unicos=[]
for i in categorical_features:
    x=(df[i].unique()).tolist()
    valores_unicos.append(x)
    
    
#print(valores_unicos)


valores_unicos_planos = list(chain.from_iterable(valores_unicos))

#print(valores_unicos_planos)


for i in valores_unicos_planos:
    df[i]=0
    
    
total_filas=df.shape[0]

for i in range(total_filas):
    for c in columnas_interes:
        for m in valores_unicos_planos:
            if m == df.iloc[i][c]:
                df.at[i, m] = 1


print(df)
