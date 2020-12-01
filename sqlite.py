# coding=utf-8
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
    lesson_id1 = "3845127e-e6d9-4a15-b6e0-14276ace1cd8"
    lesson_id2 = "618af7ad-3d63-4609-a7f1-50704106b9e4"
    cursor.execute("INSERT INTO lesson VALUES (?, 'Lesson 1', 'This lesson teaches you the most typical words in Finnish. The ones you are likely to encounter everyday in Finland.')", (lesson_id1,))
    cursor.execute("INSERT INTO lesson VALUES (?, 'Lesson 2', 'This lesson acts as your survival kit in Finland, including how to order a beer in Finnish.')", (lesson_id2,))

    #add word test data

    # cursor.execute("INSERT INTO word VALUES (?, ?, 'Moi', 'This is used to greet a Finnish person.', 'Hello')", (word_id, lesson_id1,))
    # cursor.execute("INSERT INTO word VALUES (?, ?, 'Mikä sun nimi on?', 'This sentence helps to inquire what to call the person you just encountered.', 'What's your name?')", (word_id, lesson_id2,))

    # &#228; and ä = ä  &#246; and &ouml; = ö
    
    #add word datat for lesson 1
    words = [
        dict(name="Moi", description="This is used to greet a Finnish person", translation="Hello", audio_url='/static/audio/moi-toni.mp3', video_url='/static/video/moi-nelly-1.m4v'),
        dict(name="Moi moi", description="This is used to wish a person farewell", translation="Bye bye", audio_url='/static/audio/moimoi-toni.mp3', video_url='/static/video/moimoi-sara.mp4'),
        dict(name="Lähetään!", description="Used to suggest to your friend that you should be leaving", translation="Let's go!", audio_url='/static/audio/lähetään-toni.mp3', video_url='/static/video/lähetää-henkka.mp4'),
        dict(name="Nähään!", description="Literal translation: We will see", translation="See you!", audio_url='/static/audio/nähään-toni.mp3', video_url='/static/video/nähään-nelly.m4v'),
        dict(name="Häh?", description="Used when you did not hear what your friend said to you", translation="What?", audio_url='/static/audio/häh-toni.mp3', video_url='/static/video/häh-sara.mp4'),
        dict(name="Mitäs sä?", description="Literal translation: What you?", translation="How are you?", audio_url='/static/audio/mitässä-toni.mp3', video_url='/static/video/mitässä-nelly.m4v'),
        dict(name="Mitäs tässä.", description="Literal translation: What here? This is basically the way to answer the question How are you? without actually giving a proper answer back.", translation="Not bad or Alright", audio_url='/static/audio/mitästässä-toni.mp3', video_url='/static/video/mitästässä-sara.mp4'),
        dict(name="Mitäs ite?", description="Literal translation: What yourself?", translation="And you?", audio_url='/static/audio/mitäsite-toni.mp3', video_url='/static/video/mitäsite-henkka.mp4'),
        dict(name="Kiitos", description="Finnish people give thanks when it is deserved and never only for the sake of saying it.", translation="Thank you", audio_url='/static/audio/kiitos-toni.mp3', video_url='/static/video/kiitos-henkka.mp4'),
        dict(name="Sori", description="Finnish people would use this if they accidentally bumb into you. This is not used for apologising after a serious mess up.", translation="Sorry", audio_url='/static/audio/sori-toni.mp3', video_url='/static/video/sori-sara.mp4'),
        dict(name="Joo", description="The variation to this that has the same meaning is: Juu", translation="Yes", audio_url='/static/audio/joo-toni.mp3', video_url='/static/video/joo-nelly.m4v'),
        dict(name="Ei", description="Use this when you disagree with something a person has said", translation="No", audio_url='/static/audio/ei-toni.mp3', video_url='/static/video/ei-henkka.mp4'),
        dict(name="Ei mitään", description="Literal translation: No nothing. This could be used when you did someone a favour and they thanked you for it.", translation="No problem or It was nothing", audio_url='/static/audio/eimitään-toni.mp3', video_url='/static/video/eimitää-nelly.m4v'),
        dict(name="Ok", description="Pay attention to the Finnish pronounciation of this word", translation="Ok", audio_url='/static/audio/ok-toni.mp3', video_url='/static/video/okei-sara.mp4'),
        dict(name="Selvä", description="This is used to tell someone you have understood the instructions they gave you.", translation="Alright", audio_url='/static/audio/selvä-toni.mp3', video_url='/static/video/selvä-henkka.mp4'),
        dict(name="Jee!", description="This is used to show enthusiasm", translation="Yay!", audio_url='/static/audio/jee-toni.mp3', video_url='/static/video/jee-nelly.m4v'),
        dict(name="Oota!", description="Use this to ask you friend to wait for you", translation="Wait!", audio_url='/static/audio/ootas-toni.mp3', video_url='/static/video/oota-sara.mp4'),
        dict(name="Apua!", description="Use this when you are in a dire need of help", translation="Help!", audio_url='/static/audio/apua-toni.mp3', video_url='/static/video/apua-henkka.mp4'),
        dict(name="Kippis!", description="Used when you raise a toast with someone", translation="Cheers!", audio_url='/static/audio/kippis-toni.mp3', video_url='/static/video/kippis-sara.mp4')
    ]
    for word in words:
        word_id = str(uuid.uuid4())
        cursor.execute("INSERT INTO word VALUES (?,?,?,?,?)", (word_id, lesson_id1, (word["name"].encode().decode('utf8')), (word["description"].encode().decode('utf8')), (word["translation"].encode().decode('utf8')),))
        cursor.execute("INSERT INTO audio VALUES (?,?,?)", (str(uuid.uuid4()), word_id, word["audio_url"],))
        cursor.execute("INSERT INTO video VALUES (?,?,?)", (str(uuid.uuid4()), word_id, word["video_url"],)) 
    
    # &#228; and ä = ä  &#246; and &ouml; = ö

    #add word data for lesson 2
    words = [
        dict(name="Mikä sun nimi on?", description="Direct translation: What your name is?", translation="What's your name?", audio_url='/static/audio/mikäsunnimion-toni.mp3', video_url='/static/video/mikäsunnimion-alarik.mp4'),
        dict(name="Mä oon..", description="Mä is a shortened version from the word minä.", translation="I am..", audio_url='/static/audio/mäoon-toni.mp3', video_url='/static/video/mäoon-alarik.mp4'),
        dict(name="Puhuksä englantii?", description="Direct translation: Speak you English? Sä is a shortened version from sinä.", translation="Do you speak English?", audio_url='/static/audio/puhuksäenglantii-toni.mp3', video_url='/static/video/puhuksäenglantii-iina.m4v'),
        dict(name="Miks?", description="Shortened from Miksi?", translation="Why?", audio_url='/static/audio/miks-toni.mp3', video_url='/static/video/miks-alarik.mp4'),
        dict(name="En tiiä", description="Shortened from En tiedä?", translation="I don't know", audio_url='/static/audio/entiie-toni.mp3', video_url='/static/video/emmätiiä-iina.m4v'),
        dict(name="Emmä usko", description="Direct translation: I don't believe. Shortened from En mä usko", translation="I don't think so", audio_url='/static/audio/enmäusko-toni.mp3', video_url='/static/video/emmäusko-iina.m4v'),
        dict(name="Hienoo!", description="Used when you want to celebrate something.", translation="Great! or Excellent!", audio_url='/static/audio/hienoo-toni.mp3', video_url='/static/video/hienoo-alarik.mp4'),
        dict(name="Onnee!", description="Direct translation: Luck!", translation="Congratulations!", audio_url='/static/audio/onnee-toni.mp3', video_url='/static/video/onnee-iina.m4v'),
        dict(name="Mitä tää tarkottaa?", description="Direct translation: What this means?", translation="What does this mean?", audio_url='/static/audio/mitätäätarkottaa-toni.mp3', video_url='/static/video/mitätäätarkottaa-alarik.mp4'),
        dict(name="Onks teil wifii?", description="Pay attention to the Finnish pronounciation of 'wifii'. Direct translation: Do you(plural) have wifi?", translation="Do you have wifi?", audio_url='/static/audio/onksteilwifii-toni.mp3', video_url='/static/video/onksteilwifii-iina.m4v'),
        dict(name="Mis teil on vessa?", description="Direct translation: Where you(plural) have the bathroom?", translation="Where can I find the bathroom?", audio_url='/static/audio/missäteilonvessa-toni.mp3', video_url='/static/video/misteilonvessa-alarik.mp4'),
        dict(name="Puhun vaa vähä suomee.", description="Direct translation: I speak only less Finnish.", translation="I (can) only speak a little Finnish", audio_url='/static/audio/puhunvaanvähänsuomee-toni.mp3', video_url='/static/video/puhunvaanvähänsuomee-alarik.mp4'),
        dict(name="En tajuu mitää.", description="Direct translation: I don't understand nothing.", translation="I (can't) understand anything.", audio_url='/static/audio/entajuumitään-toni.mp3', video_url='/static/video/entajuumitään-iina.m4v'),
        dict(name="Voiksä puhuu hitaammin?", description="Voiksä shortened from 'Voitko sä'", translation="Can you speak slower?", audio_url='/static/audio/voiksäpuhuuhitaammin-toni.mp3', video_url='/static/video/voiksäpuhuuhitaammin-iina.m4v'),
        dict(name="Voikko jättää mut rauhaan?", description="The nice way of asking someone to leave you alone.", translation="Can you leave me alone?", audio_url='/static/audio/voikkojättäämutrauhaan-toni.mp3', video_url='/static/video/voikkojättäämutrauhaan-alarik.mp4'),
        dict(name="Yks kahvi, kiitos", description="This sentence will get you a Finnish black filter coffee from a cafe. Finnish language doesn't have the word for 'please', so in this case we use 'thank you' instead.", translation="One coffee, thank you", audio_url='/static/audio/ykskahvikiitos-toni.mp3', video_url='/static/video/ykskahvikiitos-alarik.mp4'),
        dict(name="Yks olut, kiitos", description="This sentence will get you a house beer in a bar.", translation="One beer, thank you", audio_url='/static/audio/yksolutkiitos-toni.mp3', video_url='/static/video/yksolutkiitos-alarik.mp4'),
        dict(name="Mä, sä, se", description="Se refers to any one person with any gender.", translation="I, you, she or he or it", audio_url='/static/audio/mäsäse-toni.mp3', video_url='/static/video/mäsäse-iina.m4v'),
        dict(name="Me, te, ne", description="Ne refers to any group of people regardless of their gender.", translation="We, you(plural), they", audio_url='/static/audio/metene-toni.mp3', video_url='/static/video/metene-iina.m4v')
    ]
    for word in words:
        word_id = str(uuid.uuid4())
        cursor.execute("INSERT INTO word VALUES (?,?,?,?,?)", (word_id, lesson_id2, (word["name"].encode().decode('utf8')), (word["description"].encode().decode('utf8')), (word["translation"].encode().decode('utf8')),))
        cursor.execute("INSERT INTO audio VALUES (?,?,?)", (str(uuid.uuid4()), word_id, word["audio_url"],))
        cursor.execute("INSERT INTO video VALUES (?,?,?)", (str(uuid.uuid4()), word_id, word["video_url"],)) 
    
    #add user activity test data

    # cursor.execute("INSERT INTO user_activity VALUES ('20aa', 1603635607, '10aa', '40aa')")
    # cursor.execute("INSERT INTO user_activity VALUES ('20ab', 1604271682, '10aa', '40ab')")

    connection.commit()

    connection.close()