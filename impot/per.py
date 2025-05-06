def calcul_impots(revenus):
    p1 = 10777
    p2 = 27478
    p3 = 78570
    p4 = 168994
    
    t1 = 11/100
    t2 = 30/100
    t3 = 41/100
    t4 = 45/100
    
    i1 = 0
    i2 = 0
    i3 = 0
    i4 = 0
    
    tmi = 0
    
    if revenus <= p1:
        impots = 0
        tmi = 0
    if p1 < revenus <= p2:
        i1 = (revenus - p1)*t1
        impots = i1
        tmi = int(t1*100)
    if p2 < revenus <= p3:
        i1 = (p2 - p1)*t1
        i2 = (revenus - p2)*t2
        impots = i1 + i2
        tmi = int(t2*100)
    if p3 < revenus <= p4:
        i1 = (p2 - p1)*t1
        i2 = (p3 - p2)*t2
        i3 = (revenus - p3)*t3
        impots = i1 + i2 + i3
        tmi = int(t3*100)
    if revenus > p4:
        i1 = (p2 - p1)*t1
        i2 = (p3 - p2)*t2
        i3 = (p4 - p3)*t3
        i4 = (revenus - p4)*t4
        impots = i1 + i2 + i3 + i4
        tmi = int(t4*100)
        
    i1 = int(round(i1))
    i2 = int(round(i2))
    i3 = int(round(i3))
    i4 = int(round(i4))
    im = int(round(impots))
    
    output = {}
    output["i1"] = i1
    output["i2"] = i2
    output["i3"] = i3
    output["i4"] = i4
    output["im"] = im
    
    # print("Impots tranche   ", int(t1*100), "%    ", i1, '€')
    # print("Impots tranche   ", int(t2*100), "%    ", i2, '€')
    # print("Impots tranche   ", int(t3*100), "%    ", i3, '€')
    # print("Impots tranche   ", int(t4*100), "%    ", i4, '€')
    # print()
    # print("Impots           ", impots, '€')
    # print("TMI              ", tmi, "%")
    
    return output

revenus = 66e3 + 13e3
per     = 15000
plafond_per = 5300

impots = calcul_impots(revenus)
impots_per = calcul_impots(revenus-per)
eco = impots["im"] - impots_per["im"]
if eco > plafond_per:
    eco = plafond_per
    print("Plafond déduction fiscal PER dépassé")
    
print("Economies: ", int(eco), "€")
