redo-ifchange rby-stats.py gbc-stats.py
redo-ifchange games/en/{red,blue,yellow}.gb
redo-ifchange games/en/{gold,silver,crystal}.gbc

mkdir -p data/{red,blue,yellow}
mkdir -p data/{gold,silver,crystal}

python rby-stats.py games/en/red.gb > data/red/stats
python rby-stats.py games/en/blue.gb > data/blue/stats
python rby-stats.py games/en/yellow.gb > data/yellow/stats

python gbc-stats.py games/en/gold.gbc > data/gold/stats
python gbc-stats.py games/en/silver.gbc > data/silver/stats
python gbc-stats.py games/en/crystal.gbc > data/crystal/stats
