import psycopg2


connection = psycopg2.connect("dbname=learning_sql user = dbperson")

cursor = connection.cursor()

player_name = input("What player would you like to look up? ")

cursor.execute("SELECT * FROM duke_stats WHERE player = %s;", (player_name,))
result = cursor.fetchone()

print("| Player Name: {} "
      "| Class: {} "
      "| Position: {} "
      "| Height: {} "
      "| Points: {} "
      "| Rebounds: {} "
      "| Assists: {} |".format(result[0], result[1], result[2], result[3], result[4], result[5], result[6]))



cursor.close()
connection.close()