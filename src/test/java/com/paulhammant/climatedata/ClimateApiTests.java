package com.paulhammant.climatedata;

import org.junit.Before;
import org.junit.Test;

import static com.paulhammant.climatedata.ClimateApi.DEFAULT_CLIMATE_API_SITE;
import static org.junit.Assert.assertEquals;
import static org.junit.Assert.fail;

public class ClimateApiTests {

    private ClimateApi climateApi;

    void setSite(String site) {
        climateApi = new ClimateApi(site);
    }

    /*
     See overrides of this method in RecordingClimateApiTests and PlaybackClimateApiTests
     */
    @Before
    public void startup() {

        setSite(DEFAULT_CLIMATE_API_SITE);
    }

    @Test
    public void averageRainfallForGreatBritainFrom1980to1999Exists() {

        assertEquals(988.8454972331015,
                climateApi.getAveAnnualRainfall(1980, 1999, "gbr"), 0);
    }

    @Test
    public void averageRainfallForFranceFrom1980to1999Exists() {

        assertEquals(913.7986955122727,
                climateApi.getAveAnnualRainfall(1980, 1999, "fra"), 0);
    }

    @Test
    public void averageRainfallForEgyptFrom1980to1999Exists() {

        assertEquals(54.58587712129825,
                climateApi.getAveAnnualRainfall(1980, 1999, "egy"), 0);
    }

    @Test
    public void averageRainfallForGreatBritainFrom1985to1995DoesNotExist() {

        // wrong date ranges just return an empty list of data -
        try {
            climateApi.getAveAnnualRainfall(1985, 1995, "gbr");
            fail("should have failed in line above");
        } catch (UnsupportedOperationException e) {
            assertEquals("date range 1985-1995 not supported", e.getMessage());
        }
    }

    @Test
    public void averageRainfallForMiddleEarthFrom1980to1999DoesNotExist() {

        try {
            climateApi.getAveAnnualRainfall(1980, 1999, "mde");
            fail("should have failed in line above");
        } catch (UnsupportedOperationException e) {
            assertEquals("mde not recognized by climateweb", e.getMessage());
        }
    }

}
