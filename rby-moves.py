"""Dump move data from gameboy Pokemon games"""

from __future__ import print_function
from __future__ import unicode_literals

import sys

from struct import Struct, pack, unpack

POUND_STATS = pack("<BBBBBB", 1, 0, 40, 0, 255, 35)
#BASE = 0x38000
MAX_MOVES = 165

# n, effect, power, type, accuracy, pp
move_struct = Struct("<BBBBBB")

filename, = sys.argv[1:]

# These games are only a couple megabytes. Just read the whole darn thing into
# memory
with open(filename, "rb") as f:
    data = f.read()

try:
    base = data.index(POUND_STATS)
except ValueError:
    print("Could not find start of move data. Is this a Pokemon game?", file=sys.stderr)
    sys.exit(1)

p = base
for n in range(MAX_MOVES):
    stats = move_struct.unpack(data[p:p+move_struct.size])
    p += move_struct.size

    print(*stats, sep="\t")
