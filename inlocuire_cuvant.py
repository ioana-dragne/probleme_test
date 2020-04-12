fraza = "Lorem Ipsum este pur si simplu o macheta pentru text a industriei tipografice. "
# fraza = input()
lista_de_inlocuit = [[17, 20, "cu siguranta"], [34, 40, "emblema"], [63, 77, "informatice"]]

for i in lista_de_inlocuit:
  fraza = fraza.replace(fraza[i[0]:i[1]], i[2])


# A doua varianta
# for i in lista_de_inlocuit:
#   fraza = fraza.replace(fraza[i[0]:(i[0]+len(i[2]))], i[2])


print(fraza)
