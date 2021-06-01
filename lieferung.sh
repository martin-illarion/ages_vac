pt="/home/ubuntu/ages_vac/ages_vac"

curl https://info.gesundheitsministerium.gv.at/data/timeline-lieferungen-impfstoffe.csv -o $pt/timeline-lieferungen-impfstoffe.csv

sed -i "s/;/,/g" $pt/timeline-lieferungen-impfstoffe.csv

echo "" >> $pt/timeline-lieferungen-impfstoffe.csv

head -n1 $pt/timeline-lieferungen-impfstoffe.csv > $pt/vac-lieferung.csv

# tac = reverse cat!

tail -n +2 $pt/timeline-lieferungen-impfstoffe.csv | tac >> $pt/vac-lieferung.csv