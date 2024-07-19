"""
Scenario: Un laboratorio scientifico registra le temperature ogni ora.
Obiettivo: Utilizzare numpy per calcolare la temperatura media,
 minima e massima registrata.
Dati: Un array numpy di temperature registrate in una giornata.
"""

import numpy as np
temp=np.array([10,20,30,-3,0,12,13,22])

mas=np.max(temp)
min=np.min(temp)
media=np.mean(temp)

print("Temp massima:",mas,"\nTemp minima: ",min,"\nTemp media:",media)