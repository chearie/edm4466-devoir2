# coding : utf-8
# Ariane Chevrier, UQAM 2020

import json, csv
import requests

fichier = "lobbying-climat.csv"
fichier = "lobbying-climat-JHR.csv"

url = "http://jhroy.ca/uqam/lobby.json"

req = requests.get(url)

#if req.status_code == 200:
#     # print("OK")
#     test = req.json()
#     # print(test["registre"])

# if req.status_code != 200:
#     print("Nope!")

# else:
#     lobb = req.json()
#     print(lobb["registre"][0][0]["comlog_id"])
#     print(lobb["registre"][0][0]["fr_client_org_corp_nm"])
#     print(lobb["registre"][0][0]["en_client_org_corp_nm"])
#     print(lobb["registre"][0][1][1]["objet"])
#     print(lobb["registre"][0][1][1]["objet_autre"])
#     print(lobb["registre"][0][2][0]["institution"])

# nombres = list(range(0,72000))
# n = 0

# for nombre in nombres:
#     n += 1
#     infos = []

# if req.status_code != 200:
#         print("Nope")
# else:
#     lobb = req.json()
#     print(lobb["registre"][0][0]["comlog_id"])
#     print(lobb["registre"][0][0]["fr_client_org_corp_nm"])
#     print(lobb["registre"][0][0]["en_client_org_corp_nm"])
#     print(lobb["registre"][0][1][1]["objet"])
#     print(lobb["registre"][0][1][1]["objet_autre"])
#     print(lobb["registre"][0][2][0]["institution"])
    # print(len(lobb["registre"]))

lobby = req.json()

ntest = 0
n = 0
for chacun in lobby["registre"]:
        info = []
        ntest += 1
        code = chacun[0]["client_org_corp_num"]
        nomFr = chacun[0]["fr_client_org_corp_nm"]
        nomEn = chacun[0]["en_client_org_corp_nm"]
        date = chacun[0]["date_comm"]
        objet1 = chacun[1][0]["objet"] ### SUPER SCRIPT! SAUF QUE... IL PEUT Y AVOIR PLUSIEURS SUJETS DE LOBBYING À VÉRIFIER, OR ICI TU N'EN VÉRIFIE QU'UN SEUL, LE PREMIER
        objet2 = chacun[1][0]["objet_autre"]
        institution = chacun[2][0]["institution"]

        info.append(code)
        info.append(nomFr)
        info.append(nomEn)
        info.append(date)
        info.append(objet1)
        info.append(objet2)
        info.append(institution)

        # if objet1 or objet2 != "limat":
        #         print("NOON")
        # else:
        #         print("OUI")

        if "limat" in objet1 or "limat" in objet2:
                infoFin = []
                n += 1
                infoFin.append(code)
                infoFin.append(nomFr)
                infoFin.append(nomEn)
                infoFin.append(date)
                infoFin.append(objet1)
                infoFin.append(objet2)
                infoFin.append(institution)

                print(n, infoFin)

                bonCop = open(fichier, "a")
                badCop = csv.writer(bonCop)
                badCop.writerow(infoFin)