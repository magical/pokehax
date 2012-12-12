"""Dump pokemon base stats from Generation II Pokemon games

http://bulbapedia.bulbagarden.net/wiki/Pokémon_base_stats_data_structure_in_Generation_II"""


from __future__ import print_function
from __future__ import unicode_literals

import sys

from struct import Struct, pack, unpack

BULBASAUR_STATS = pack("<BBBBBB", 1, 45, 49, 49, 45, 65)
MAX_POKEMON = 251

# n, stats, types, catch rate & exp yield, items, gender & unknown & hatch counter & unknown, sprite dims. & blank & blank, growth & egg groups, tms
stat_struct = Struct("<B BBBBBB 2B BB 2B BBBB BHH BB Q")

filename, = sys.argv[1:]

# These games are only a couple megabytes. Just read the whole darn thing into
# memory
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
