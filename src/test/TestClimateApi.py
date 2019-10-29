import pytest

from src.main.ClimateApi import ClimateApi


class TestClimateApi:

    site = ClimateApi.CLIMATE_API_SITE

    @pytest.fixture(autouse=True)
    def startup(self):
        self.climateApi = ClimateApi(self.site)

    def test_averageRainfallForGreatBritainFrom1980to1999Exists(self):
        assert self.climateApi.getAveAnnualRainfall(1980, 1999, "gbr") == 988.8454972331015

    def test_averageRainfallForFranceFrom1980to1999Exists(self):
        assert self.climateApi.getAveAnnualRainfall(1980, 1999, "fra") == 913.7986955122727

    def test_averageRainfallForEgyptFrom1980to1999Exists(self):
        assert self.climateApi.getAveAnnualRainfall(1980, 1999, "egy") == 54.58587712129825

    def test_averageRainfallForGreatBritainFrom1985to1995DoesNotExist(self):
        with pytest.raises(AttributeError) as execinfo:
            self.climateApi.getAveAnnualRainfall(1985, 1995, "gbr")
        assert "date range 1985-1995 not supported" in execinfo.value.args[0]

    def test_averageRainfallForMiddleEarthFrom1980to1999DoesNotExist(self):
        with pytest.raises(AttributeError) as excinfo:
            self.climateApi.getAveAnnualRainfall(1980, 1999, "mde")
        assert "not recognized by climateweb" in excinfo.value.args[0]

    def test_averageRainfallForGreatBritainAndFranceFrom1980to1999CanBeCalculatedFromTwoRequests(self):
        rainfall = self.climateApi.getAveAnnualRainfall(1980, 1999, "gbr", "fra")
        assert rainfall == 951.3220963726872

