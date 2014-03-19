#! /usr/bin/python

# Boilerplate
import sys
sys.path.insert(1,"/Users/esguerra/development/python/rxnlvl/") # Change this to the full path of rxnlvl
from rxnlvl import *

# Plot
p = plot([10.0,10.0],vbuf=10.0,hbuf=5.0,bgcolour=None, qualified='sortof')

p +  level(energy(   00,     'kcalmol'),  1,  'G1P',         0x0)
p +  level(energy(   23.6,   'kcalmol'),  2,  'EaW',    0xFF4444)
p +  level(energy(   14.4,   'kcalmol'),  2,  'EaP',         0x0)
p +  level(energy(  -10.3,   'kcalmol'),  3,  'G16bpW', 0xFF4444)
p +  level(energy(  -14.5,   'kcalmol'),  3,  'G16bpP',      0x0)

p +  edge(  'G1P',  'EaW',   0x0, 0.4, 'normal')
p +  edge(  'G1P',  'EaP',   0x0, 0.4, 'normal')
p +  edge(  'EaW', 'G16bpW', 0x0, 0.2, 'normal')
p +  edge(  'EaP', 'G16bpP', 0x0, 0.4, 'normal')

p + baseline(energy( 0.0, 'kcalmol'),colour=0x0,mode='dashed',opacity=0.1)

p.write()
