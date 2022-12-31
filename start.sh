if [ -z $UPSTREAM_REPO ]
then
  echo "Cloning main Repository"
  git clone https://github.com/DRAGON-PRO/LazyPrincessV2.git /FLIMS-HD
else
  echo "Cloning Custom Repo from $UPSTREAM_REPO "
  git clone $UPSTREAM_REPO /FLIMS-HD
fi
cd /FLIMS-HD
pip3 install -U -r requirements.txt
echo "🍃Starting Bot🍃...."
python3 bot.py
