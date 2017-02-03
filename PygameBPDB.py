


import psycopg2


def interact_with_database(command):
    # Connect and set up cursor            #database gegevens                           wachtwoord
    connection = psycopg2.connect(database="BPDB", user="postgres", password="ivo123", host="127.0.0.1", port="5433")
    cursor = connection.cursor()

    # Execute the command
    cursor.execute(command)
    connection.commit()

    # Save results
    results = None
    try:
        results = cursor.fetchall()
    except psycopg2.ProgrammingError:
        # Nothing to fetch
        pass

    # Close connection
    cursor.close()
    connection.close()

    return results


# Uploads a score into the hiscore table
def upload_score(name, score):
    query = "UPDATE score SET sc=" + str(score) + " WHERE name = '" + name + "'"
    print(query)
    interact_with_database(query)


# Downloads score data from database
def download_scores():
    return interact_with_database("SELECT * FROM score")


# Downloads the top score from database
def download_top_score(score):                                              # welke waarde wil je
    result = interact_with_database("SELECT * FROM score ORDER BY score")[0][1]

    return result

def newplayer(name):
    query = "INSERT INTO score (sc,name) VALUES (1,'"+ name + "');"
    interact_with_database(query)

def addscore(name):
    score = interact_with_database("SELECT sc FROM score WHERE name = '" + name + "';" )[0][0]
    query = "UPDATE score SET sc=" + str(score+1) + " WHERE name = '" + name + "';"
    interact_with_database(query)

def checkname(name):
    query = interact_with_database("SELECT name FROM score WHERE name = '" + name + "';")
    if query == []:
        return False
    else:
        print("[('"+name+"',)]")
        return True


n = str(input())
if checkname(n):
    addscore(n)
else:
    newplayer(n)