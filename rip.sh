#!/bin/bash
set -eu

mkdir -p data/{red,blue,yellow}
mkdir -p data/{gold,silver,crystal}
mkdir -p data/{ruby,sapphire,emerald}

python rby-stats.py games/en/red.gb > data/red/stats
python rby-stats.py games/en/blue.gb > data/blue/stats
python rby-stats.py games/en/yellow.gb > data/yellow/stats

python gsc-stats.py games/en/gold.gbc > data/gold/stats
python gsc-stats.py games/en/silver.gbc > data/silver/stats
python gsc-stats.py games/en/crystal.gbc > data/crystal/stats

python rby-moves.py games/en/red.gb > data/red/moves
python rby-moves.py games/en/blue.gb > data/blue/moves
python rby-moves.py games/en/yellow.gb > data/yellow/moves

for version in ruby sapphire emerald; do
    python rse-stats.py games/en/$version.gba > data/$version/stats
done

python rby-evo-moves.py games/en/red.gb | tee >(sed -n '1~2p' >data/red/evo) >(sed -n '2~2p' >data/red/levelup-moves) >/dev/null
python rby-evo-moves.py games/en/blue.gb | tee >(sed -n '1~2p' >data/blue/evo) >(sed -n '2~2p' >data/blue/levelup-moves) >/dev/null
