cnp = input()
ref = '279146358279'

cifra_ctr = sum([int(cnp[i]) * int(ref[i]) for i in range(len(ref))]) % 11

if cifra_ctr == 10:
  cifra_ctr = 1

if (len(cnp) == 13
    and int(cnp[0]) in range (1, 10)  
    and int(cnp[1:3] in [str(x).zfill(2) for x in range(0, 100)])   # anul
    and int(cnp[3:5] in [str(x).zfill(2) for x in range(0, 13)])    # luna
    and int(cnp[5:7] in [str(x).zfill(2) for x in range(0, 32)])    # ziua
    and int(cnp[7:9] in [str(x).zfill(2) for x in range(0, 53)])    # judetul
    and int(cnp[9:12] in [str(x).zfill(3) for x in range(0, 1000)])
    and int(cnp[12]) == cifra_ctr):
  if ((int(cnp[3:5]) in [1, 3, 5, 7, 8, 10, 12] and int(cnp[5:7]) < 32)
      or 
      (int(cnp[3:5]) in [4, 6, 9, 11] and int(cnp[5:7]) < 31)
      or
      (int(cnp[3:5]) == 2 and int(cnp[5:7]) < 30)):
    print("CNP valid")
  else:
    print("CNP invalid")
