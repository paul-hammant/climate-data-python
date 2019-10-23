## Running it

This requires JDK 12 (or above) and Maven 3.6.1+ (or above) to run.

Running the tests directly against the the World Bank's Climate API (http://climatedataapi.worldbank.org)

```
mvn clean install
```

This runs five tests.

# The job is port it all to Python3 with Pytest tests.

## The API class should be re-usable

* src/main/java/com/paulhammant/climatedata/ClimateApi.java

## There are also the test classes:

* src/test/java/com/paulhammant/climatedata/ClimateApiTests.java

## These two classes are hack for Java's XStream:

* src/main/java/com/paulhammant/climatedata/domain/web/AnnualData.java
* src/main/java/com/paulhammant/climatedata/domain/web/AnnualGcmDatum.java

They need not be replicated for Python if there is a better way.
