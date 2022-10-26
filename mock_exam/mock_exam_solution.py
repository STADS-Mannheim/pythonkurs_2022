# Nr 1a)
a = 3
b = 5
print((a-b)/(a+b))

# Nr 1b)
def berechnung(a,b):
    if a+b == 0:
        print('a+b muss ungleich 0 sein.')
        return None
    else:
        return (a-b)/(a+b)

input_1 = berechnung(0,0)
print(input_1)
input_2 = berechnung(1,2)
print(input_2)

# Nr 1c)
x = float(0)
x_float = isinstance(x,float)
farben = {"red": (255,0,0),
          "green": (0,255,0),
          "blue": (0,0,255)}
print(farben.get('green')) # or print(farben['green']))

# Nr 1d)
str_out = ''
for i in range(9):
    str_out += str(i+1)
    print(str_out)

# Nr 2a)
import numpy as np

v = np.arange(0,200,4)
m = np.identity(50) # Alternative: m = np.diag([1 for _ in range(50)]).reshape((50,50))
m[-1,-1] = np.nan
rng = np.random.default_rng()
normal_vector = rng.normal(size=50)
print(normal_vector)
z_exp = np.exp(normal_vector)
prod = np.matmul(z_exp,m)

# Nr 2b)
import pandas as pd
df = pd.read_csv("/Users/lucaslinden/Pythonkurs/pythonkurs_2022/mock_exam/pendler.csv",sep=';',thousands='.')
print(df.head())
print('Der Datensatz besteht aus {} Zeilen und {} Spalten.'.format(len(df.index),len(df.columns)))
df_new = df.drop(columns=['Gemeindekennziffer'])
df_new.set_index('Name',inplace=True)
df_new['Nettopendler'] = df_new.Einpendler - df_new.Auspendler
pendler = df_new.sort_values(by='Nettopendler',ascending=False).head()['Nettopendler']
print(pendler)
print('Die höchste Quote hat Stuttgart.')
print('Mannheim hat {} viele Pendler.'.format(pendler['Mannheim, Universitätsstadt']))

# Nr 2c
df_new['Einpendlerquote'] = df_new.Einpendler / df_new.Erwerbstaetige_am_Arbeitsort
pendler_corr = df_new.Erwerbstaetige_am_Arbeitsort.corr(df_new.Einpendlerquote)
print(pendler_corr)
max_stadt = df_new[df_new.Erwerbstaetige_am_Arbeitsort > 10000].Einpendlerquote.idxmax()
print('Die höchste Einpendlerquote mit {} % hat {}.'.format(round(df_new.loc[max_stadt,'Einpendlerquote'],2)*100,max_stadt.split(',')[0]))

# Nr 2d
import matplotlib
matplotlib.use('Qt5Agg')
import matplotlib.pyplot as plt

fig,ax= plt.subplots()
ax.scatter(df_new.Einpendler,df_new.Auspendler)
ax.set_xlabel('Einpendler')
ax.set_ylabel('Auspendler')
plt.show()

