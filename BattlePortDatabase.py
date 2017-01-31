import psycopg2
connection = psycopg2.connect(database="BattlePort", user="postgres", password="wachtwoord", host="127.0.0.1", port="5433")
print ("Opened database successfully")

cursor = connection.cursor()







#define create table
def create_table():
    cursor.execute("CREATE TABLE IF NOT EXISTS Scores(pid integer, naam varchar(20), score integer, primary key (pid))")




#define insert into..
def data_entry(pid, naam, score):

    connection = psycopg2.connect(database="BattlePort", user="postgres", password="ivo123", host="127.0.0.1", port="5433")
    cursor = connection.cursor()
    cursor.execute("insert into scores values(%s, %s, %s);", (pid, naam, score))

    connection.commit()
    cursor.close()
    connection.close()
    print("data added successfully")



#define queries
def kweerie(zoekopdracht):
    cursor.execute(zoekopdracht)
    rows = cursor.fetchall()
    for row in rows:
        print("PID = ", row[0])
        print("Naam = ", row[1])
        print("Score = ", row[2], "\n")
    print("----------------------------------")




#create_table()
#data_entry(730, 'jan', 304)
#data_entry(836, 'iemand', 667)

kweerie("SELECT * FROM scores WHERE score > 9000")
kweerie("SELECT * FROM scores WHERE score > 5000 AND score < 9000")
kweerie("SELECT * FROM scores WHERE score < 5000")
kweerie("SELECT * FROM scores order by score DESC ")
