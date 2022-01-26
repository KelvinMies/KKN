from zlib import DEFLATED
from numpy import average
import pandas as pd
from datetime import date, datetime
import lib_bamboo as bamboo
import os
from datetime import timedelta

os.system("cls") #Deze regel nog invullen! Hoe maak je het scherm leeg?
print("Working...")

data = pd.read_excel("A5-template-main/python/Basketbal_Promotiedivisie_tussenstand.xlsx")
data["datum"] = pd.to_datetime(data["datum"], format="%d/%m/%Y",)
data = data.sort_values("datum", ascending=False)

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
top5 = data.sort_values("overtredingen" , ascending = False) #Deze regel nog invullen! Hoe maak je een top 5?
top5 = top5.head(5)
print(top5)
file3 = open("A5-template-main/files/zwartboek.txt", "w", encoding="UTF-8")
file3.write(bamboo.prettify(top5, type="zwartboek"))
file3.close() #Deze regel nog invullen! Hoe sluit je file3?


#Informatievraag 4
ereNummer = 2
latestDate = data["datum"].max()
latestMin = latestDate - timedelta(days=14)
filter = (data["overtredingen"] < ereNummer)
data_filtered = data[filter]
filter = (data_filtered["datum"] >= latestMin)
data_filtered = data_filtered[filter]
print(data_filtered)
file4 = open("A5-template-main/files/eregalerij.txt", "w", encoding="UTF-8")
file4.write(bamboo.prettify(data_filtered, type="eregalerij"))
file4.close() 

















#Informatievraag 5
#data_pivoted = data.pivot_table(
 #index="scheidsrechter",
 #columns="datum",
 #values="overtredingen",
 #aggfunc=sum
#)
#print(data_pivoted)
#file5a = file1 = open("A5-template-main/files/pivot.txt" , "w" , encoding="UTF-8")


print("Done!")
