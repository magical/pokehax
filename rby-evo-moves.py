
from __future__ import print_function, unicode_literals

import sys
from struct import pack, unpack

BASE = 0x3b05c
BASE_NEAR = 0x705c
MAX = 190

filename, = sys.argv[1:]

f = open(filename, "rb")
f.seek(BASE)

base = BASE_NEAR + 2*MAX
# data follows pointers
pointers = [unpack("<H", f.read(2))[0] for _ in range(MAX)]

BANK_BASE = 0x38000 - 0x4000

def zread(f):
    string = b""
    while True:
        b = f.read(1)
        if b == b"\x00":
            break
        string += b
    return string


for p in pointers:
    f.seek(p + BANK_BASE)
    evos = zread(f)
    moves = zread(f)

    #print("evos:", *evos)
    #print("moves:", *moves)
    print(*evos)
    print(*moves)
