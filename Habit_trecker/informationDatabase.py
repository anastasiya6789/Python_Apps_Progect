import sqlite3
def name_vivod(vivod):
    conn = sqlite3.connect('habit_tracker.db')
    cursor = conn.cursor()
    cursor.execute("SELECT id, name FROM photos")
    data = cursor.fetchall()
    a, b= [], []
    for i in data:
        acc = 0
        for j in i:
            if acc == 0: a.append(j); acc += 1; continue;
            if acc == 1: b.append(j);


    ind_str = b[vivod - 1]
    return ind_str