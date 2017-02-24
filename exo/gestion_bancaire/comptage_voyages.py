#!/usr/bin/env python
# -*- coding: utf-8 -*-

from	datetime	import	datetime
import re
import sqlite3 as lite


f = open("/media/stagiaire/Dawan/training-python/assets/comptage-voyageurs-trains-transilien.csv", 'r')
max_montants = 0
f.readline()
for i in f:

    print (i[:-1])
    montants = i[:-1].split(';')
    if int(montants[-1]) > max_montants:
        jour= datetime.strptime(montants[3], '%Y-%m-%d')
        if jour.weekday() == 3:
            max_montants = int(montants[-1])
            ligne = i

f.seek(0)

f.readline()
for i in f:
    montants = i[:-1].split(';')
    reg = re.compile("Entre ([0-9]*)h et ([0-9]*)h")
    print (montants[-2])
    res = reg.search(montants[-2])
    print (res)
#    deb = res.group(1)
#    fin = res.group(2)
#    print (deb)
#    print (fin)

f.close


print (max_montants)
print (ligne)

con	=lite.connect('test.db')
with con:
    cursor	=	con.cursor()
    cursor.execute('CREATE TABLE IF NOT EXISTS episode (num_saison, num_episode)')



