import requests;
import csv;
import math;
from datetime import datetime

l_file="/home/ubuntu/ages_vac/ages_vac/impfungen-gemeinden.csv"
#l_file="C:\\Users\\mpolak_cloudbees\\Dropbox\\python\\ages_impfung\\impfungen-gemeinden.csv"
out_path="/home/ubuntu/ages_vac/ages_vac/"
#out_path="C:\\Users\\mpolak_cloudbees\\Dropbox\\python\\ages_impfung\\"

url = 'https://info.gesundheitsministerium.gv.at/data/impfungen-gemeinden.csv'
req = requests.get(url, allow_redirects=True)

url_content = req.content
csv_file = open(l_file, 'wb')
#print(url_content)
csv_file.write(url_content)
csv_file.close()

bl_list=["Burgenland","Kärnten","Niederösterreich","Oberösterreich","Salzburg","Steiermark","Tirol","Vorarlberg","Wien"]

gkz_list = {
    "101": "Eisenstadt (Stadt)",
    "102": "Rust (Stadt)",
    "103": "Eisenstadt-Umgebung",
    "104": "Güssing",
    "105": "Jennersdorf",
    "106": "Mattersburg",
    "107": "Neusiedl am See",
    "108": "Oberpullendorf",
    "109": "Oberwart",
    "201": "Klagenfurt (Stadt)",
    "202": "Villach (Stadt)",
    "203": "Hermagor",
    "204": "Klagenfurt Land",
    "205": "Sankt Veit an der Glan",
    "206": "Spittal an der Drau",
    "207": "Villach Land",
    "208": "Völkermarkt",
    "209": "Wolfsberg",
    "210": "Feldkirchen",
    "301": "Krems an der Donau",
    "302": "Sankt Pölten (Stadt)",
    "303": "Waidhofen an der Ybbs (Stadt)",
    "304": "Wiener Neustadt (Stadt)",
    "305": "Amstetten",
    "306": "Baden",
    "307": "Bruck an der Leitha",
    "308": "Gänserndorf",
    "309": "Gmünd",
    "310": "Hollabrunn",
    "311": "Horn",
    "312": "Korneuburg",
    "313": "Krems (Land)",
    "314": "Lilienfeld",
    "315": "Melk",
    "316": "Mistelbach",
    "317": "Mödling",
    "318": "Neunkirchen",
    "319": "Sankt Pölten (Land)",
    "320": "Scheibbs",
    "321": "Tulln",
    "322": "Waidhofen an der Thaya",
    "323": "Wiener Neustadt (Land)",
    "325": "Zwettl",
    "401": "Linz (Stadt)",
    "402": "Steyr (Stadt)",
    "403": "Wels (Stadt)",
    "404": "Braunau am Inn",
    "405": "Eferding",
    "406": "Freistadt",
    "407": "Gmunden",
    "408": "Grieskirchen",
    "409": "Kirchdorf an der Krems",
    "410": "Linz-Land",
    "411": "Perg",
    "412": "Ried im Innkreis",
    "413": "Rohrbach",
    "414": "Schärding",
    "415": "Steyr-Land",
    "416": "Urfahr-Umgebung",
    "417": "Vöcklabruck",
    "418": "Wels-Land",
    "501": "Salzburg (Stadt)",
    "502": "Hallein",
    "503": "Salzburg-Umgebung",
    "504": "Sankt Johann im Pongau",
    "505": "Tamsweg",
    "506": "Zell am See",
    "601": "Graz (Stadt)",
    "603": "Deutschlandsberg",
    "606": "Graz-Umgebung",
    "610": "Leibnitz",
    "611": "Leoben",
    "612": "Liezen",
    "614": "Murau",
    "616": "Voitsberg",
    "617": "Weiz",
    "620": "Murtal",
    "621": "Bruck-Mürzzuschlag",
    "622": "Hartberg-Fürstenfeld",
    "623": "Südoststeiermark",
    "701": "Innsbruck-Stadt",
    "702": "Imst",
    "703": "Innsbruck-Land",
    "704": "Kitzbühel",
    "705": "Kufstein",
    "706": "Landeck",
    "707": "Lienz",
    "708": "Reutte",
    "709": "Schwaz",
    "801": "Bludenz",
    "802": "Bregenz",
    "803": "Dornbirn",
    "804": "Feldkirch",
    "901": "Wien-Innere Stadt",
    "902": "Wien-Leopoldstadt",
    "903": "Wien-Landstraße",
    "904": "Wien-Wieden",
    "905": "Wien-Margareten",
    "906": "Wien-Mariahilf",
    "907": "Wien-Neubau",
    "908": "Wien-Josefstadt",
    "909": "Wien-Alsergrund",
    "910": "Wien-Favoriten",
    "911": "Wien-Simmering",
    "912": "Wien-Meidling",
    "913": "Wien-Hietzing",
    "914": "Wien-Penzing",
    "915": "Wien-Rudolfsheim-Fünfhaus",
    "916": "Wien-Ottakring",
    "917": "Wien-Hernals",
    "918": "Wien-Währing",
    "919": "Wien-Döbling",
    "920": "Wien-Brigittenau",
    "921": "Wien-Floridsdorf",
    "922": "Wien-Donaustadt",
    "923": "Wien-Liesing"
}

pop_bez={}
frst_bez={}
scnd_bez={}

with open(l_file,"r", newline='',encoding="utf-8-sig") as csvfile:
    cov_reader = csv.DictReader(csvfile, delimiter=';')
    for row in cov_reader:
        #Datum;Gemeindecode;Bevölkerung;Teilgeimpfte;TeilgeimpftePro100;Vollimmunisierte;VollimmunisiertePro100
        date_str = row["Datum"]
        date_obj = datetime.strptime(date_str[0:10], "%Y-%m-%d")
        date = date_obj.strftime("%Y/%m/%d")
        gkz = row["Gemeindecode"][0:3]
        pop = row["Bevölkerung"]
        frst = row["Teilgeimpfte"]
        scnd = row["Vollimmunisierte"]
        bl=bl_list[int(gkz[0])-1]
        if date not in pop_bez:
            pop_bez[date] = {}
            frst_bez[date] = {}
            scnd_bez[date] = {}
        if bl not in pop_bez[date]:
            pop_bez[date][bl] = {}
            frst_bez[date][bl] = {}
            scnd_bez[date][bl] = {}
        if gkz not in pop_bez[date][bl]:
            pop_bez[date][bl][gkz] = int(pop)
            frst_bez[date][bl][gkz] = int(frst)
            scnd_bez[date][bl][gkz] = int(scnd)
        else:
            pop_bez[date][bl][gkz] += int(pop)
            frst_bez[date][bl][gkz] += int(frst)
            scnd_bez[date][bl][gkz] += int(scnd)

hdr_pop=True
hdr_teil=True
hdr_voll=True

with open(out_path + "vac_bez_pop.csv","r", encoding='utf-8') as f:
    if f.readline()[0:5]=="date,": hdr_pop=False
with open(out_path + "vac_bez_teil.csv","r", encoding='utf-8') as f:
    if f.readline()[0:5]=="date,": hdr_teil=False
with open(out_path + "vac_bez_voll.csv","r", encoding='utf-8') as f:
    if f.readline()[0:5]=="date,": hdr_voll=False

with open(out_path + "vac_bez_pop.csv","a+", encoding='utf-8') as csv_popfile:
    with open(out_path + "vac_bez_teil.csv","a+", encoding='utf-8') as csv_teilfile:
        with open(out_path + "vac_bez_voll.csv","a+", encoding='utf-8') as csv_vollfile:
            hdr = "date"
            line_pop = date
            line_frst = date
            line_scnd = date
            for bl in bl_list:
                for d in pop_bez:
                    for g in pop_bez[d][bl]:
                        line_pop += "," + str(pop_bez[d][bl][g])
                        line_frst += "," + str(frst_bez[d][bl][g])
                        line_scnd += "," + str(scnd_bez[d][bl][g])
                        hdr += "," + gkz_list[g]
            hdr += "\n"
            line_pop += "\n"
            line_frst += "\n"
            line_scnd += "\n"
            if hdr_pop: csv_popfile.write(hdr)
            if hdr_teil: csv_teilfile.write(hdr)
            if hdr_voll: csv_vollfile.write(hdr)
            csv_popfile.write(line_pop)
            csv_teilfile.write(line_frst)
            csv_vollfile.write(line_scnd)
