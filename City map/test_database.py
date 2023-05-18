import sqlite3
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QLabel
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt

def died(vivod):
    conn = sqlite3.connect('City_map.db')
    cursor = conn.cursor()
    cursor.execute("SELECT id, adress, description, name FROM photos")
    data = cursor.fetchall()
    a, b, c, d = [], [], [], []
    for i in data:
        acc = 0
        for j in i:
            if acc == 0: a.append(j); acc += 1; continue;
            if acc == 1: b.append(j); acc += 1; continue;
            if acc == 2: c.append(j); acc += 1; continue;
            if acc == 3: d.append(j);

    print(f'Строка {vivod}: {a[vivod - 1], b[vivod - 1], c[vivod - 1], d[vivod - 1]}')

def address_vivod(vivod):
    conn = sqlite3.connect('City_map.db')
    cursor = conn.cursor()
    cursor.execute("SELECT id, adress, description, name FROM photos")
    data = cursor.fetchall()
    a, b, c, d = [], [], [], []
    for i in data:
        acc = 0
        for j in i:
            if acc == 0: a.append(j); acc += 1; continue;
            if acc == 1: b.append(j); acc += 1; continue;
            if acc == 2: c.append(j); acc += 1; continue;
            if acc == 3: d.append(j);

    end_str = b[vivod - 1]

    return end_str

def description_vivod(vivod):
        conn = sqlite3.connect('City_map.db')
        cursor = conn.cursor()
        cursor.execute("SELECT id, adress, description, name FROM photos")
        data = cursor.fetchall()
        a, b, c, d = [], [], [], []
        for i in data:
            acc = 0
            for j in i:
                if acc == 0: a.append(j); acc += 1; continue;
                if acc == 1: b.append(j); acc += 1; continue;
                if acc == 2: c.append(j); acc += 1; continue;
                if acc == 3: d.append(j);

        and_str = c[vivod - 1]

        return and_str


def name_vivod(vivod):
    conn = sqlite3.connect('City_map.db')
    cursor = conn.cursor()
    cursor.execute("SELECT id, adress, description, name FROM photos")
    data = cursor.fetchall()
    a, b, c, d = [], [], [], []
    for i in data:
        acc = 0
        for j in i:
            if acc == 0: a.append(j); acc += 1; continue;
            if acc == 1: b.append(j); acc += 1; continue;
            if acc == 2: c.append(j); acc += 1; continue;
            if acc == 3: d.append(j);

    ind_str = d[vivod - 1]
    return ind_str







