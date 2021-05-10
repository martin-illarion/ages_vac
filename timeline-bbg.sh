pt="/home/ubuntu/ages_vac/ages_vac"

curl https://info.gesundheitsministerium.gv.at/data/timeline-bbg.csv -o $pt/timeline-bbg.csv

sed -i "s/;/,/g" $pt/timeline-bbg.csv

head -n1 $pt/timeline-bbg.csv > $pt/bbg-österreich.csv
head -n1 $pt/timeline-bbg.csv > $pt/bbg-wien.csv
head -n1 $pt/timeline-bbg.csv > $pt/bbg-niederösterreich.csv
head -n1 $pt/timeline-bbg.csv > $pt/bbg-burgenland.csv
head -n1 $pt/timeline-bbg.csv > $pt/bbg-oberösterreich.csv
head -n1 $pt/timeline-bbg.csv > $pt/bbg-steiermark.csv
head -n1 $pt/timeline-bbg.csv > $pt/bbg-kärnten.csv
head -n1 $pt/timeline-bbg.csv > $pt/bbg-salzburg.csv
head -n1 $pt/timeline-bbg.csv > $pt/bbg-tirol.csv
head -n1 $pt/timeline-bbg.csv > $pt/bbg-vorarlberg.csv
head -n1 $pt/timeline-bbg.csv > $pt/bbg-bundesbeschaffung.csv

# tac = reverse cat!

tac $pt/timeline-bbg.csv | grep ",Österreich," >> $pt/bbg-österreich.csv
tac $pt/timeline-bbg.csv | grep ",Wien," >> $pt/bbg-wien.csv
tac $pt/timeline-bbg.csv | grep ",Niederösterreich," >> $pt/bbg-niederösterreich.csv
tac $pt/timeline-bbg.csv | grep ",Burgenland," >> $pt/bbg-burgenland.csv
tac $pt/timeline-bbg.csv | grep ",Oberösterreich," >> $pt/bbg-oberösterreich.csv
tac $pt/timeline-bbg.csv | grep ",Steiermark," >> $pt/bbg-steiermark.csv
tac $pt/timeline-bbg.csv | grep ",Kärnten," >> $pt/bbg-kärnten.csv
tac $pt/timeline-bbg.csv | grep ",Salzburg," >> $pt/bbg-salzburg.csv
tac $pt/timeline-bbg.csv | grep ",Tirol," >> $pt/bbg-tirol.csv
tac $pt/timeline-bbg.csv | grep ",Vorarlberg," >> $pt/bbg-vorarlberg.csv
tac $pt/timeline-bbg.csv | grep ",Bundesbeschaffung," >> $pt/bbg-bundesbeschaffung.csv