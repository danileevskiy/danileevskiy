obem= 1.44
stranicy= 100
stroki = 50
simvoly = 25
x = 4
simvoly_1= stroki * simvoly * stranicy
simvoly_obs= simvoly_1 * x
kb= obem * 1024 * 1024
knigi = int(kb // simvoly_obs)
print("Количество книг, помещающихся на дискету:", knigi)
