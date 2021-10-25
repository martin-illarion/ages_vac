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

#translate{"Burgenland"="Bgl","Kärnten"="Ktn","Niederösterreich"="Noe","Oberösterreich","Salzburg","Steiermark","Tirol","Vorarlberg","Wien","Österreich","KeineZuordnung"}

line_2={}
line={}
line_g={}
for b in bl:
    line[b]=[]
    line_2[b]=[]
    line_g[b]=[]

with open(l_file,"r", newline='',encoding="utf-8-sig") as csvfile:

    cov_reader = csv.DictReader(csvfile, delimiter=';')
    print(cov_reader)
    for row in cov_reader:
        #Datum;BundeslandID;Bevölkerung;Name;EingetrageneImpfungen;EingetrageneImpfungenPro100;Teilgeimpfte;TeilgeimpftePro100;Vollimmunisierte;VollimmunisiertePro100;Gruppe_<15_M_1;Gruppe_<15_W_1;Gruppe_<15_D_1;Gruppe_15-24_M_1;Gruppe_15-24_W_1;Gruppe_15-24_D_1;Gruppe_25-34_M_1;Gruppe_25-34_W_1;Gruppe_25-34_D_1;Gruppe_35-44_M_1;Gruppe_35-44_W_1;Gruppe_35-44_D_1;Gruppe_45-54_M_1;Gruppe_45-54_W_1;Gruppe_45-54_D_1;Gruppe_55-64_M_1;Gruppe_55-64_W_1;Gruppe_55-64_D_1;Gruppe_65-74_M_1;Gruppe_65-74_W_1;Gruppe_65-74_D_1;Gruppe_75-84_M_1;Gruppe_75-84_W_1;Gruppe_75-84_D_1;Gruppe_>84_M_1;Gruppe_>84_W_1;Gruppe_>84_D_1;Gruppe_<15_M_2;Gruppe_<15_W_2;Gruppe_<15_D_2;Gruppe_15-24_M_2;Gruppe_15-24_W_2;Gruppe_15-24_D_2;Gruppe_25-34_M_2;Gruppe_25-34_W_2;Gruppe_25-34_D_2;Gruppe_35-44_M_2;Gruppe_35-44_W_2;Gruppe_35-44_D_2;Gruppe_45-54_M_2;Gruppe_45-54_W_2;Gruppe_45-54_D_2;Gruppe_55-64_M_2;Gruppe_55-64_W_2;Gruppe_55-64_D_2;Gruppe_65-74_M_2;Gruppe_65-74_W_2;Gruppe_65-74_D_2;Gruppe_75-84_M_2;Gruppe_75-84_W_2;Gruppe_75-84_D_2;Gruppe_>84_M_2;Gruppe_>84_W_2;Gruppe_>84_D_2;Gruppe_NichtZuordenbar;EingetrageneImpfungenBioNTechPfizer_1;EingetrageneImpfungenModerna_1;EingetrageneImpfungenAstraZeneca_1;EingetrageneImpfungenBioNTechPfizer_2;EingetrageneImpfungenModerna_2;EingetrageneImpfungenAstraZeneca_2;EingetrageneImpfungenJanssen;ImpfstoffNichtZugeordnet_1;ImpfstoffNichtZugeordnet_2
        bundesland = row["Name"]
        #print(row["Gruppe<24_M_1"])
        datum = row["Datum"]
        #print(datum) Gruppe_<25_D_2
        ag00 = int(row["Gruppe_<15_M_1"]) + int(row["Gruppe_<15_W_1"]) + int(row["Gruppe_<15_D_1"])
        ag01 = int(row["Gruppe_15-24_M_1"]) + int(row["Gruppe_15-24_W_1"]) + int(row["Gruppe_15-24_D_1"])
        ag02 = int(row["Gruppe_25-34_M_1"]) + int(row["Gruppe_25-34_W_1"]) + int(row["Gruppe_25-34_D_1"])
        ag03 = int(row["Gruppe_35-44_M_1"]) + int(row["Gruppe_35-44_W_1"]) + int(row["Gruppe_35-44_D_1"])
        ag04 = int(row["Gruppe_45-54_M_1"]) + int(row["Gruppe_45-54_W_1"]) + int(row["Gruppe_45-54_D_1"])
        ag05 = int(row["Gruppe_55-64_M_1"]) + int(row["Gruppe_55-64_W_1"]) + int(row["Gruppe_55-64_D_1"])
        ag06 = int(row["Gruppe_65-74_M_1"]) + int(row["Gruppe_65-74_W_1"]) + int(row["Gruppe_65-74_D_1"])
        ag07 = int(row["Gruppe_75-84_M_1"]) + int(row["Gruppe_75-84_W_1"]) + int(row["Gruppe_75-84_D_1"])
        ag08 = int(row["Gruppe_>84_M_1"])   + int(row["Gruppe_>84_W_1"])   + int(row["Gruppe_>84_D_1"])
        
        ag00_m = int(row["Gruppe_<15_M_1"]) + int(row["Gruppe_<15_D_1"])
        ag01_m = int(row["Gruppe_15-24_M_1"])   + int(row["Gruppe_15-24_D_1"])
        ag02_m = int(row["Gruppe_25-34_M_1"]) + int(row["Gruppe_25-34_D_1"])
        ag03_m = int(row["Gruppe_35-44_M_1"]) + int(row["Gruppe_35-44_D_1"])
        ag04_m = int(row["Gruppe_45-54_M_1"]) + int(row["Gruppe_45-54_D_1"])
        ag05_m = int(row["Gruppe_55-64_M_1"]) + int(row["Gruppe_55-64_D_1"])
        ag06_m = int(row["Gruppe_65-74_M_1"]) + int(row["Gruppe_65-74_D_1"])
        ag07_m = int(row["Gruppe_75-84_M_1"]) + int(row["Gruppe_75-84_D_1"])
        ag08_m = int(row["Gruppe_>84_M_1"])   + int(row["Gruppe_>84_D_1"])

        ag00_w = int(row["Gruppe_<15_W_1"])
        ag01_w = int(row["Gruppe_15-24_W_1"])  
        ag02_w = int(row["Gruppe_25-34_W_1"])
        ag03_w = int(row["Gruppe_35-44_W_1"])
        ag04_w = int(row["Gruppe_45-54_W_1"])
        ag05_w = int(row["Gruppe_55-64_W_1"])
        ag06_w = int(row["Gruppe_65-74_W_1"])
        ag07_w = int(row["Gruppe_75-84_W_1"])
        ag08_w = int(row["Gruppe_>84_W_1"])  
        

        ag00_2 = int(row["Gruppe_<15_M_2"]) + int(row["Gruppe_<15_W_2"]) + int(row["Gruppe_<15_D_2"])
        ag01_2 = int(row["Gruppe_15-24_M_2"])    + int(row["Gruppe_15-24_W_2"]) + int(row["Gruppe_15-24_D_2"])
        ag02_2 = int(row["Gruppe_25-34_M_2"]) + int(row["Gruppe_25-34_W_2"]) + int(row["Gruppe_25-34_D_2"])
        ag03_2 = int(row["Gruppe_35-44_M_2"]) + int(row["Gruppe_35-44_W_2"]) + int(row["Gruppe_35-44_D_2"])
        ag04_2 = int(row["Gruppe_45-54_M_2"]) + int(row["Gruppe_45-54_W_2"]) + int(row["Gruppe_45-54_D_2"])
        ag05_2 = int(row["Gruppe_55-64_M_2"]) + int(row["Gruppe_55-64_W_2"]) + int(row["Gruppe_55-64_D_2"])
        ag06_2 = int(row["Gruppe_65-74_M_2"]) + int(row["Gruppe_65-74_W_2"]) + int(row["Gruppe_65-74_D_2"])
        ag07_2 = int(row["Gruppe_75-84_M_2"]) + int(row["Gruppe_75-84_W_2"]) + int(row["Gruppe_75-84_D_2"])
        ag08_2 = int(row["Gruppe_>84_M_2"])   + int(row["Gruppe_>84_W_2"])   + int(row["Gruppe_>84_D_2"])
        
        ag00_2_m = int(row["Gruppe_<15_M_2"]) + int(row["Gruppe_<15_D_2"])
        ag01_2_m = int(row["Gruppe_15-24_M_2"]) + int(row["Gruppe_15-24_D_2"])
        ag02_2_m = int(row["Gruppe_25-34_M_2"]) + int(row["Gruppe_25-34_D_2"])
        ag03_2_m = int(row["Gruppe_35-44_M_2"]) + int(row["Gruppe_35-44_D_2"])
        ag04_2_m = int(row["Gruppe_45-54_M_2"]) + int(row["Gruppe_45-54_D_2"])
        ag05_2_m = int(row["Gruppe_55-64_M_2"]) + int(row["Gruppe_55-64_D_2"])
        ag06_2_m = int(row["Gruppe_65-74_M_2"]) + int(row["Gruppe_65-74_D_2"])
        ag07_2_m = int(row["Gruppe_75-84_M_2"]) + int(row["Gruppe_75-84_D_2"])
        ag08_2_m = int(row["Gruppe_>84_M_2"]) + int(row["Gruppe_>84_D_2"])

        ag00_2_w = int(row["Gruppe_<15_W_2"]) 
        ag01_2_w = int(row["Gruppe_15-24_W_2"]) 
        ag02_2_w = int(row["Gruppe_25-34_W_2"])
        ag03_2_w = int(row["Gruppe_35-44_W_2"])
        ag04_2_w = int(row["Gruppe_45-54_W_2"])
        ag05_2_w = int(row["Gruppe_55-64_W_2"])
        ag06_2_w = int(row["Gruppe_65-74_W_2"])
        ag07_2_w = int(row["Gruppe_75-84_W_2"])
        ag08_2_w = int(row["Gruppe_>84_W_2"])  

        bp_1 = int(row["EingetrageneImpfungenBioNTechPfizer_1"])
        bp_2 = int(row["EingetrageneImpfungenBioNTechPfizer_2"])
        mo_1 = int(row["EingetrageneImpfungenModerna_1"])
        mo_2 = int(row["EingetrageneImpfungenModerna_2"])
        az_1 = int(row["EingetrageneImpfungenAstraZeneca_1"])
        az_2 = int(row["EingetrageneImpfungenAstraZeneca_2"])
        ja = int(row["EingetrageneImpfungenJanssen"])
        unb_1 = int(row["ImpfstoffNichtZugeordnet_1"])
        unb_2 = int(row["ImpfstoffNichtZugeordnet_2"])

        #csv_outfile.seek(0)
        #if bundesland=="Österreich":
        newline = str(datum + "," + str(ag00) + "," + str(ag01) + "," +str(ag02) + "," +str(ag03) + "," +str(ag04) + "," +str(ag05) + "," +str(ag06) + "," +str(ag07) + "," +str(ag08) + "\n")
        line[bundesland].append(newline)

        newline_2 = str(datum + "," + str(ag00_2) + "," + str(ag01_2) + "," +str(ag02_2) + "," +str(ag03_2) + "," +str(ag04_2) + "," +str(ag05_2) + "," +str(ag06_2) + "," +str(ag07_2) + "," +str(ag08_2) + "\n")
        line_2[bundesland].append(newline_2)

        #print(newline)
        #print(datum + "," + str(ag01) + "," +str(ag02) + "," +str(ag03) + "," +str(ag04) + "," +str(ag05) + "," +str(ag06) + "," +str(ag07) + "," +str(ag08) + "\n" )
        #csv_outfile.write(datum + "," + str(ag01) + "," +str(ag02) + "," +str(ag03) + "," +str(ag04) + "," +str(ag05) + "," +str(ag06) + "," +str(ag07) + "," +str(ag08) + "\n" )
        
        newline_g = str(datum + "," + str(ag00_m) + "," + str(ag00_w) + "," + str(ag01_m) + "," + str(ag01_w) + "," +str(ag02_m) + "," + str(ag02_w) + "," +str(ag03_m) + "," + str(ag03_w) + "," +str(ag04_m)+ "," + str(ag04_w) + "," +str(ag05_m)+ "," + str(ag05_w) + "," +str(ag06_m) + "," + str(ag06_w) + "," +str(ag07_m)+ "," + str(ag07_w) + "," +str(ag08_m)+ "," + str(ag08_w) + "," + str(ag00_2_m) + "," + str(ag00_2_w) + "," + str(ag01_2_m) + "," + str(ag01_2_w) + "," +str(ag02_2_m) + "," + str(ag02_2_w) + "," +str(ag03_2_m) + "," + str(ag03_2_w) + "," +str(ag04_2_m)+ "," + str(ag04_2_w) + "," +str(ag05_2_m)+ "," + str(ag05_2_w) + "," +str(ag06_2_m) + "," + str(ag06_2_w) + "," +str(ag07_2_m)+ "," + str(ag07_2_w) + "," +str(ag08_2_m)+ "," + str(ag08_2_w) + "," + str(bp_1) + "," + str(bp_2) + "," + str(mo_1) + "," + str(mo_2) + "," + str(az_1) + "," + str(az_2) + "," + str(ja) + "," + str(unb_1) + "," + str(unb_2) + "\n")

        line_g[bundesland].append(newline_g)
        
    for b in bl:
        line[b].append("Datum,<15,15-24,25-34,35-44,45-54,55-64,65-74,75-84,>84\n")
        line_2[b].append("Datum,<15,15-24,25-34,35-44,45-54,55-64,65-74,75-84,>84\n")
        line_g[b].append("Datum,<15_1_m,<15_1_w,15-24_1_m,15-24_1_w,25-34_1_m,25-34_1_w,35-44_1_m,35-44_1_w,45-54_1_m,45-54_1_w,55-64_1_m,55-64_1_w,65-74_1_m,65-74_1_w,75-84_1_m,75-84_1_w,>84_1_m,>84_1_w,<15_2_m,<15_2_w,15-24_2_m,15-24_2_w,25-34_2_m,25-34_2_w,35-44_2_m,35-44_2_w,45-54_2_m,45-54_2_w,55-64_2_m,55-64_2_w,65-74_2_m,65-74_2_w,75-84_2_m,75-84_2_w,>84_2_m,>84_2_w,bp_1,bp_2,mo_1,mo_2,az_1,az_2,ja,unb_1,unb_2\n")
for b in bl:
    with open(out_path + b + ".csv","w", encoding='utf-8') as csv_outfile:
        #print(out_path + b + ".csv")
        for l in reversed(line[b]):
            csv_outfile.write(l)
            #print(l)
    with open(out_path + b + "_2.csv","w", encoding='utf-8') as csv_outfile:
        #print(out_path + b + ".csv")
        for l in reversed(line_2[b]):
            csv_outfile.write(l)
    with open(out_path + b + "_gesamt.csv","w", encoding='utf-8') as csv_outfile:
        #print(out_path + b + ".csv")
        for l in reversed(line_g[b]):
            csv_outfile.write(l)
