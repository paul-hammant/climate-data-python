import os
import threading

import pytest
import src.main.mock_service as MockService
from src.test.ClimateApiTests import TestClass


class TestPlayback(TestClass):

    site = "http://localhost:8099"
    thread1 = threading.Thread(target=MockService.start, daemon=True)
    thread1.start()

    if __name__ == "__main__":
        try:
            pytest.main(["-x", os.getcwd()+"/PlaybackClimateApiTests.py"])
        finally:
            os._exit(1)



