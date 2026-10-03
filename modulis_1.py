import math

telpas_platums = float(input("Telpas platums, metros: "))
telpas_garums = float(input("Telpas garums, metros: "))
rulla_platums = float(input("Linoleja rulla platums, metros: "))
rulla_garums = float(input("Linoleja rulla garums, metros: "))
cena_par_rulli = float(input("Cena par 1 rulli, eiro: "))

def aprekinat_linoleja_izmaksas(cena_par_rulli, rulla_garums, rulla_platums, telpas_platums, telpas_garums):
    telpas_platums_noapalots = math.ceil(telpas_platums)
    telpas_garums_noapalots = math.ceil(telpas_garums)

    telpas_platiba = telpas_platums_noapalots * telpas_garums_noapalots
    rulla_platiba = rulla_garums * rulla_platums

    nepieciesamais_linolejs = telpas_platiba / rulla_platiba
    nepieciesamais_linolejs_noapalots = math.ceil(nepieciesamais_linolejs)

    kopejas_izmaksas = nepieciesamais_linolejs_noapalots * cena_par_rulli

    return round(kopejas_izmaksas, 2)

print(aprekinat_linoleja_izmaksas(cena_par_rulli, rulla_garums, rulla_platums, telpas_platums, telpas_garums))