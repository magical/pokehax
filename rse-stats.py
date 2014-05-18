"""Dump pokemon base stats from Generation III Pokemon games

http://bulbapedia.bulbagarden.net/wiki/Pokémon_base_stats_data_structure_in_Generation_III"""


from __future__ import print_function
from __future__ import unicode_literals

import sys

from struct import Struct, pack, unpack

BULBASAUR_STATS = pack("<BBBBBB", 45, 49, 49, 45, 65, 65)
MAX_POKEMON = 411

# stats, types, catch rate & exp yield & effort, items, gender & hatch counter & happiness & growth, egg groups, abilities, flee rate & color, padding
stat_struct = Struct("<BBBBBB 2B BBH 2H BBBB 2B 2B BB xx")

filename, = sys.argv[1:]

# These games are only a couple... er, 17... megabytes. Just read the whole darn
# thing into memory
with open(filename, "rb") as f:
    data = f.read()

try:
    base = data.index(BULBASAUR_STATS)
except ValueError:
    print("Could not find start of stats. Is this really a pokemon game?", file=sys.stderr)
    sys.exit(1)

p = base
for n in range(MAX_POKEMON):
    stats = stat_struct.unpack(data[p:p+stat_struct.size])
    p += stat_struct.size

    print(*stats, sep="\t")
