# Summēt skaitļus no 1 līdz 100.

summma=0
skaitlis=1

while skaitlis<=100:
    summma+=skaitlis # summma=summma+skaitlis, kļūda1 jo nebija pielikts +
    skaitlis+=1 # kļūda2 jo nebija pielikts +

print("Summa no 1 līdz 100 ir:summma}")
