#!/usr/bin/python
from string import maketrans
ko = "aiouHn"
cok = "@195uA"
kocokil = maketrans(ko, cok)
stur = "\0x54\0x68\0x65\0x20\0x46\0x4c\0x41\0x47\0x20\0x2d\0x3e\0x20\0x6b\0x55\0x61\0x35\0x41\0x54\0x75\0x48\0x61\0x6e\0x79\0x41\0x6e\0x39\0x33\0x53\0x61"
print stur.translate(kocokil)
