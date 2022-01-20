import pandas as pd
from datetime import datetime
import lib_bamboo as bamboo
import os

................... #Deze regel nog invullen! Hoe maak je het scherm leeg?
print("Working...")

data = pd.read_excel("python/Voorbeeld_Divisie.xlsx")
data["datum"] = pd.to_datetime(data["datum"], format="%d/%m/%Y")
data = data.sort_values("datum")

#Informatievraag 1



#Informatievraag 2



#Informatievraag 3
zwartBoek = ....... #Deze regel nog invullen! Hoe maak je een top 5?
file3 = open("files/zwartboek.txt", "w", encoding="UTF-8")
file3.write(bamboo.prettify(zwartBoek, type="zwartboek"))
................... #Deze regel nog invullen! Hoe sluit je file3?


#Informatievraag 4









print("Done!")
