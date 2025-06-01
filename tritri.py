def tritri(total, avance_fanny_5050, taux_michel=55/100, arrondi=True):
    """
    total :     dépensé dans le tritri
    equilibre : ce que Michel doit à Fanny en répartition 50/50
    """
    
    taux_fg = 1 - taux_michel
    mc_total = taux_michel*total
    fg_total = taux_fg*total
    mc_50_50 = total/2 - avance_fanny_5050
    fg_50_50 = total/2 + avance_fanny_5050
    mc2fg = round(mc_total - mc_50_50, 2)

    print()
    print("--- Tritri ---")
    message = ""
    if mc2fg > 0:
        message = f'Minou doit {abs(int(round(mc2fg)))} € à Fafa'
    elif mc2fg < 0:
        message = f'Fafa doit {abs(int(round(mc2fg)))} € à Minou'
    elif mc2fg == 0:
        message = 'Les comptes sont parfaitement équilibrés'
    message += f" (Répartition {int(taux_michel*100)}/{100 - int(taux_michel*100)})"

    if arrondi:
        digits = 0
    else:
        digits = 2
    print(message)
    print()
    print("--- Détails ---")
    print('Total payé', round(total, digits), '€')
    print('Avance Fafa', round(fg_50_50,digits), '€')
    print('Avance Minou', round(mc_50_50,digits), '€')
    print()
    print('Après régul Fafa', round(fg_total, digits), '€')
    print('Après régul Minou', round(mc_total, digits), '€')

    print()


total = 339
avance_fanny_5050 = 81

tritri(total=total, avance_fanny_5050=avance_fanny_5050)