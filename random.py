#!/usr/bin/env python

import random

print "Content-Type: text/plain"
print

def div(d):
    num = random.randint(100000, 99999999)
    num = round(num / d) * d
    return int(num)

print "Random value is " + str(div(1423));
