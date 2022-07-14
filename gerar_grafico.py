import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import sys

file = sys.argv[1]

#Lendo arquivo CSV
df = pd.read_csv(file,sep=';',header=0)
#Pegando todas colunas para o Eixo Y
colunas=np.delete(np.array(df.columns),0,0)

#criando o Eixo X (timeline)
x=np.array(df['tempo'])

#plotando todas as linhas do eixo Y
for c in colunas:
  plt.plot(x,np.array(df[c]),label=f'{c}')

#configurações de layout do gráfico
plt.xticks(rotation = 45)
plt.ylabel('Média')
plt.title('Média por minuto')
plt.grid(True)
plt.legend()

#Salvando o gráfico em um arquivo PNG
plt.savefig('test.png')
