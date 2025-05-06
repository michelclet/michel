def tritri(total, avance_fanny_5050):
    """
    total :     dépensé dans le tritri
    equilibre : ce que Michel doit à Fanny en répartition 50/50
    """
    taux_mc = 55/100
    taux_fg = 1 - taux_mc
    mc_total = taux_mc*total
    fg_total = taux_fg*total
    mc_50_50 = total/2 - avance_fanny_5050
    fg_50_50 = total/2 + avance_fanny_5050
    mc2fg = round(mc_total - mc_50_50, 2)

    print()
    print("--- Tritri ---")
    print(f"Répartition {int(taux_mc*100)}/{100 - int(taux_mc*100)}")
    if mc2fg > 0:
        print('Minou doit', abs(int(round(mc2fg))), '€ à Fafa')
    elif mc2fg < 0:
        print('Fafa doit', abs(int(round(mc2fg))), '€ à Minou')
    elif mc2fg == 0:
        print('Les comptes sont parfaitement équilibrés')
    print()
    print("--- Détails ---")
    print('Total du tritri', total, '€')

    print()
    print('Payé')
    print('Fafa', round(fg_50_50,2), '€')
    print('Minou', round(mc_50_50,2), '€')

    print()
    print('Réel payé après régul')
    print('Fafa', round(fg_total, 2), '€')
    print('Minou', round(mc_total, 2), '€')

    print()


total = 943.70
avance_fanny_5050 = -92.78

tritri(total=total, avance_fanny_5050=avance_fanny_5050)
75