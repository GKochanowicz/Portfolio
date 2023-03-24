print("Cześć, co chcesz zrobić?")
print("1. Oblicz NWW")
print("2. Oblicz NWD")

operacja = input()

if operacja == "1":
   cyfra1 = int (input("wpisz pierwszą cyfrę"))
   cyfra2 = int (input("wpisz drugą cyfrę"))
   NWW = cyfra1 * cyfra2
   while cyfra2 > 0:
      r= cyfra1 % cyfra2
      cyfra1 = cyfra2
      cyfra2 = r
   NWW = NWW / cyfra1
   print(" NWW wynosi",NWW)

elif  "2":
   cyfra3 = int (input("wpisz pierwszą cyfrę"))
   cyfra4 = int (input("wpisz drugą cyfrę"))
   while cyfra3 != cyfra4:
      if cyfra3 > cyfra4:
         cyfra3= cyfra3 - cyfra4
      else:
         cyfra4 = cyfra4 - cyfra3
   print("NWD wynosi", cyfra3)


   #print("NWW " + for