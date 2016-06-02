import psycopg2
import csv

connection = psycopg2.connect("dbname=learning_sql user = dbperson")

cursor = connection.cursor()

cursor.execute("DROP TABLE IF EXISTS duke_stats;")

table_create_command = '''CREATE TABLE duke_stats (
  player varchar(20),
  class varchar(3),
  position varchar(1),
  height varchar(10),
  points float(5),
  rebounds float(5),
  assists float(5)
);'''

cursor.execute(table_create_command)

with open("player_stats.csv") as infile:
    data = csv.DictReader(infile, fieldnames=["player", "class", "position", "height", "points", "rebounds", "assists"])
    for row in data:
        cursor.execute("INSERT INTO duke_stats VALUES (%s, %s, %s, %s, %s, %s, %s);", (row['player'],
                                                                                       row['class'],
                                                                                       row['position'],
                                                                                       row['height'],
                                                                                       float(row['points']),
                                                                                       float(row['rebounds']),
                                                                                       float(row['assists'])))

connection.commit()


cursor.close()
connection.close()