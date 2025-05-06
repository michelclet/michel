revenu_net_imposable = 2767.09

taux_reel = 9.9/100
taux_pacs = 15.0/100

impot_reel = round(taux_reel * revenu_net_imposable, 2)
impot_pacs = round(taux_pacs * revenu_net_imposable, 2)

remboursement = round(impot_pacs - impot_reel, 2)

print("Michel doit", remboursement, "€ à Fanny")
print()
print("Impots PACS, ", impot_pacs, "€")
print("Impots réel, ", impot_reel, "€")
