__author__='suvihelin'

import uuid

class Word(object):

    def __init__(self, lesson_id, name, description, translation, word_id=None):
        self.lesson_id = lesson_id
        self.name = name
        self.description = description
        self.translation = translation
        self.word_id = str(uuid.uuid4()) if word_id is None else word_id

