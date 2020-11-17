import psycopg2
import PySimpleGUI as sg

try:
    connection = psycopg2.connect(user="postgres",
                                  password="goahead",
                                  host="localhost",
                                  port="5432",
                                  database="postgres_db")

    cursor = connection.cursor()
    # Print PostgreSQL Connection properties
    print ( connection.get_dsn_parameters(),"\n")

    # Print PostgreSQL version
    cursor.execute("SELECT version();")
    record = cursor.fetchone()
    print("You are connected to - ", record,"\n")

    # creating the layout
    layout = [
        [sg.Input(key='body', size=(50,1)), sg.Button('Post'), sg.Button('Show Notes')]
    ]
    window = sg.Window('Title', layout)

    # didnt work-> pg_insert_query = """ INSERT INTO post (body) VALUES (%s)"""

    while True:
        event, values = window.read()
        if event == 'Post':
            # create record in post table
            # didnt work-> record_to_insert = (values['body'])
            cursor.execute(""" INSERT INTO post (body) VALUES ('%s')""" % values['body'])
            connection.commit()
            window['body']('')
            continue
        if event == 'Show Notes':
            notesLayout = [
                [sg.Button('Hi')]
            ]
            notesWindow = sg.Window('Notes', notesLayout)
            while True:
                event, values = notesWindow.read()
                if event == 'Hi':
                    break
                if event == None:
                    break
            notesWindow.close()
            continue
        if event == None:
            break

    window.close()

except (Exception, psycopg2.Error) as error :
    print (error)
finally:
    #closing database connection.
        if(connection):
            cursor.close()
            connection.close()
            print("PostgreSQL connection is closed")