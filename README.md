Note - The World Bank took down their climate WebAPI. Darn it. We now depend on a docker version of the same until we work out what to do long term. Docker build and deploy this locally - https://github.com/servirtium/worldbank-climate-recordings - see README

TL;DR:

```
docker build git@github.com:servirtium/worldbank-climate-recordings.git#main -t worldbank-weather-api-for-servirtium-development
docker run -d -p 4567:4567 worldbank-weather-api-for-servirtium-development
```

The build for this demo project needs that docker container running

## setup

This requires Python3, and a locally installed 'servirtium-python' library. 
See https://github.com/servirtium/servirtium-python. 

Install all required packages using:
```
pip3 install -r requirements.txt
```

## Running the climate API tests directly against World Bank's Climate HTTP API.

```
python3 -m pytest src/test/TestClimateApi.py
```

That runs six tests, which should all pass, directly 
targeting a WHO climate API. And specifically, there's no Servirtium involved in that.

## Tests with playing back previously recorded World Bank's Climate HTTP API, via Servirtium

```
python3 -m pytest src/test/TestPlaybackClimateApi.py
```

That runs six tests, which should all pass again. This 
time using a pre-recorded interactions with that Word Bank
climate API, instead of the real thing.

(actually it runs 12 tests, but we can't work out how
to make it run only the 5 subclass test methods)

## Tests that re-record World Bank's Climate HTTP API, via Servirtium

```
python3 -m pytest src/test/TestRecordingClimateApi.py
```

Again this runs six tests, which all pass again. Check the src/mocks/ folder after the
tests have run.

## Credits:

Ross Fang for the porting of the Java example at 
https://github.com/paul-hammant/climate-data-tck (via UpWork)
