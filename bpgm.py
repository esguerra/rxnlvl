#! /usr/bin/python

# Boilerplate
import sys
sys.path.insert(1,"/Users/esguerra/development/python/rxnlvl/") # Change this to the full path of rxnlvl
from rxnlvl import *

# Plot
p = plot([10.0,10.0],vbuf=10.0,hbuf=5.0,bgcolour=None, qualified='sortof')

p +  level(energy(   00,     'kcalmol'),  1,  'bG6P',         0x0)
p +  level(energy(   15.1,   'kcalmol'),  2,  'elsass1',    0xFF4444)
p +  level(energy(   14.0,   'kcalmol'),  2,  'webster1',    0xFF4444)
p +  level(energy(   6.1,    'kcalmol'),  2,  'marcos1',    0xFF4444)
p +  level(energy(   3.8,    'kcalmol'),  3,  'elsass2',         0x0)
p +  level(energy(   4.3,    'kcalmol'),  3,  'webster2', 0xFF4444)
p +  level(energy(  -6.7,    'kcalmol'),  3,  'marcos2',      0x0)

p +  edge(  'bG6P',  'elsass1',   0x0, 0.4, 'normal')
p +  edge(  'bG6P',  'webster1',   0x0, 0.4, 'normal')
p +  edge(  'bG6P',  'marcos1',   0x0, 0.4, 'normal')

p +  edge(  'elsass1', 'elsass2', 0x0, 0.2, 'normal')
p +  edge(  'webster1', 'webster2', 0x0, 0.4, 'normal')
p +  edge(  'marcos1', 'marcos2', 0x0, 0.4, 'normal')


p + baseline(energy( 0.0, 'kcalmol'),colour=0x0,mode='dashed',opacity=0.1)

p.write()
