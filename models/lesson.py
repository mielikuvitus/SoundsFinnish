__author__='suvihelin'

import uuid

class Lesson(object):

    def __init__(self, name, description, lesson_id=None):
        self.name = name
        self.description = description
        self.lesson_id = str(uuid.uuid4()) if lesson_id is None else lesson_id