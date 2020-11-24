import sqlite3

#method for other modules to create connection
def get_connection():
    connection = sqlite3.connect('sounds_finnish.db')
    return connection

def close_connection(connection):
    connection.commit()
    connection.close()

#create user table
def setup():

    #define connection and cursor
    connection = sqlite3.connect('sounds_finnish.db')
    cursor = connection.cursor()

    command1 = """CREATE TABLE IF NOT EXISTS 
                    user(
                        user_id text PRIMARY KEY,
                        name text,
                        password_hash text
                    )
                """

    cursor.execute(command1)

    #create lesson table

    command2 = """CREATE TABLE IF NOT EXISTS
                    lesson(
                        lesson_id text PRIMARY KEY,
                        name text,
                        description text
                    )
                """

    cursor.execute(command2)

    #create word table

    command3 = """CREATE TABLE IF NOT EXISTS
                    word(
                        word_id text PRIMARY KEY,
                        lesson_id text,
                        name text,
                        description text,
                        translation text,
                        FOREIGN KEY(lesson_id) REFERENCES lesson(lesson_id)
                    )
                """

    cursor.execute(command3)

    #create user activity table

    command4 = """CREATE TABLE IF NOT EXISTS
                    user_activity(
                        user_activity_id text PRIMARY KEY,
                        timestamp integer,
                        word_id text,
                        user_id text,
                        FOREIGN KEY(word_id) REFERENCES word(word_id),
                        FOREIGN KEY(user_id) REFERENCES user(user_id)
                    )
                """

    cursor.execute(command4)

    #create audio table

    command5 = """CREATE TABLE IF NOT EXISTS
                    audio(
                        audio_id text PRIMARY KEY,
                        word_id text,
                        content_url text,
                        FOREIGN KEY(word_id) REFERENCES word(word_id)
                    )
                """

    cursor.execute(command5)

    #create video table

    command6 = """CREATE TABLE IF NOT EXISTS
                    video(
                        video_id text PRIMARY KEY,
                        word_id text,
                        content_url text,
                        FOREIGN KEY(word_id) REFERENCES word(word_id)
                    )
                """

    cursor.execute(command6)

    #add user test data

    cursor.execute("INSERT INTO user VALUES ('40aa', 'Suv', 'C46B72A257050F3772991AAEC4E1D6C2')")
    cursor.execute("INSERT INTO user VALUES ('40ab', 'Octo-Cam', 'EE16C954CDD90E97F79AFFEE819F3830')")

    #add lesson test data

    cursor.execute("INSERT INTO lesson VALUES ('00aa', 'Lesson 1', 'This lesson teaches you how to greet in Finnish.')")
    cursor.execute("INSERT INTO lesson VALUES ('00ab', 'Lesson 2', 'This lesson teaches you how to order a beer in Finnish.')")

    #add word test data

    cursor.execute("INSERT INTO word VALUES ('10aa', '00aa', 'Moi', 'This is used to greet a Finnish person.', 'Hello')")
    cursor.execute("INSERT INTO word VALUES ('10ab', '00ab', 'Olut', 'It is better than kalja.', 'A beer')")

    #add user activity test data

    cursor.execute("INSERT INTO user_activity VALUES ('20aa', 1603635607, '10aa', '40aa')")
    cursor.execute("INSERT INTO user_activity VALUES ('20ab', 1604271682, '10aa', '40ab')")

    #add audio test data

    cursor.execute("INSERT INTO audio VALUES ('30aa', '10aa', 'https://freesound.org/s/426908/')")
    cursor.execute("INSERT INTO audio VALUES ('30ab', '10ab', 'https://freesound.org/s/361815/')")

    #add video test data

    cursor.execute("INSERT INTO video VALUES ('50aa', '10aa', 'https://www.pexels.com/video/hitchhiking-astronaut-holding-a-sign-5274494/')")
    cursor.execute("INSERT INTO video VALUES ('50ab', '10ab', 'https://www.pexels.com/video/a-beer-in-drinking-glass-sliding-on-bar-counter-5530294/')")



    connection.commit()

    connection.close()