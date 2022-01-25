from numpy import average
import pandas as pd
from datetime import datetime
import lib_bamboo as bamboo
import os

os.system("cls") #Deze regel nog invullen! Hoe maak je het scherm leeg?
print("Working...")

data = pd.read_excel("A5-template-main/python/Basketbal_Promotiedivisie_tussenstand.xlsx")
data["datum"] = pd.to_datetime(data["datum"], format="%d/%m/%Y")
data = data.sort_values("datum")

#Informatievraag 1
totalFouls = data["overtredingen"].sum()
print(totalFouls)
file1 = open("A5-template-main/files/sum.txt" , "w" , encoding="UTF-8")
file1.write(f"{totalFouls}")
file1.close()

#Informatievraag 2
averageFouls = data["overtredingen"].mean().astype(int)
print(averageFouls)
averageFile = open("A5-template-main/files/average.txt", "w", encoding="UTF-8")
averageFile.write(f"{averageFouls}")
averageFile.close()

#Informatievraag 3
zwartBoek = data.sort_values("overtredingen" , ascending = False) #Deze regel nog invullen! Hoe maak je een top 5?
top5 = zwartBoek.head(5)
print(top5)
file3 = open("A5-template-main/files/zwartboek.txt", "w", encoding="UTF-8")
file3.write(bamboo.prettify(zwartBoek, type="zwartboek"))
file3.close() #Deze regel nog invullen! Hoe sluit je file3?


#Informatievraag 4









print("Done!")
