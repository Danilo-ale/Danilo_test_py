"""
Esercizio su Pandas

Scenario: Una catena di ristoranti vuole analizzare le vendite giornaliere in diverse filiali.
Obiettivo: Utilizzare pandas per calcolare le vendite medie giornaliere per ogni filiale.
Dati: Il dataset contiene colonne "Data", "Filiale" e "Vendite".

Compiti:
Genera i dati da un file CSV.
Utilizza groupby() per raggruppare i dati per "Data" e "Filiale".
Calcola la media delle vendite giornaliere per filiale
Calcola quale filiale ha venduto di più
Salva tutti i valori e i risultati su un nuovo file(ES: csv).
"""
import pandas as pd

# Convertiamo il dizionario in un DataFrame
df = pd.read_csv("ESERCIZIO TEST VENERDI 19\\ristoranti.csv")

def group_df():
    #groupby su data e filiale
    df_ag = df.groupby(["Data", "Filiale"]).sum("Vendite")
    print(f"\n---Valori raggruppati:---\n{df_ag}")
    return df_ag
    

def media():
    #gruopuby su data e filiale calcolando la media vendite
    df_s=df.groupby(["Filiale","Data"]).mean("Vendite")
    print("Vendite medie:\n",df_s)
    return df_s

def m_filiale():
    #sommo le vendite per ristorante
    df_ag = df.groupby(["Filiale"]).sum("Vendite")
    df_m=df_ag.sort_values(by="Vendite")
    print(df_m.iloc[-1])        #ristorante con più vendite.
    return df_m

def salva_csv(df1,df2, df3):
    #concateno i df
    df_uniti = pd.concat([df1, df2,df3])
    df_uniti.to_csv("ESERCIZIO TEST VENERDI 19\\ristoranti_salvataggio.csv")

df1=group_df()
df2= media()
df3=m_filiale()
salva_csv(df1,df2,df3)