#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sqlite3 as lite

class MediaDB:
    def __init__(self):
        con = lite.connect('mediasql.db')

        with con:
            cursor = con.cursor()
            cursor.execute('CREATE TABLE IF NOT EXISTS episode (num_saison, num_episode)')
            con.commit()

MariaDB()