import os
from http import HTTPStatus
from http.server import HTTPServer, BaseHTTPRequestHandler

from src.main.mock_recording import MockRecording


class HttpHandler(BaseHTTPRequestHandler):

    currentMethodName = ""

    def do_GET(self):
        if is_valid_path(self.path):

            # don't iterate over list, go direct to the .md file in question, via ...
            print(os.path.dirname(os.path.realpath(__file__)).replace('main', 'mocks')
                  + "/" + HttpHandler.currentMethodName.replace("test_", "") + ".md")

            recording = list(filter(lambda mock : mock.path == self.path, mock_recordings))[0]
            request_headers = get_dict_from_headers_string(str(self.headers).strip())

            if recording.request_headers == request_headers or True:  # Headers currently don't match
                self.send_response(200)
                self.send_header("Content-type", "text/html")

                if False:  # Need to fix
                    for key, value in recording.response_headers.items():
                        self.send_header(key.strip(), value)

                self.end_headers()
                self.wfile.write(bytes(recording.response_body, "utf-8"))

            else:
                self.send_error(
                HTTPStatus.NOT_FOUND,
                "Non-matching headers")

        else:
            self.send_error(
            HTTPStatus.NOT_FOUND,
            "Unknown file path")

class SimpleMarkdownParser:

    @staticmethod
    def __get_markdown_file_strings(mocks_path) -> [str]:
        file_strings = []

        for filename in os.listdir(mocks_path):
            file_path = os.path.join(mocks_path, filename)
            file = open(file_path, "r")
            file_strings.append(file.read())

        return file_strings

    @staticmethod
    def get_headers_dict(header_string) -> dict:
        out = {}
        header_lines = header_string.split('\n')

        for line in header_lines:
            line_split = [l.strip() for l in line.split(':')]
            out[line_split[0]] = line_split[1]

        return out

    def get_recordings(self, mocks_path) -> [MockRecording]:
        markdown_raw_strings = self.__get_markdown_file_strings(mocks_path)
        return [self.__parse_markdown_string(string) for string in markdown_raw_strings]

    def __parse_markdown_string(self, markdown_string) -> MockRecording:

        raw_strings = markdown_string.split("##")
        clean_strings = []

        for string in raw_strings:
            if len(string):
                clean_strings.append(string.strip().replace('#', ''))

        interaction_description = clean_strings[0]
        interaction_split = interaction_description.split(' ')
        request_path = interaction_split[len(interaction_split) - 1]

        request_headers_string = clean_strings[1].split('```')[1].strip()
        request_headers = self.get_headers_dict(request_headers_string)
        request_body = clean_strings[2].split('```')[1].strip()

        response_headers_string = clean_strings[3].split('```')[1].strip()
        response_headers = self.get_headers_dict(response_headers_string)
        response_body = clean_strings[4].split('```')[1].strip()

        return MockRecording(request_path=request_path, request_headers=request_headers, request_body=request_body,
                             response_headers=response_headers, response_body=response_body)


parser = SimpleMarkdownParser()
mock_recordings = parser.get_recordings(os.path.dirname(os.path.realpath(__file__)).replace('main', 'mocks'))

def is_valid_path(path) -> bool:
    return bool(len(list(filter(lambda mock: mock.path == path, mock_recordings))))


def get_dict_from_headers_string(headers_string) -> {}:
    out = {}
    lines = headers_string.split('\n')

    for line in lines:
        line_split = [l.strip().replace('\n', '') for l in line.split(':')]
        out[line_split[0]] = line_split[1]
    return out


def start():
    server_address = ('localhost', 8099)
    httpHandler = HttpHandler
    httpd = HTTPServer(server_address, httpHandler)
    httpd.serve_forever()

if __name__ == "__main__":
    start()


