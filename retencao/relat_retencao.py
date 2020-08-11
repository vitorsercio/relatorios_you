import pandas as pd
import matplotlib as plt
import numpy as np
import datetime as dt

extracao=pd.read_csv('retencao.csv')
#convertendo datahora para apenas data
extracao.data_atendimento=pd.to_datetime(extracao.data_atendimento).dt.date

