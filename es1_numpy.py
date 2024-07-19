"""
Scenario: Un laboratorio scientifico registra le temperature ogni ora.
Obiettivo: Utilizzare numpy per calcolare la temperatura media,
 minima e massima registrata.
Dati: Un array numpy di temperature registrate in una giornata.

Determina la temperatura più probabile per le prossime 4 posizioni 
rispetto a un aumento costante di 0,2 gradi al giorno ogni settimana. 
"""

import numpy as np
#temp di un giorno. 24 ore-> 24 temp
temp = np.random.uniform(15, 30, 24)
temp=np.round(temp,1)
mas=np.max(temp)
min=np.min(temp)
media=np.mean(temp)

print("Temp massima:",mas,"\nTemp minima: ",min,"\nTemp media:",media)

#temperatura aumenta di 0,2 gradi/giorno
aumento_ora=0.2/24

#le prossime 4 temperature orarie partono dall'ultima temp[-1]
#array temp_pros da 1 a 4, calcolando l'aumento all'ora di temperature
temp_pros=np.arange(1,5)*aumento_ora
#sommo l'ultima temp all'array
temp_pros+=temp[-1]
print("Temperature l prossime 4 ore:", temp_pros)
