dt=$(date)

cd /home/ubuntu/ages_vac/ages_vac/

git pull
echo "$dt [INFO] git pull done"

python3 get_vac.py
echo "$dt [INFO] get_vac done"

dat=$(date)

/home/ubuntu/ages_vac/ages_vac/timeline-bbg.sh
echo "$dt [INFO] BBG done"

git commit -am "$dat"
echo "git commit done $dat"

git push

echo "[INFO] pushed"
