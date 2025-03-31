
transport_limit =float(input("ievadiet savu atļauto promiļu daudzumu:"))  # Atļautās promiles (piemēram, 0.5‰)
if transport_limit == 0.0:
    print("Galīgi traks esi? Tu nedrīksti necik dzert!")
gender = input("Ievadiet savu dzimumu(vīrietis, sieviete):") # Lietotāja dzimums
weight = float(input("Ievadiet savu svaru(kg):"))  # Lietotāja svars kg

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





#"Alus (5%) ml": round(beer_ml, 1),  "Vīns (12%) ml": round(wine_ml, 1),  "Degvīns (40%) ml": round(vodka_ml, 1),

    





import math
#result = calculate_max_alcohol(transport_limit, gender, weight)
if wine_ml%2>=0.5:
    wine_ml=math.ceil(wine_ml)
else:
    wine_ml=math.floor(wine_ml)
if beer_ml%2>=0.5:
    beer_ml=math.ceil(beer_ml)
else:
    beer_ml=math.floor(beer_ml)
if vodka_ml%2>=0.5:
    vodka_ml=math.ceil(vodka_ml)
else:
    vodka_ml=math.floor(vodka_ml)
print("Šovakar drīksti izdzert ", beer_ml , "ml ar alu")
print("Šovakar drīksti izdzert ", wine_ml , "ml ar vīnu")
print("Šovakar drīksti izdzert ", vodka_ml , "ml ar degvīnu")

#asiņainā mērija - tajā izvanto 59ml ar šņabi
asin_merij_daudz = vodka_ml/59
if asin_merij_daudz%2>=0.5:
    asin_merij_daudz = math.ceil(asin_merij_daudz)
else:
    asin_merij_daudz = math.floor(asin_merij_daudz)
print(asin_merij_daudz)