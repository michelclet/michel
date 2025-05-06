loyer           = 450
charges         = 50

loyer_an_impots = loyer*12

loyer_cc        = loyer + charges
loyer_an_cc     = loyer_cc*12

pret            = 1177*12
abattement      = .5

imposable       = loyer_an_impots*abattement

impot1          = imposable*13/100
impot2          = imposable*17.2/100
impots          = impot1 + impot2

charges_copro   = 130*12
charges         = impots + pret + charges_copro

# print('loyer annuel cc:     ', loyer_an_cc)
# print('impots:              ', round(impots))
# print('pret:                ', round(pret))
# print('charges copro:       ', round(charges_copro))
# print('charges totales:     ', round(charges_totales))
# print('loyer net:           ', round(loyer_net))

# print('charges:     ', round(charges))
# print('loyer:        ', round(gain))
# print('benefice:    ', round(benefice))

charges_sans_loc    = round(pret + charges_copro)
charges_avec_loc    = round(charges - loyer_an_cc)
gain                = charges_sans_loc - charges_avec_loc  

print('Charges sans loc %d€' % -charges_sans_loc)
print('Charges avec loc %d€' % -charges_avec_loc)
print('Gain             %d€' % gain)