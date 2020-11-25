import sqlite3
import uuid

#method for other modules to create connection
def get_connection():
    connection = sqlite3.connect('sounds_finnish.db')
    return connection

def close_connection(connection):
    connection.commit()
    connection.close()

#create all tables
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

    """ cursor.execute("INSERT INTO user VALUES ('40aa', 'Suv', 'C46B72A257050F3772991AAEC4E1D6C2')")
    cursor.execute("INSERT INTO user VALUES ('40ab', 'Octo-Cam', 'EE16C954CDD90E97F79AFFEE819F3830')") """

    #add lesson data
    lesson_id1 = str(uuid.uuid4())
    lesson_id2 = str(uuid.uuid4())
    cursor.execute("INSERT INTO lesson VALUES (?, 'Lesson 1', 'This lesson teaches you the most typical words in Finnish. The ones you are likely to encounter everyday in Finland.')", (lesson_id1,))
    cursor.execute("INSERT INTO lesson VALUES (?, 'Lesson 2', 'This lesson acts as your survival kit in Finland, including how to order a beer in Finnish.')", (lesson_id2,))

    #add word test data

    """ cursor.execute("INSERT INTO word VALUES (?, ?, 'Moi', 'This is used to greet a Finnish person.', 'Hello')", (word_id, lesson_id1,))
    cursor.execute("INSERT INTO word VALUES (?, ?, 'Mikä sun nimi on?', 'This sentence helps to inquire what to call the person you just encountered.', 'What's your name?')", (word_id, lesson_id2,)) """

    # &#228; and &auml; = ä  &#246; and &ouml; = ö
    
    #add word datat for lesson 1
    words = [
        dict(name="Moi", description="This is used to greet a Finnish person", translation="Hello"),
        dict(name="Moi moi", description="This is used to wish a person farewell", translation="Bye bye"),
        dict(name="L&auml;het&auml;&auml;n!", description="Used to suggest to your friend that you should be leaving", translation="Let&apos;s go!"),
        dict(name="N&auml;h&auml;&auml;n!", description="Literal translation: We will see", translation="See you!"),
        dict(name="H&auml;h?", description="Used when you did not hear what your friend said to you", translation="What?"),
        dict(name="Mit&auml;s s&auml;?", description="Literal translation: What you?", translation="How are you?"),
        dict(name="Mit&auml;s t&auml;ss&auml;?", description="Literal translation: What here? This is basically the way to answer the question How are you? without actually giving a proper answer back.", translation="Not bad or Alright"),
        dict(name="Mit&auml;s ite?", description="Literal translation: What yourself?", translation="And you?"),
        dict(name="Kiitos", description="Finnish people give thanks when it is deserved and never only for the sake of saying it.", translation="Thank you"),
        dict(name="Sori", description="Finnish people would use this if they accidentally bumb into you. This is not used for apologising after a serious mess up.", translation="Sorry"),
        dict(name="Joo", description="The variation to this that has the same meaning is: Juu", translation="Yes"),
        dict(name="Ei", description="Use this when you disagree with something a person has said", translation="No"),
        dict(name="Ei mit&auml;&auml;n", description="Literal translation: No nothing. This could be used when you did someone a favour and they thanked you for it.", translation="No problem or It was nothing"),
        dict(name="Ok", description="Pay attention to the Finnish pronounciation of this word", translation="Ok"),
        dict(name="Selv&auml;", description="This is used to tell someone you have understood the instructions they gave you.", translation="Alright"),
        dict(name="Jee!", description="This is used to show enthusiasm", translation="Yay!"),
        dict(name="Oota!", description="Use this to ask you friend to wait for you", translation="Wait!"),
        dict(name="Apua!", description="Use this when you are in a dire need of help", translation="Help!"),
        dict(name="Kippis!", description="Used when you raise a toast with someone", translation="Cheers!")
    ]
    for word in words:
        cursor.execute("INSERT INTO word VALUES (?,?,?,?,?)", (str(uuid.uuid4()), lesson_id1, word["name"], word["description"], word["translation"],))

    # &#228; and &auml; = ä  &#246; and &ouml; = ö

    #add word data for lesson 2
    words = [
        dict(name="Mik&auml; sun nimi on?", description="Direct translation: What your name is?", translation="What&apos;s your name?"),
        dict(name="M&auml; oon..", description="M&auml; is a shortened version from the word min&auml;.", translation="I am.."),
        dict(name="Puhuks&auml; englantii?", description="Direct translation: Speak you English? S&auml; is a shortened version from sin&auml;.", translation="Do you speak English?"),
        dict(name="Miks?", description="Shortened from Miksi?", translation="Why?"),
        dict(name="En tii&auml;", description="Shortened from En tied&auml;?", translation="I don&apos;t know"),
        dict(name="Emm&auml; usko", description="Direct translation: I don&apos;t believe. Shortened from En m&auml; usko", translation="I don&apos;t think so"),
        dict(name="Hienoo!", description="Used when you want to celebrate something.", translation="Great! or Excellent!"),
        dict(name="Onnee!", description="Direct translation: Luck!", translation="Congratulations!"),
        dict(name="Mit&auml; t&auml;&auml; tarkottaa?", description="Direct translation: What this means?", translation="What does this mean?"),
        dict(name="Onks teil wifii?", description="Pay attention to the Finnish pronounciation of &apos;wifii&apos;. Direct translation: Do you(plural) have wifi?", translation="Do you have wifi?"),
        dict(name="Mis teil on vessa?", description="Direct translation: Where you(plural) have the bathroom?", translation="Where can I find the bathroom?"),
        dict(name="Puhun vaa v&auml;h&auml; suomee.", description="Direct translation: I speak only less Finnish.", translation="I (can) only speak a little Finnish"),
        dict(name="En tajuu mit&auml;&auml;.", description="Direct translation: I don&apos;t undestand nothing.", translation="I (can&apos;t) understand anything."),
        dict(name="Voiks&auml; puhuu hitaammin?", description="Voiks&auml; shortened from &apos;Voitko s&auml;&apos;", translation="Can you speak slower?"),
        dict(name="Voikko j&auml;tt&auml;&auml; mut rauhaan?", description="The nice way of asking someone to leave you alone.", translation="Can you leave me alone?"),
        dict(name="Yks kahvi, kiitos", description="This sentence will get you a Finnish black filter coffee from a cafe. Finnish language doesn&apos;t have the word for &apos;please&apos;, so in this case we use &apos;thank you&apos; instead.", translation="One coffee, thank you"),
        dict(name="Yks olut, kiitos", description="This sentence will get you a house beer in a bar.", translation="One beer, thank you"),
        dict(name="M&auml;, s&auml;, se", description="Se refers to any one person with any gender.", translation="I, you, she or he or it"),
        dict(name="Me, te, ne", description="Ne refers to any group of people regardless of their gender.", translation="We, you(plural), they")
    ]
    for word in words:
        cursor.execute("INSERT INTO word VALUES (?,?,?,?,?)", (str(uuid.uuid4()), lesson_id2, word["name"], word["description"], word["translation"],))
    
    #add user activity test data

    """ cursor.execute("INSERT INTO user_activity VALUES ('20aa', 1603635607, '10aa', '40aa')")
    cursor.execute("INSERT INTO user_activity VALUES ('20ab', 1604271682, '10aa', '40ab')") """

    #add audio test data

    """ cursor.execute("INSERT INTO audio VALUES ('30aa', '10aa', 'https://freesound.org/s/426908/')")
    cursor.execute("INSERT INTO audio VALUES ('30ab', '10ab', 'https://freesound.org/s/361815/')") """

    #add video test data

    """ cursor.execute("INSERT INTO video VALUES ('50aa', '10aa', 'https://www.pexels.com/video/hitchhiking-astronaut-holding-a-sign-5274494/')")
    cursor.execute("INSERT INTO video VALUES ('50ab', '10ab', 'https://www.pexels.com/video/a-beer-in-drinking-glass-sliding-on-bar-counter-5530294/')") """



    connection.commit()

    connection.close()