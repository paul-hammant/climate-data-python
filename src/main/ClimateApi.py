import requests
import xml.etree.ElementTree as ET


class ClimateApi:

    DEFAULT_CLIMATE_API_SITE = "http://climatedataapi.worldbank.org"
    LOCAL_HOST = "http://localhost:8099"

    def __init__(self, site):
        self.site = site

    def getAveAnnualRainfall(self, fromCCYY : int, toCCYY : int, countryISO : str) -> float:
        url = self.site + f"/climateweb/rest/v1/country/annualavg/pr/{fromCCYY}/{toCCYY}/{countryISO}.xml"

        try:
            request = requests.get(url)
            request_text = request.text
            if "Invalid country code. Three letters are required" in request_text:
                raise AttributeError(f"{countryISO} not recognized by climateweb")
            root = ET.fromstring(request_text)
        except requests.exceptions.RequestException as e:
            raise Exception(f"Exception occurred when parsing XML : {e})")

        datums = root.findall('domain.web.AnnualGcmDatum')
        total = 0
        for element in datums:
            tst = element.find('annualData')
            total += float(tst.find('double').text)

        if len(datums) == 0:
            raise AttributeError(f"date range {fromCCYY}-{toCCYY} not supported")

        return total / len(datums)