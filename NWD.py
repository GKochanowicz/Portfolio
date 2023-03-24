cyfra3 = int (input("wpisz pierwszą cyfrę"))
cyfra4 = int (input("wpisz drugą cyfrę"))
while cyfra3 != cyfra4:
      if cyfra3 > cyfra4:
         cyfra3= cyfra3 - cyfra4
      else:
         cyfra4 = cyfra4 - cyfra3
print("NWD wynosi", cyfra3)