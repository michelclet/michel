# Prorata pour les mois incompplets
n_heures_absence = 0
n_heures_absence_maj25 = 0
salaire_horaire_net = 10.5
n_heures_absence_total = n_heures_absence + n_heures_absence_maj25

# Nombre d'heures de base
n_heures_ref = 40*52/12
n_heures_ref_maj25 = 8*52/12

n_heures_ref_total = n_heures_ref + n_heures_ref_maj25
salaire_ref = salaire_horaire_net*n_heures_ref/2
salaire_ref_maj25 = salaire_horaire_net*n_heures_ref_maj25*1.25/2
salaire_ref_net = salaire_ref + salaire_ref_maj25

# Nombre d'heures réellement travaillées
n_heures_reel = n_heures_ref - n_heures_absence
n_heures_reel_maj25 = n_heures_ref_maj25 - n_heures_absence_maj25
salaire_reel = salaire_ref_net - salaire_ref_net*n_heures_absence_total/n_heures_ref_total

print("salaire réel", round(salaire_reel, 2), "€")
print("salaire de référence", round(salaire_ref_net, 2), "€")
print("Nombre d'heure pour la co-famille", round(n_heures_reel/2), "h")
print("Nombre d'heure majorée 25% pour la co-famille", round(n_heures_reel_maj25/2), "h")
print(2*52/12*1.5)
print("")
print("Total net perçu")
print(559.76 + 1137.5*3 + 10.5*30)
print("1/10e du total perçu")
print(round(10/100*4287, 2))