import sqlite3 as sql


class Drifter_Server():

    def __init__(self,):

        connection = sql.connect('drifter.db')

        cursor = connection.cursor()

        cursor.execute('''CREATE TABLE systems
                            (name text)''')

        cursor.execute("INSERT INTO systems VALUES ('Sol System')")

        connection.commit()

        connection.close
