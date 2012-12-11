redo-ifchange rby-stats.py games/en/{red,blue,yellow}.gb

mkdir -p data/red
mkdir -p data/blue
mkdir -p data/yellow

python rby-stats.py games/en/red.gb > data/red/stats
python rby-stats.py games/en/blue.gb > data/blue/stats
python rby-stats.py games/en/yellow.gb > data/yellow/stats
