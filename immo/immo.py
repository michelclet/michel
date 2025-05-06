from immo_functions import simulation_resultat
from immo_functions import mensualite_resultat
from immo_functions import interet_resultat
from immo_functions import capital_resultat
from immo_functions import capacite_resultat

# simulation_resultat
revenus     = (110000+40000)*0.78/12+70/100*1000
credit      = 1000
prix        = 630000
notaire     = prix*7.1/100
taux        = 3.5
duree       = 25
apport      = 150000
assurance   = 70
# output      = simulation_resultat(prix, taux, duree, apport, assurance, revenus, credit, notaire)

# for key in output.keys():
#     print(key, output[key])

endettement = 34
output = capacite_resultat(taux, duree, apport, assurance, revenus, credit, endettement)

for key in output.keys():
    print(key, output[key])

# # Relais
# estimation      = 375000
# reste_credit    = 150000
# garde           = 50000

# relais          = 80/100*(estimation - garde)
# sup             = (estimation - garde) - relais

# taux_relais     = 1.32
# taux_sup        = 1.64
# mensualite  = mensualite_resultat(sup, taux_sup, duree)
# print(mensualite)