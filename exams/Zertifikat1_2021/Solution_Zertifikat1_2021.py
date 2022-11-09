# Nr 1

# a)
x = 11
y = 4
print(((x+y)/2)**2)

# b)
def mittel_quadriert(x,y):
    if x - y == 0:
        print('x und y sind gleich.')
        return 1
    else:
        return ((x+y)/2)**2

print(mittel_quadriert(-4,4))
print(mittel_quadriert(-1,7))

#c)
infiziert = 1
case = bool(infiziert)
type(case)
elemente = ['Luft','Wasser','Feuer']
elemente_neu = elemente + ['Erde']
weihnachtsgeschenke = {'Buecher': 2,'O-Saft':1.5, 'PS5': False, 'Kekse': ['Anzahl',5]}
weihnachtsgeschenke.get('Kekse')

#d)
str_out = ''
for i in range(1,8):
    n = 2**i
    str_out += str(n)
    print(str_out)
# alternatively with tip:
string_list = []
for i in range(1,8):
    n = 2**i
    string_list.append(str(n))
    print("".join(string_list))

# Nr 2

#########
# Erstellung der ipynb Datei nicht relevant für unseren Kurs!

import numpy as np
import pandas as pd

#a)
v = np.arange(2021,1897,-4)
ma_diag = np.vstack([np.diag([1.0 for _ in range(10)],k=1),[0 for _ in range(11)]])
rng = np.random.default_rng()
z = rng.normal(size=12)
ma_diag[:,0] = z
ma_flat = np.exp(ma_diag).reshape((132,1))
print(np.var(ma_flat))

#b)
df = pd.read_csv("/Users/lucaslinden/Pythonkurs/pythonkurs_2022/exams/Zertifikat1_2021/diamonds.csv",index_col=False)
print(df.head(10))
print('Der Datensatz besteht aus {} Zeilen und {} Spalten.'.format(df.shape[0],df.shape[1]))
np.unique(df.isna().values) # Datensatz hat keine fehlenden Werte
df.drop_duplicates(inplace=True)
df = df[(df.x != 0) & (df.y != 0) & (df.z != 0)]
df['Volume'] = df.x * df.y * df.z
print('{} Diamanten haben die Qualität Premium.'.format(len(df[df.cut == 'Premium'])))

#c)
best = df[df.clarity == 'IF']
import seaborn as sns
import matplotlib
matplotlib.use('Qt5Agg')
import matplotlib.pyplot as plt

sns.scatterplot(data=best,x='Volume',y='price')
plt.show()
sns.countplot(data=df,x='cut')
plt.show()

grouped_df = df[['color','price']].groupby('color').mean()
print('Die teuerste Farbe ist {}.'.format(grouped_df.price.idxmax()))

df_agg = df.groupby(['cut','color','clarity'])['Volume'].sum()
print('Das aggregierte Volumen ist {}'.format(df_agg['Fair']['D']['SI1']))
