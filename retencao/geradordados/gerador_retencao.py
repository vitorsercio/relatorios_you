import datetime as dt
import random as rdm
import csv

def rdmdata():
    inicio,fim=dt.datetime(2020,8,1),dt.datetime(2020,8,7,23,59,59)
    delta=(fim-inicio).total_seconds()
    rdelta=rdm.randrange(delta)
    rdate=inicio+dt.timedelta(seconds=rdelta)
    return(rdate)

nomes=open("nomes.apagar").read().split('\n')
nomes.pop()
motivos=['migracao indevida','problema cobranca','contencao de despesa','mudanca CEP','insatis. Dados','insatis. Voz','A.N.R.']
tipos=['Desconto','Dados adc.','priorizacao tratamento','readequacao de plano','Troca titularidade']
resultados=['retido','migrado','cancelado']
logins=['T35678'+'%02d'%(x) for x in range(70)]
loginsnomes=dict(zip(logins,nomes))
cursor = csv.writer(open('retencao.csv','w'))
cursor.writerow(('data_atendimento','protocolo','gsm','matricula','motivo_solicitacao','tipo_retencao','resultado'))
for i in range(100000):
    data=rdmdata()
    protocolo='2020123'+'%06d'%(i)
    gsm='11981'+'%06d'%(i)
    matricula=rdm.choice(logins)
    motivo=rdm.choice(motivos)
    if(motivo=='A.N.R.'):
        tipo=resultado=motivo
    else:
        tipo=rdm.choice(tipos)
        resultado=rdm.choice(resultados)
    cursor.writerow((data,protocolo,gsm,matricula,motivo,tipo,resultado))

