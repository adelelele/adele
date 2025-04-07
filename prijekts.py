print("Dzer droši = brauc droši")
print("Ja skaitlī ir komats, tā vietā raksti punktu!")
print("Kad ievadi, spied ENTER")

transport_limit =float(input("ievadiet savu atļauto promiļu daudzumu vadot automašīnu:"))  # Atļautās promiles (piemēram, 0.5‰)
gender = input("Ievadiet savu dzimumu(ja vīrietis - v, ja sieviete - s):") # Lietotāja dzimums
weight = float(input("Ievadiet savu svaru(kg):"))  # Lietotāja svars kg
hours = float(input("Ievadiet pēc cik stundām jums ir jāvada automašīna:"))
elimination_rate = 0.12  # Vidēji 0.12‰ tiek sadalīts stundā

  

if gender == "v":
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
if beer_ml%500 < 400:
    if math.floor(beer_ml/500)==1:
        print("Šovakar drīksti izdzert ", beer_ml , "ml ar alu - ", math.floor(beer_ml/500), "0.5tilp aliņu")
    else:
        print("Šovakar drīksti izdzert ", beer_ml , "ml ar alu - ", math.floor(beer_ml/500), "0.5tilp aliņus")
else:
    if math.ceil(beer_ml/500)==1:
        print("Šovakar drīksti izdzert ", beer_ml , "ml ar alu - ", math.ceil(beer_ml/500), "0.5tilp aliņu")
    else:
        print("Šovakar drīksti izdzert ", beer_ml , "ml ar alu - ", math.ceil(beer_ml/500), "0.5tilp aliņus")
    

print("VAI")
if wine_ml%1000 >= 800:
    print("Šovakar drīksti izdzert ", wine_ml , "ml ar vīnu - ", math.ceil(wine_ml/1000), "vienlitrīgas pudeles ar vīnu")
else:
    print("Šovakar drīksti izdzert ", wine_ml , "ml ar vīnu - ", math.floor(wine_ml/1000), "vienlitrīgas pudeles ar vīnu")

print("VAI")
print("Šovakar drīksti izdzert ", vodka_ml , "ml ar degvīnu")
print("Degvīna daudzums kokteiļos:")

#asiņainā mērija - tajā izvanto 59ml ar šņabi
asin_merij_daudz = vodka_ml/59
if asin_merij_daudz%2>=0.5:
    asin_merij_daudz = math.ceil(asin_merij_daudz)
else:
    asin_merij_daudz = math.floor(asin_merij_daudz)
print("1) ", asin_merij_daudz, "Asiņainās Mērijas")

#Skrūvgriezis - 59 ml šņabja
print("2) ", asin_merij_daudz, "Skrūvjgriežus")

#Kosmopolitans - 74ml ar šņabi
kosmo_daudz = vodka_ml/74
if kosmo_daudz%2>=0.5:
    kosmo_daudz = math.ceil(kosmo_daudz)
else:
    kosmo_daudz = math.floor(kosmo_daudz)
print("3) ", kosmo_daudz, "Kosmopolitanus")

#Sea breeze - 44ml šņabis
sea_daudz = vodka_ml/44
if sea_daudz%2>=0.5:
    sea_daudz = math.ceil(sea_daudz)
else:
    sea_daudz = math.floor(sea_daudz)
print("4) ", sea_daudz, "Sea breeze kokteiļus")

#Gimlet - 60ml 
gimlet_daudz = vodka_ml/60
if gimlet_daudz%2>=0.5:
    gimlet_daudz = math.ceil(gimlet_daudz)
else:
    gimlet_daudz = math.floor(gimlet_daudz)
print("5) ", gimlet_daudz, "Gimlet kokteiļus")
