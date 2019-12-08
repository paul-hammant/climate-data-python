import inspect
import os
import sys
import threading

import pytest
import src.main.mock_service as MockService
from src.test.TestClimateApi import TestClimateApi


class TestPlaybackClimateApi(TestClimateApi):

    # mock server is man-in-the-middle, overriding real site
    site = "http://localhost:8099"

    thread1 = threading.Thread(target=MockService.start, daemon=True)
    thread1.start()

    if __name__ == "__main__":
        try:
            pytest.main(["-x", os.getcwd()+"/TestPlaybackClimateApi.py"])
        finally:
            os._exit(1)

    def test_averageRainfallForGreatBritainFrom1980to1999Exists(self):
        MockService.MockServiceHttpHandler.set_invoking_method(inspect.stack()[0][3])
        super().test_averageRainfallForGreatBritainFrom1980to1999Exists()

    def test_averageRainfallForFranceFrom1980to1999Exists(self):
       MockService.MockServiceHttpHandler.set_invoking_method(inspect.stack()[0][3])
       super().test_averageRainfallForFranceFrom1980to1999Exists()

    def test_averageRainfallForEgyptFrom1980to1999Exists(self):
        MockService.MockServiceHttpHandler.set_invoking_method(inspect.stack()[0][3])
        super().test_averageRainfallForEgyptFrom1980to1999Exists()

    def test_averageRainfallForGreatBritainFrom1985to1995DoesNotExist(self):
        MockService.MockServiceHttpHandler.set_invoking_method(inspect.stack()[0][3])
        super().test_averageRainfallForGreatBritainFrom1985to1995DoesNotExist()

    def test_averageRainfallForMiddleEarthFrom1980to1999DoesNotExist(self):
        MockService.MockServiceHttpHandler.set_invoking_method(inspect.stack()[0][3])
        super().test_averageRainfallForMiddleEarthFrom1980to1999DoesNotExist()

    def test_averageRainfallForGreatBritainAndFranceFrom1980to1999CanBeCalculatedFromTwoRequests(self):
        MockService.MockServiceHttpHandler.set_invoking_method(inspect.stack()[0][3])
        super().test_averageRainfallForGreatBritainAndFranceFrom1980to1999CanBeCalculatedFromTwoRequests()


