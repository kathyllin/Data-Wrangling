import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

dados_tempo = pd.read_excel('(1.2) dataset_principal.xls')
dados_merge = pd.read_excel('(1.3) dataset_join.xls')

pd.set_option("display.max.columns", None)
#print(dados_tempo)

dados_tempo.columns

dados_tempo.head(n=5)

dados_tempo.tail(n=3)

#dados_tempo.info()

dados_tempo = dados_tempo.rename(columns={'Estudante': 'estudante',
                                          'Tempo para chegar à escola (minutos)':'tempo',
                                          'Distância percorrida até a escola (quilômetros)':'distancia',
                                          'Quantidade de semáforos': 'semaforos',
                                          'Período do dia': 'periodo',
                                          'Perfil ao volante': 'perfil'})

#dados_tempo.info()