"""Scenario: Una azienda vuole analizzare la performance giornaliera
 delle vendite e delle ore lavorative dei suoi dipendenti per ottimizzare le operazioni.
Obiettivo: Utilizzare Pandas e Numpy per calcolare le vendite medie
 per ora lavorativa e identificare giorni di alta e bassa efficienza.

Compiti:
Generazione dei Dati:
Utilizza numpy per generare un array di date per 30 giorni.
Genera dati casuali per "Vendite" e "Ore Lavorative" utilizzando numpy per ciascun giorno.
Crea un DataFrame pandas con colonne "Data", "Vendite", "Ore Lavorative".
Analisi delle Vendite:
Calcola le vendite medie per ora lavorativa per ogni giorno.
Identifica i giorni con la massima e la minima
Salva tutti i valori e i risultati su un nuovo file(ES: csv)."""


import pandas as pd
import numpy as np
from random import randint
from datetime import date


#ricavo la data di oggi in modo dinamico con la libreria
oggi=date.today()

#genero array data
date = np.arange(np.datetime64(oggi), np.datetime64(oggi) + 30)
vendite=[]
ore_lavorative=[]

#riempio gli array casualmente
for i in range(0,30):
    v_casuali=randint(0,100)
    vendite.append(v_casuali)
    ore_lavoro=randint(1,30)
    ore_lavorative.append(ore_lavoro)


dati={"Data":date,
      "Vendite":vendite,
      "Ore Lavorative":ore_lavorative
}

df=pd.DataFrame(dati)
print(df)

#creo nuova colonna vendite/ora
def vendite_ora():
    df["Vendite/Ora"]=df["Vendite"]/df["Ore Lavorative"]
    df["Vendite/Ora"]=round(df["Vendite/Ora"],1)
    print(df)


def max_min_vend():
    #sommo prima le vendite per ogni giorno, poi faccio sort_values()
    df_v=df.groupby("Data").sum("Vendite")
    df_s=df_v.sort_values(by="Vendite")
    print(f"Giorno con meno vendite:\n{df_s.iloc[1]}\n\nGiorno con più vendite:\n{df_s.iloc[-1]}")
    return df_s

def scrivi_csv(df1,df2):
    #concateno i df e scrivo sul csv
    df_uniti = pd.concat([df1, df2])
    df_uniti.to_csv("ESERCIZIO TEST VENERDI 19\\lavoro_salvataggio.csv")



#richiamo funzione
vendite_ora()
max_min_df=max_min_vend()
scrivi_csv(df,max_min_df)