#import modules
import psycopg2

# Connect to database
connection = psycopg2.connect(database="BattlePort", user="postgres", password="ivo123", host="127.0.0.1", port="5433")
print ("Opened database successfully")

cursor = connection.cursor()

# Tabel aanmaken
def create_table():
    cursor.execute("CREATE TABLE IF NOT EXISTS Scores(pid integer, naam varchar(20), score integer, primary key (pid))")


# Data aan de tabel toevoegen
def data_entry(pid, naam, score):

    connection = psycopg2.connect(database="BattlePort", user="postgres", password="ivo123", host="127.0.0.1", port="5433")
    cursor = connection.cursor()
    cursor.execute("insert into scores values(%s, %s, %s);", (pid, naam, score))
    connection.commit()
    cursor.close()
    connection.close()
    print("data added successfully")


# data uit de tabel printen
def kweerie(zoekopdracht):
    cursor.execute(zoekopdracht)#selecteren
    rows = cursor.fetchall()# kopieeren
    for row in rows:
        print("PID = ", row[0])
        print("Naam = ", row[1])
        print("Score = ", row[2], "\n")
    print("----------------------------------")



# database lezen
def read_database(zoekopdracht):
    cursor.execute(zoekopdracht)#selecteren
    #rows = cursor.fetchall()# kopieeren
    for row in cursor.fetchall():
        print(row)



#create_table()
#data_entry(730, 'jan', 304)
#data_entry(675, 'guus', 5677)

#kweerie("SELECT * FROM scores WHERE score > 9000")
#kweerie("SELECT * FROM scores WHERE score > 5000 AND score < 9000")
#kweerie("SELECT * FROM scores WHERE score < 5000")
#kweerie("SELECT * FROM scores order by score DESC ")


# Downloads the top score from database
def download_top_score():
    result = kweerie("SELECT * FROM scores ORDER BY score DESC")
    return result


#def delete(pid, naam, score):
    #cursor.execute("DELETE FROM scores WHERE values(%s, '%s', %s), (pid,naam,score)")




#delete(156,'marnix', 9012)
#download_top_score()


#cursor.execute("delete from scores * where score = 0;")

#cursor.execute("DELETE from scores where pid = 830;")
connection.commit



download_top_score()
kweerie("SELECT * FROM scores where naam = 'Default'")
#dfatabase = cursor.execute("DELETE FROM scores WHERE score = 0;")