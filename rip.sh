set -eu

mkdir -p data/{red,blue,yellow}
mkdir -p data/{gold,silver,crystal}

python rby-stats.py games/en/red.gb > data/red/stats
python rby-stats.py games/en/blue.gb > data/blue/stats
python rby-stats.py games/en/yellow.gb > data/yellow/stats

python gsc-stats.py games/en/gold.gbc > data/gold/stats
python gsc-stats.py games/en/silver.gbc > data/silver/stats
python gsc-stats.py games/en/crystal.gbc > data/crystal/stats

python rby-moves.py games/en/red.gb > data/red/moves
python rby-moves.py games/en/blue.gb > data/blue/moves
python rby-moves.py games/en/yellow.gb > data/yellow/moves
