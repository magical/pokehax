"""Dump pokemon base stats from gameboy Pokemon games

http://bulbapedia.bulbagarden.net/wiki/Pokémon_base_stats_data_structure_in_Generation_I"""


from __future__ import print_function
from __future__ import unicode_literals

import sys

from struct import pack, unpack
from struct import Struct

BULBASAUR_STATS = pack("<BBBBBB", 1, 45, 49, 49, 45, 65)
MAX_POKEMON = 150

stat_struct = Struct("<BBBBBBBBBBBHH4BBQ")

filename, = sys.argv[1:]

# These games are only a couple megabytes. Just read the whole darn thing into
# memory
with open(filename, "rb") as f:
    data = f.read()

try:
    base = data.index(BULBASAUR_STATS)
except ValueError:
    print("Could not find start of stats. Is this really a pokemon game?", file=sys.stderr)
    sys.exit(0)

#fmt = "{0}\t{1}\t{2}\t{3}\t{4}\t{5}\t{6}\t{7}\t{8}\t{9}\t0x{10:X}\t0x{11:X}\t0x{12:X}\t{13}\t{14}\t{15}\t{16}\t{17}\t{18:064b}"
#fmt = "{0}\t{1}\t{2}\t{3}\t{4}\t{5}\t{6}\t{7}\t{8}\t{9}\t{17}"

p = base
for n in range(MAX_POKEMON):
    stats = stat_struct.unpack(data[p:p+stat_struct.size])
    p += stat_struct.size

    #print(fmt.format(*stats))
    print(*stats, sep="\t")
