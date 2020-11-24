__author__='suvihelin'

import uuid

class Video(object):

    def __init__(self, word_id, content_url, video_id=None):
        self.word_id = word_id
        self.content_url = content_url
        self.video_id = str(uuid.uuid4()) if video_id is None else video_id
