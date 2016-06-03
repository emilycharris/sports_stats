import psycopg2

def start_over():
    start_over = input("Would you like to (l)ook up a player, (a)dd a new player, or (q)uit? ").lower()

    if start_over == 'l' or start_over == 'lookup':
        lookup()

    if start_over == 'a' or start_over == 'add':
        add()

    if start_over() == 'q' or start_over() == 'quit':
        exit()
    else:
        exit()

def lookup():
    cursor = connection.cursor()

    player_name = input("What player would you like to look up? ")
    cursor.execute("SELECT * FROM duke_stats WHERE player = %s;", (player_name,))
    result = cursor.fetchone()

    print("\n| Player Name: {} "
          "| Class: {} "
          "| Position: {} "
          "| Height: {} "
          "| Points: {} "
          "| Rebounds: {} "
          "| Assists: {} |\n".format(result[0], result[1], result[2], result[3], result[4], result[5], result[6]))
    start_over()

def add():
    cursor = connection.cursor()
    try:
        add_name = input("Enter the player's name: ")
        add_class = input("Enter the player's class for the 14-15 season: ")
        add_position = input("Enter the player's position: ")
        add_height = input("Enter the player's height: ")
        add_points = input("Enter the player's points for the 14-15 season: ")
        add_rebounds = input("Enter the player's rebounds for the 14-15 season: ")
        add_assists = input("Enter the player's assists for the 14-15 season: ")
        cursor.execute("INSERT INTO duke_stats (player, class, position, height, points, rebounds, assists) "
                       "VALUES (%s, %s, %s, %s, %s, %s, %s)",
                       (add_name, add_class, add_position, add_height, add_points, add_rebounds, add_assists))
    except psycopg2.DataError:
        print("That is not a valid input.  Try again.")
        start_over()

    connection.commit()
    print("Player added")
    start_over()

connection = psycopg2.connect("dbname=learning_sql user = dbperson")

cursor = connection.cursor()

start_over()

cursor.close()
connection.close()

