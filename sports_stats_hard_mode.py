import psycopg2

def start_over():
    start_over = input("Would you like to (l)ook up or edit a player, (a)dd a new player, or (q)uit? ").lower()

    if start_over == 'l' or start_over == 'lookup':
        lookup()

    if start_over == 'a' or start_over == 'add':
        add()

    if start_over == 'q' or start_over == 'quit':
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

    edit_input = input("Would you like to (e)dit the stats on this player or (r)eturn to the menu? ").lower()
    if edit_input == 'r' or edit_input == 'return':
        start_over()
    if edit_input == 'e' or edit_input == 'edit':
        player_edit(player_name)
    return player_name


def player_edit(player_name):
    field_select = input("\nWould you like to edit the player's (1) name, (2) class, (3) position, (4) height,\n"
                        "(5) points, (6) rebounds, or (7) assists?  Please enter 1-7. ")
    if field_select == '1':
        edit_name = input("\nEnter the player's updated name: ")

        cursor.execute("UPDATE duke_stats SET player = %s WHERE player = %s", (edit_name, player_name))
        connection.commit()

        update_other_fields(player_name)

    if field_select == '2':
        edit_class = input("\nEnter the player's updated class: ")

        cursor.execute("UPDATE duke_stats SET class = %s WHERE player = %s", (edit_class, player_name))
        connection.commit()

        update_other_fields(player_name)

    if field_select == '3':
        edit_position = input("\nEnter the player's updated position: ")

        cursor.execute("UPDATE duke_stats SET position = %s WHERE player = %s", (edit_position, player_name))
        connection.commit()

        update_other_fields(player_name)

    if field_select == '4':
        edit_height = input("\nEnter the player's updated height: ")

        cursor.execute("UPDATE duke_stats SET height = %s WHERE player = %s", (edit_height, player_name))
        connection.commit()

        update_other_fields(player_name)

    if field_select == '5':
        edit_points = input("\nEnter the player's updated points: ")

        cursor.execute("UPDATE duke_stats SET points = %s WHERE player = %s", (edit_points, player_name))
        connection.commit()

        update_other_fields(player_name)

    if field_select == '6':
        edit_rebounds = input("\nEnter the player's updated rebounds: ")

        cursor.execute("UPDATE duke_stats SET rebounds = %s WHERE player = %s", (edit_rebounds, player_name))
        connection.commit()

        update_other_fields(player_name)

    if field_select == '7':
        edit_assists = input("\nEnter the player's updated assists: ")

        cursor.execute("UPDATE duke_stats SET assists = %s WHERE player = %s", (edit_assists, player_name))
        connection.commit()

        update_other_fields(player_name)
    else:
        start_over()


def update_other_fields(player_name):
    update_again = input("\nWould you like to update another field for this player? (Y)es or (N)o. ").lower()
    if update_again == 'y' or update_again == 'yes':
        player_edit(player_name)
    else:
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