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
    """     lesson_id1 = str(uuid.uuid4())
    lesson_id2 = str(uuid.uuid4())
    cursor.execute("INSERT INTO lesson VALUES (?, 'Lesson 1', 'This lesson teaches you the most typical words in Finnish. The ones you are likely to encounter everyday in Finland.')", (lesson_id1,))
    cursor.execute("INSERT INTO lesson VALUES (?, 'Lesson 2', 'This lesson acts as your survival kit in Finland, including how to order a beer in Finnish.')", (lesson_id2,)) """

    #add word test data

    """ cursor.execute("INSERT INTO word VALUES (?, ?, 'Moi', 'This is used to greet a Finnish person.', 'Hello')", (word_id, lesson_id1,))
    cursor.execute("INSERT INTO word VALUES (?, ?, 'Mikä sun nimi on?', 'This sentence helps to inquire what to call the person you just encountered.', 'What's your name?')", (word_id, lesson_id2,)) """

    # &#228; and ä = ä  &#246; and &ouml; = ö
    
    #add word datat for lesson 1
    """     words = [
        dict(name="Moi", description="This is used to greet a Finnish person", translation="Hello"),
        dict(name="Moi moi", description="This is used to wish a person farewell", translation="Bye bye"),
        dict(name="Lähetään!", description="Used to suggest to your friend that you should be leaving", translation="Let's go!"),
        dict(name="Nähään!", description="Literal translation: We will see", translation="See you!"),
        dict(name="Häh?", description="Used when you did not hear what your friend said to you", translation="What?"),
        dict(name="Mitäs sä?", description="Literal translation: What you?", translation="How are you?"),
        dict(name="Mitäs tässä?", description="Literal translation: What here? This is basically the way to answer the question How are you? without actually giving a proper answer back.", translation="Not bad or Alright"),
        dict(name="Mitäs ite?", description="Literal translation: What yourself?", translation="And you?"),
        dict(name="Kiitos", description="Finnish people give thanks when it is deserved and never only for the sake of saying it.", translation="Thank you"),
        dict(name="Sori", description="Finnish people would use this if they accidentally bumb into you. This is not used for apologising after a serious mess up.", translation="Sorry"),
        dict(name="Joo", description="The variation to this that has the same meaning is: Juu", translation="Yes"),
        dict(name="Ei", description="Use this when you disagree with something a person has said", translation="No"),
        dict(name="Ei mitään", description="Literal translation: No nothing. This could be used when you did someone a favour and they thanked you for it.", translation="No problem or It was nothing"),
        dict(name="Ok", description="Pay attention to the Finnish pronounciation of this word", translation="Ok"),
        dict(name="Selvä", description="This is used to tell someone you have understood the instructions they gave you.", translation="Alright"),
        dict(name="Jee!", description="This is used to show enthusiasm", translation="Yay!"),
        dict(name="Oota!", description="Use this to ask you friend to wait for you", translation="Wait!"),
        dict(name="Apua!", description="Use this when you are in a dire need of help", translation="Help!"),
        dict(name="Kippis!", description="Used when you raise a toast with someone", translation="Cheers!")
    ]
    for word in words:
        cursor.execute("INSERT INTO word VALUES (?,?,?,?,?)", (str(uuid.uuid4()), lesson_id1, unicode(word["name"].decode('utf8')), unicode(word["description"].decode('utf8')), unicode(word["translation"].decode('utf8')),))
    """
    # &#228; and ä = ä  &#246; and &ouml; = ö

    #add word data for lesson 2
    """     words = [
        dict(name="Mikä sun nimi on?", description="Direct translation: What your name is?", translation="What's your name?"),
        dict(name="Mä oon..", description="Mä is a shortened version from the word minä.", translation="I am.."),
        dict(name="Puhuksä englantii?", description="Direct translation: Speak you English? Sä is a shortened version from sinä.", translation="Do you speak English?"),
        dict(name="Miks?", description="Shortened from Miksi?", translation="Why?"),
        dict(name="En tiiä", description="Shortened from En tiedä?", translation="I don't know"),
        dict(name="Emmä usko", description="Direct translation: I don't believe. Shortened from En mä usko", translation="I don't think so"),
        dict(name="Hienoo!", description="Used when you want to celebrate something.", translation="Great! or Excellent!"),
        dict(name="Onnee!", description="Direct translation: Luck!", translation="Congratulations!"),
        dict(name="Mitä tää tarkottaa?", description="Direct translation: What this means?", translation="What does this mean?"),
        dict(name="Onks teil wifii?", description="Pay attention to the Finnish pronounciation of 'wifii'. Direct translation: Do you(plural) have wifi?", translation="Do you have wifi?"),
        dict(name="Mis teil on vessa?", description="Direct translation: Where you(plural) have the bathroom?", translation="Where can I find the bathroom?"),
        dict(name="Puhun vaa vähä suomee.", description="Direct translation: I speak only less Finnish.", translation="I (can) only speak a little Finnish"),
        dict(name="En tajuu mitää.", description="Direct translation: I don't undestand nothing.", translation="I (can't) understand anything."),
        dict(name="Voiksä puhuu hitaammin?", description="Voiksä shortened from 'Voitko sä'", translation="Can you speak slower?"),
        dict(name="Voikko jättää mut rauhaan?", description="The nice way of asking someone to leave you alone.", translation="Can you leave me alone?"),
        dict(name="Yks kahvi, kiitos", description="This sentence will get you a Finnish black filter coffee from a cafe. Finnish language doesn't have the word for 'please', so in this case we use 'thank you' instead.", translation="One coffee, thank you"),
        dict(name="Yks olut, kiitos", description="This sentence will get you a house beer in a bar.", translation="One beer, thank you"),
        dict(name="Mä, sä, se", description="Se refers to any one person with any gender.", translation="I, you, she or he or it"),
        dict(name="Me, te, ne", description="Ne refers to any group of people regardless of their gender.", translation="We, you(plural), they")
    ]
    for word in words:
        cursor.execute("INSERT INTO word VALUES (?,?,?,?,?)", (str(uuid.uuid4()), lesson_id2, unicode(word["name"].decode('utf8')), unicode(word["description"].decode('utf8')), unicode(word["translation"].decode('utf8')),)) """
    
    #add user activity test data

    """ cursor.execute("INSERT INTO user_activity VALUES ('20aa', 1603635607, '10aa', '40aa')")
    cursor.execute("INSERT INTO user_activity VALUES ('20ab', 1604271682, '10aa', '40ab')") """

    #add audio data for lesson1

    #audio_id, word_id, content_url
    """     audio_files = [
        dict(word_id='1a127cf9-354a-4262-8183-8c52f4d1dcac', content_url='/static/audio/moi-toni.mp3'),
        dict(word_id='323c03b5-8255-4c69-b9d1-074b5c629362', content_url='/static/audio/moimoi-toni.mp3'),
        dict(word_id='c6b0cf3d-4a06-415b-b558-de4a88643d96', content_url='/static/audio/lähetään-toni.mp3'),
        dict(word_id='33bfba8b-d9c6-4b8b-8e9e-0aa811f14c28', content_url='/static/audio/nähään-toni.mp3'),
        dict(word_id='c26a4365-c03c-4e63-92d9-2edc82cc3554', content_url='/static/audio/häh-toni.mp3'),
        dict(word_id='594e51ea-a36a-4248-a087-95c3beec2abc', content_url='/static/audio/mitässä-toni.mp3'),
        dict(word_id='cbf8ef17-54dd-48e1-a7ea-1c2444551973', content_url='/static/audio/mitästässä-toni.mp3'),
        dict(word_id='d25af6fc-925d-439a-9c46-d13511b31b61', content_url='/static/audio/mitäsite-toni.mp3'),
        dict(word_id='63f7535e-4656-4624-b3f3-5035fc996055', content_url='/static/audio/kiitos-toni.mp3'),
        dict(word_id='a7781d82-805e-4b86-9ba8-bcd82c1af49a', content_url='/static/audio/sori-toni.mp3'),
        dict(word_id='6d554275-2ba5-4909-baf7-954fe1176275', content_url='/static/audio/joo-toni.mp3'),
        dict(word_id='8db24552-025b-4d11-8b0c-8f0df6988db8', content_url='/static/audio/ei-toni.mp3'),
        dict(word_id='75cdeddc-b279-45d6-b4d4-831173edb416', content_url='/static/audio/eimitään-toni.mp3'),
        dict(word_id='2207b170-ad80-47d0-a9ad-27f5bc80082f', content_url='/static/audio/ok-toni.mp3'),
        dict(word_id='bf77a9b7-bb9d-4203-b1b1-7217b2aec00b', content_url='/static/audio/selvä-toni.mp3'),
        dict(word_id='dd15748e-da29-42b9-a221-fb6add230ab7', content_url='/static/audio/jee-toni.mp3'),
        dict(word_id='0e14acf7-39a8-4cee-b03b-fd804f1dc25f', content_url='/static/audio/ootas-toni.mp3'),
        dict(word_id='7d986d3c-bc33-4a7f-8004-9296a1dac196', content_url='/static/audio/apua-toni.mp3'),
        dict(word_id='f8706ba2-e3bb-4583-b2ac-d92d93e541ef', content_url='/static/audio/kippis-toni.mp3'),
    ]
    for audio in audio_files:
        cursor.execute("INSERT INTO audio VALUES (?,?,?)", (str(uuid.uuid4()), audio["word_id"], audio["content_url"],))
    """
    #add audio data for lesson2

    #audio_id, word_id, content_url
    """     audio_files = [
        dict(word_id='139982c8-6d5e-432a-bc43-6172ae8662f3', content_url='/static/audio/mikäsunnimion-toni.mp3'),
        dict(word_id='ca22da25-4fb1-48a8-a2c0-72b792d2ad2a', content_url='/static/audio/mäoon-toni.mp3'),
        dict(word_id='f59eef12-89ff-464f-8b8a-54b903c55740', content_url='/static/audio/puhuksäenglantii.mp3'), #suvi -file
        dict(word_id='d0ca5c6b-3e9f-4e1c-bd5e-65ae1e0d33a8', content_url='/static/audio/miks-toni.mp3'),
        dict(word_id='cda227a5-aaca-4716-888e-f367a87787b5', content_url='/static/audio/entiie-toni.mp3'),
        dict(word_id='d3ee8f93-7a1c-4b7e-badd-ee74d063b44d', content_url='/static/audio/enmäusko-toni.mp3'),
        dict(word_id='b64eb9b3-d50c-44dc-bbc6-d42852035294', content_url='/static/audio/hienoo-toni.mp3'),
        dict(word_id='95fa103c-68fe-4623-8682-15c4a872b8ce', content_url='/static/audio/onnee-toni.mp3'),
        dict(word_id='37482b31-ed8c-4ee6-be6c-ec48ad4a35c5', content_url='/static/audio/mitätäätarkottaa-toni.mp3'),
        dict(word_id='b7e6306e-670c-43ba-bb1f-7957ca389b35', content_url='/static/audio/onksteilwifii-toni.mp3'),
        dict(word_id='b0d0115b-1eeb-4092-99b5-4dbf5b93cc8d', content_url='/static/audio/missäteilonvessa-toni.mp3'),
        dict(word_id='9e225f87-e0bd-4381-8b3c-cf8e7717597b', content_url='/static/audio/puhunvaanvähänsuomee-toni.mp3'),
        dict(word_id='f05d1ab0-25d7-4b66-9d4a-0c0f0a3d1b7e', content_url='/static/audio/entajuumitään-toni.mp3'),
        dict(word_id='6d1dd8b0-8ea7-40b2-a137-9fbd82d33513', content_url='/static/audio/voiksäpuhuuhitaammin-toni.mp3'),
        dict(word_id='5a50ae2c-4610-4677-9f68-3f9847149e2f', content_url='/static/audio/voikkojättäämutrauhaan-toni.mp3'),
        dict(word_id='3b0c7b7c-1e69-46e3-9aa7-2776c3f070f3', content_url='/static/audio/ykskahvikiitos-toni.mp3'),
        dict(word_id='b1dbdd53-dc2c-47ad-bfcc-62f9b8e27e63', content_url='/static/audio/yksolutkiitos-toni.mp3'),
        dict(word_id='78b6883d-0052-40ee-882c-4d1b0ad80403', content_url='/static/audio/mäsäse-toni.mp3'),
        dict(word_id='86592ec8-8816-49a7-a43b-c72e1597f82b', content_url='/static/audio/metene-toni.mp3')

    ]
    for audio in audio_files:
        cursor.execute("INSERT INTO audio VALUES (?,?,?)", (str(uuid.uuid4()), audio["word_id"], audio["content_url"],))
    """

    #add video data

    video_id = str(uuid.uuid4())
    cursor.execute("INSERT INTO video VALUES (?, '1a127cf9-354a-4262-8183-8c52f4d1dcac', '/static/video/moi-nelly-1.m4v')", (video_id,))

    """    video_files = [
        dict(word_id='1a127cf9-354a-4262-8183-8c52f4d1dcac', content_url='/static/video/moi-nelly.mov')


    ]
    for video in video_files:
        cursor.execute("INSERT INTO video VALUES (?,?,?)", (str(uuid.uuid4()), video["word_id"], video["content_url"],))

    """
    connection.commit()

    connection.close()