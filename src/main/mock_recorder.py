import os
from http.server import HTTPServer, BaseHTTPRequestHandler

import requests
from src.main.mock_recording import Interaction, MockRecording
from src.main.mock_service import SimpleMarkdownParser


class Recording:

    req_header_title = '### Request headers recorded for playback:'
    req_body_title = '### Request body recorded for playback ():'

    res_header_title = '### Response headers recorded for playback:'


    @staticmethod
    def get_response_body_title(interaction: Interaction):
        return f"### Response body recorded for playback ({interaction.response_code}: {interaction.response_type}):"

    @staticmethod
    def get_interaction_string_title(interaction: Interaction, interactions: [Interaction]) -> str:
        return f'## Interaction {interactions.index(interaction)}: GET {interaction.path}'

    @staticmethod
    def wrap_string(i_string: str):
        return '```\n' + i_string + '\n```'

    @staticmethod
    def headers_to_string(headers: {}):
        return '\n'.join([f'{k}: {v}' for (k, v) in headers.items()])

    def __init__(self):
        self.interactions = []

    def add_interaction(self, interaction : Interaction):
        self.interactions.append(interaction)

    def to_markdown_string(self) -> str:
        lines = []

        for interaction in self.interactions:
            lines.append(self.get_interaction_string_title(interaction, self.interactions))

            lines.append(self.req_header_title)
            lines.append(self.wrap_string(self.headers_to_string(interaction.request_headers)))
            lines.append(self.req_body_title)
            lines.append(self.wrap_string(interaction.request_body if not '' else '\n'))  # if empty \n else

            lines.append(self.res_header_title)
            lines.append(self.wrap_string(self.headers_to_string(interaction.response_headers)))

            lines.append(self.get_response_body_title(interaction))
            lines.append(self.wrap_string(interaction.response_body))

        return '\n\n'.join(lines)


class RecorderHttpHandler(BaseHTTPRequestHandler):
    host = "http://climatedataapi.worldbank.org"
    invoking_method = 'default_value_rec'
    current_recording = Recording()

    @staticmethod
    def set_invoking_method(method_name):
        RecorderHttpHandler.invoking_method = method_name
        RecorderHttpHandler.current_recording = Recording()

    def do_GET(self):

        r_headers = self.headers
        replace_values = {'User-Agent': 'Servirtium-Testing', 'Host': self.host.replace('http://', '')}

        for k, v in r_headers.items():
            if k in replace_values.keys():
                del(r_headers[k])
                r_headers[k] = replace_values[k]

        test_file = SimpleMarkdownParser.get_recording_from_name(RecorderHttpHandler.invoking_method, mock_recordings)
        response = requests.get(RecorderHttpHandler.host + self.path, headers=r_headers)

        self.send_response(response.status_code)
        self.end_headers()
        self.wfile.write(response.content)

        RecorderHttpHandler.current_recording.add_interaction(Interaction(request_headers=r_headers, request_body='\n', request_path=self.path,
                                                                          response_headers=response.headers, response_body=(str(response.content, encoding='utf-8')),
                                                                          response_code=response.status_code))

        if len(RecorderHttpHandler.current_recording.interactions) == len(test_file.interactions): # Last interaction
            f = open(RecorderHttpHandler.invoking_method + ".md", "w+")
            f.write(RecorderHttpHandler.current_recording.to_markdown_string())
            f.close()


parser = SimpleMarkdownParser()
mock_recordings = parser.get_recordings(os.path.dirname(os.path.realpath(__file__)).replace('main', 'mocks'))


def set_real_host(host):
    RecorderHttpHandler.host = host


def start():
    server_address = ('localhost', 8099)
    httpd = HTTPServer(server_address, RecorderHttpHandler)
    httpd.serve_forever()


if __name__ == "__main__":
    start()


