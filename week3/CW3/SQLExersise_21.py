# -*- coding: utf-8 -*-
"""
Created on Thu Sep  5 23:08:56 2019

@author: ORCAS_ISLAM
"""

import sqlite3
conn = sqlite3.connect('officesqlite.sqlite')
c = conn.cursor()

c.execute("INSERT INTO students (name,subject,grade) VALUES ('Salim','Math',95)")
c.execute("INSERT INTO students (name,subject,grade) VALUES ('Noor','History',94)")
c.execute("INSERT INTO students (name,subject,grade) VALUES ('Noor','Bioogy',96)")
c.execute("INSERT INTO students (name,subject,grade) VALUES ('Salah','Math',80)")
c.execute("INSERT INTO students (name,subject,grade) VALUES ('Salim','History',67)")
c.execute("INSERT INTO students (name,subject,grade) VALUES ('Maria','Biology',73)")
c.execute("INSERT INTO students (name,subject,grade) VALUES ('Noor','Math',100)")
c.execute("INSERT INTO students (name,subject,grade) VALUES ('Maria','Math',50)")
c.execute("INSERT INTO students (name,subject,grade) VALUES ('Salah','History',98)")
c.execute("INSERT INTO students (name,subject,grade) VALUES ('Salim','Biology',85)")

conn.commit()
conn.close()

    