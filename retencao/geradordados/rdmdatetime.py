import datetime as dt
import random as rdm

def rdmdata():
    inicio,fim=dt.datetime(2020,8,1),dt.datetime(2020,8,7,23,59,59)
    delta=(fim-inicio).total_seconds()
    rdelta=rdm.randrange(delta)
    rdate=inicio+dt.timedelta(seconds=rdelta)
    return(rdate)
