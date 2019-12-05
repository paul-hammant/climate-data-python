
class Interaction:

    def __init__(self, request_path, request_headers: {}, response_headers: {},
                 request_body='', response_body=''):
        self.path = request_path
        self.request_body = request_body
        self.request_headers = request_headers
        self.response_headers = response_headers
        self.response_body = response_body


class MockRecording:

    def __init__(self, file_name, interactions : [Interaction]):
        self.file_name = file_name
        self.interactions = interactions



