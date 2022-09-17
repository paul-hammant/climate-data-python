import inspect
import threading

import servirtium.playback as MockService
from servirtium.markdown_parser import get_markdown_file_strings

from definitions import ROOT_DIR
from src.test.test_ClimateApi import TestClimateApi


class TestPlaybackClimateApi(TestClimateApi):
    # mock server is man-in-the-middle, overriding real site
    site = "http://servirtium.local.gd:61417"

    # mock_recordings = parser.get_recordings(os.path.dirname(os.path.realpath(__file__)).replace('main', 'mocks'))

    files = get_markdown_file_strings(ROOT_DIR + "/src/mocks")
    MockService.parser._set_mock_files(files)

    thread1 = threading.Thread(target=MockService.start, daemon=True)
    thread1.start()

    def test_averageRainfallForGreatBritainFrom1980to1999Exists(self):
        MockService.MockServiceHttpHandler.set_markdown_filename(inspect.stack()[0][3])
        super().test_averageRainfallForGreatBritainFrom1980to1999Exists()

    def test_averageRainfallForFranceFrom1980to1999Exists(self):
        MockService.MockServiceHttpHandler.set_markdown_filename(inspect.stack()[0][3])
        super().test_averageRainfallForFranceFrom1980to1999Exists()

    def test_averageRainfallForEgyptFrom1980to1999Exists(self):
        MockService.MockServiceHttpHandler.set_markdown_filename(inspect.stack()[0][3])
        super().test_averageRainfallForEgyptFrom1980to1999Exists()

    def test_averageRainfallForGreatBritainFrom1985to1995DoesNotExist(self):
        MockService.MockServiceHttpHandler.set_markdown_filename(inspect.stack()[0][3])
        super().test_averageRainfallForGreatBritainFrom1985to1995DoesNotExist()

    def test_averageRainfallForMiddleEarthFrom1980to1999DoesNotExist(self):
        MockService.MockServiceHttpHandler.set_markdown_filename(inspect.stack()[0][3])
        super().test_averageRainfallForMiddleEarthFrom1980to1999DoesNotExist()

    def test_averageRainfallForGreatBritainAndFranceFrom1980to1999CanBeCalculatedFromTwoRequests(self):
        MockService.MockServiceHttpHandler.set_markdown_filename(inspect.stack()[0][3])
        super().test_averageRainfallForGreatBritainAndFranceFrom1980to1999CanBeCalculatedFromTwoRequests()
