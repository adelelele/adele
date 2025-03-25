
transport_limit = input("ievadiet savu atļauto promiļu daudzumu:")  # Atļautās promiles (piemēram, 0.5‰)
gender = input("Ievadiet savu dzimumu(vīrietis, sieviete):")  # Lietotāja dzimums
weight = input("Ievadiet savu svaru(kg):")  # Lietotāja svars kg

elimination_rate = 0.12  # Vidēji 0.12‰ tiek sadalīts stundā

hours = 12  

if gender == "vīrietis":
    gender_coef = 0.7 
else: gender_coef = 0.6  



    # Maksimālās promiles, kas drīkst būt sākumā, lai pēc 12h būtu zem robežas

max_starting_promiles = transport_limit + (hours * elimination_rate)



    # Maksimālais alkohola daudzums gramos

max_alcohol_grams = max_starting_promiles * weight * gender_coef



    # Aprēķini dažādu dzērienu atļauto daudzumu

beer_ml = (max_alcohol_grams / (5 * 0.8)) * 100  
wine_ml = (max_alcohol_grams / (12 * 0.8)) * 100  
vodka_ml = (max_alcohol_grams / (40 * 0.8)) * 100  



return {

        "Alus (5%) ml": round(beer_ml, 1),

        "Vīns (12%) ml": round(wine_ml, 1),

        "Degvīns (40%) ml": round(vodka_ml, 1),

    }






#result = calculate_max_alcohol(transport_limit, gender, weight)

print("Cik alu drīksti dzert:", round(beer_ml(int),1))
print("Cik vīnu drīksti dzert:", round(wine_ml(int), 1))
print("Cik degv;inu drīksti dzert:", round(vodka_ml(int), 1))