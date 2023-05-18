import sqlite3 as sql
con=sql.connect('habit_tracker.db')
cur=con.cursor()

cur.execute('CREATE TABLE IF NOT EXISTS photos(id INTEGER PRIMARY KEY, photo BLOB)') #создаем таблицу для хранения фотографий


#ДОБАВЛЯЕМ ФОТОГРАФИИ В БАЗУ ДАННЫХ
#for i in range(1,13):
    #with open(f'{i}.jpg','rb') as photo:
        #h=photo.read()
        #cur.execute('INSERT INTO photos(photo) VALUES(?)',[h])


#СЧИТЫВАЕМ ФОТОГРАФИИ ИЗ БАЗЫ ДАННЫХ И СОХРАНЯЕМ В ПРОЕКТ
#photos=cur.execute('SELECT photo FROM photos')
#k=1
#for photo in photos:
    #with open(f'{k}.jpg', 'wb')as file:
        #file.write(photo[0])
        #k+=1


con.commit()
cur.close()
con.close()
input('OK')