if [ -z $UPSTREAM_REPO ]
then
  echo "Cloning main Repository"
  git clone https://github.com/DRAGON-PRO/FLIMS-HD-2.git /FLIMS-HD-2
else
  echo "Cloning Custom Repo from $UPSTREAM_REPO "
  git clone $UPSTREAM_REPO /FLIMS-HD-2
fi
cd /FLIMS-HD-2
pip3 install -U -r requirements.txt
echo "🍃Starting Bot🍃...."
python3 bot.py
