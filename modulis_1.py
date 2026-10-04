import math

telpas_platums = float(input("Telpas platums, metros: "))
telpas_garums = float(input("Telpas garums, metros: "))
laminata_plaksnes_platums = float(input("Lamināta plāksnes platums, metros: "))
laminata_plaksnes_garums = float(input("Lamināta plāksnes garums, metros: "))
cena_par_plaksni = float(input("Cena par 1 plāksni, eiro: "))

def laminata_izmaksas(cena_par_plaksni, laminata_plaksnes_garums, laminata_plaksnes_platums, telpas_platums, telpas_garums):
    
    telpas_platiba = telpas_platums * telpas_garums
    plaksnes_platiba = laminata_plaksnes_garums * laminata_plaksnes_platums

    telpas_platiba_noapalots = math.ceil(telpas_platiba)

    nepieciesamais_laminats = telpas_platiba_noapalots / plaksnes_platiba

    kopejas_izmaksas = nepieciesamais_laminats * cena_par_plaksni

    return round(kopejas_izmaksas, 2)

print("Kopējā cena: " + str(laminata_izmaksas(cena_par_plaksni, laminata_plaksnes_garums, laminata_plaksnes_platums, telpas_platums, telpas_garums)) + " eiro.")