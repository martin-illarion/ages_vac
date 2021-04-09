import requests;
import csv;

l_file="/home/ubuntu/ages_vac/ages_vac/timeline-eimpfpass.csv"
out_path="/home/ubuntu/ages_vac/ages_vac/"


url = 'https://info.gesundheitsministerium.gv.at/data/timeline-eimpfpass.csv'
req = requests.get(url, allow_redirects=True)

url_content = req.content
csv_file = open(l_file, 'wb')
#print(url_content)
csv_file.write(url_content)
csv_file.close()

bl=["Burgenland","Kärnten","Niederösterreich","Oberösterreich","Salzburg","Steiermark","Tirol","Vorarlberg","Wien","Österreich","KeineZuordnung"]


line={}
for b in bl:
    line[b]=[]

with open(l_file,"r", newline='',encoding="utf-8-sig") as csvfile:

    cov_reader = csv.DictReader(csvfile, delimiter=';')
    print(cov_reader)
    for row in cov_reader:
        #Datum;BundeslandID;Bevölkerung;Name;EingetrageneImpfungen;EingetrageneImpfungenPro100;Teilgeimpfte;TeilgeimpftePro100;Vollimmunisierte;VollimmunisiertePro100;Gruppe<24_M_1;Gruppe<24_W_1;Gruppe<24_D_1;Gruppe_25-34_M_1;Gruppe_25-34_W_1;Gruppe_25-34_D_1;Gruppe_35-44_M_1;Gruppe_35-44_W_1;Gruppe_35-44_D_1;Gruppe_45-54_M_1;Gruppe_45-54_W_1;Gruppe_45-54_D_1;Gruppe_55-64_M_1;Gruppe_55-64_W_1;Gruppe_55-64_D_1;Gruppe_65-74_M_1;Gruppe_65-74_W_1;Gruppe_65-74_D_1;Gruppe_75-84_M_1;Gruppe_75-84_W_1;Gruppe_75-84_D_1;Gruppe_>84_M_1;Gruppe_>84_W_1;Gruppe_>84_D_1;Gruppe<24_M_2;Gruppe<24_W_2;Gruppe<24_D_2;Gruppe_25-34_M_2;Gruppe_25-34_W_2;Gruppe_25-34_D_2;Gruppe_35-44_M_2;Gruppe_35-44_W_2;Gruppe_35-44_D_2;Gruppe_45-54_M_2;Gruppe_45-54_W_2;Gruppe_45-54_D_2;Gruppe_55-64_M_2;Gruppe_55-64_W_2;Gruppe_55-64_D_2;Gruppe_65-74_M_2;Gruppe_65-74_W_2;Gruppe_65-74_D_2;Gruppe_75-84_M_2;Gruppe_75-84_W_2;Gruppe_75-84_D_2;Gruppe_>84_M_2;Gruppe_>84_W_2;Gruppe_>84_D_2;EingetrageneImpfungenBioNTechPfizer_1;EingetrageneImpfungenModerna_1;EingetrageneImpfungenAstraZeneca_1;EingetrageneImpfungenBioNTechPfizer_2;EingetrageneImpfungenModerna_2;EingetrageneImpfungenAstraZeneca_2
        bundesland = row["Name"]
        #print(row["Gruppe<24_M_1"])
        datum = row["Datum"]
        #print(datum) Gruppe_<25_D_2
        ag01 = int(row["Gruppe_<25_M_1"])    + int(row["Gruppe_<25_W_1"]) + int(row["Gruppe_<25_D_1"])
        ag02 = int(row["Gruppe_25-34_M_1"]) + int(row["Gruppe_25-34_W_1"]) + int(row["Gruppe_25-34_D_1"])
        ag03 = int(row["Gruppe_35-44_M_1"]) + int(row["Gruppe_35-44_W_1"]) + int(row["Gruppe_35-44_D_1"])
        ag04 = int(row["Gruppe_45-54_M_1"]) + int(row["Gruppe_45-54_W_1"]) + int(row["Gruppe_45-54_D_1"])
        ag05 = int(row["Gruppe_55-64_M_1"]) + int(row["Gruppe_55-64_W_1"]) + int(row["Gruppe_55-64_D_1"])
        ag06 = int(row["Gruppe_65-74_M_1"]) + int(row["Gruppe_65-74_W_1"]) + int(row["Gruppe_65-74_D_1"])
        ag07 = int(row["Gruppe_75-84_M_1"]) + int(row["Gruppe_75-84_W_1"]) + int(row["Gruppe_75-84_D_1"])
        ag08 = int(row["Gruppe_>84_M_1"])   + int(row["Gruppe_>84_W_1"])   + int(row["Gruppe_>84_D_1"])
        #csv_outfile.seek(0)
        #if bundesland=="Österreich":
        newline = str(datum + "," + str(ag01) + "," +str(ag02) + "," +str(ag03) + "," +str(ag04) + "," +str(ag05) + "," +str(ag06) + "," +str(ag07) + "," +str(ag08) + "\n")
        line[bundesland].append(newline)
        #print(newline)
        #print(datum + "," + str(ag01) + "," +str(ag02) + "," +str(ag03) + "," +str(ag04) + "," +str(ag05) + "," +str(ag06) + "," +str(ag07) + "," +str(ag08) + "\n" )
        #csv_outfile.write(datum + "," + str(ag01) + "," +str(ag02) + "," +str(ag03) + "," +str(ag04) + "," +str(ag05) + "," +str(ag06) + "," +str(ag07) + "," +str(ag08) + "\n" )
    for b in bl:
        line[b].append("Datum,<24,25-34,35-44,45-54,55-64,65-74,75-84,>84\n")
for b in bl:
    with open(out_path + b + ".csv","w", encoding='utf-8') as csv_outfile:
        #print(out_path + b + ".csv")
        for l in reversed(line[b]):
            csv_outfile.write(l)
