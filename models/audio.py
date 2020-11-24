__author__='suvihelin'

import uuid

class Audio(object):

    def __init__(self, word_id, content_url, audio_id=None):
        self.word_id = word_id
        self.content_url = content_url
        self.audio_id = str(uuid.uuid4()) if audio_id is None else audio_id
