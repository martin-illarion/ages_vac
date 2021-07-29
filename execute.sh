dt=$(date)

cd /home/ubuntu/ages_vac/ages_vac/

git pull
echo "$dt [INFO] git pull done"

python3 get_vac.py
echo "$dt [INFO] get_vac done"

dat=$(date)

/home/ubuntu/ages_vac/ages_vac/timeline-bbg.sh
echo "$dt [INFO] BBG done"

curl https://info.gesundheitsministerium.gv.at/data/impfungen-gemeinden.csv -o /home/ubuntu/ages_vac/ages_vac/gemeinden_tmp.csv
tail -n +2 /home/ubuntu/ages_vac/ages_vac/gemeinden.csv >> /home/ubuntu/ages_vac/ages_vac/gemeinden_new.csv
mv -f /home/ubuntu/ages_vac/ages_vac/gemeinden_new.csv /home/ubuntu/ages_vac/ages_vac/gemeinden.csv

git commit -am "$dat"
echo "git commit done $dat"

git push

echo "[INFO] pushed"
