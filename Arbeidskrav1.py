# %%
# -*- coding: utf-8 -*-
"""
Sammenligning av de årlige totalkostnadene for elbil og for bensinbil.
Av Yulia Martyushenko, (yumar9609@usn.no) 

"""

#%% Informasjon som programmet skal baseres på

S  = 12000 # antall kjørte km/år ut fra din typiske bilbruk
FE = 5000 # forsikring: elbil: 5000 kr/år
FB = 7500 # forsikring: bensinbil: 7500 kr/år
TF = 8.38 # Trafikkforsikringsavgift: 8,38 kr/dag for både elbil og bensinbil
AA = 365  # antall dager i et vanlig år
DE = 0.2  # drivstoffbruk elbil: 0,2 kWh/km. 
SP = 2.00 # strømpris (antar kun hjemmelading): 2.00 kr/kWh. 
DB = 1.0  # drivstoffbruk bensinbil: 1,0 kr/km.
BE = 0.1  # bomavgift elbil: 0,1 kr/km. 
BB = 0.3  # bomavgift bensinbil: 0,3 kr/km.

#%% Felles for både elbil og bensinbil

TFF = TF * AA  # trafikkforsikringsavgift årlig for både elbil og bensinbil

#%% Utregning av årlige kostnadene spesifik ved elbil

DDE = DE * S   # drivstoffbruk elbil for antall kjørte km/år 
SPE = DDE * SP # strømpris per år
BEE = BE * S  # bomavgift per år

#%% Utregning av årlige kostnadene spesifik ved bensinbil

DDB = DB * S  # drivstofpris per år 
BBB = BB * S  # bomavgift per år 

#%% Total kostnadene for elbil og bensinbl uten kostnader som renter på billån og verditap 

TOE = FE + TFF + SPE + BEE
TOB = FB + TFF + DDB + BBB

#%% Utskrift

print  ("\n Årlige kostnadene ved elbil sammenliknet med bensinbil ")
print  ("----------------------------------------------------------")
print("!\t\t\t\t\t\t\t!\t elbil\t\t! bensinbil\t!")
print ("!\ttrafikkforsikringsavgift!\t", f"{round(TFF,1):<10}","!", f"{round(TFF,1):<10}", "!")
print ("!\tdrivstofpris per år\t\t!\t", f"{round(SPE,1):<10}","!", f"{round(DDB,1):<10}", "!")
print ("!\tbomavgift per år \t\t!\t", f"{round(BEE,1):<10}","!", f"{round(BBB,1):<10}", "!")
print  ("----------------------------------------------------------")
print  ("Totale kostnadene \n(uten kostnader som renter\n på billån og verditap):\t!\t ", f"{round(TOE,1):<10}","!",  f"{round(TOB,1):<10}", "!")
print  ("----------------------------------------------------------")
        
