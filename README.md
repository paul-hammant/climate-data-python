## Running it

This requires Python3

```
pip3 install pytest requests
python3 -m pytest src/test/TestClimateApi.py
```

That runs five tests, which should all pass, directly 
targeting a WHO climate API.

Next, try this:

```
python3 -m pytest src/test/TestPlaybackClimateApi.py
```

That runs five tests, which should all pass, this 
time using a pre-recorded interaction with that WHO
climate API, instead of the real thing.

(actually it runs 10 tests, but we can't work out how
to make it run only the 5 subclass test methods)

## Credits:

Ross Fang for the porting of the Java example at 
https://github.com/paul-hammant/climate-data-tck (via UpWork)