# flights.May2018-April2020.csv and flights.May2017-Apr2018.csv Metadata

## Information about the flights.May2018-April2020.csv and flights.May2017-Apr2018.csv file

### File availability

These two files are too large to host in github. They are available via these Dropbox links:

* [`flights.May2017-Apr2018.csv`](https://www.dropbox.com/s/jizx4ijnpxmi3av/flights.May2017-Apr2018.csv?dl=0)
* [`flights.May2018-April2020.csv`](https://www.dropbox.com/s/r9ygw12bp2f6aml/flights.May2018-April2020.csv?dl=0)

These files contain US commercial flight on-time arrival information from the [Bureau of Transportation Statistics](https://www.transtats.bts.gov/DL_SelectFields.asp).

The data are from two time frames:

* `flights.May2017-Apr2018.csv`: data are from May 2017 to April 2018. Downloaded July 19, 2018.
* `flights.May2018-April2020.csv`: data are from May 2018 to April 20202. Downloaded July 31, 2020.

Unfortunately, one of the data columns in the two files is different. For the 2017-2018 data, the second column is a numeric code for the airline. While in the 2018-2020 data, it is a letter code for the airline. The rest of the columns should be identical. But due to the difference, the two files were not combined.

The columns in the dataset are in the table below.

Column #|Column header | Description
--------|--------------|------------
1|FL_DATE | Date of the flight
2|2017-2018 file: AIRLINE_ID <br><br> 2018-2020 file: OP_UNIQUE_CARRIER | An identification |number assigned by US DOT to identify a unique airline (carrier). <br><br> Unique Carrier Code
3|ORIGIN | Origin Airport
4|ORIGIN_CITY_NAME | Origin Airport, City Name **Note that this column has a comma in it**
5|ORIGIN_STATE_ABR | Origin Airport, State Code
6|DEST | Destination Airport
7|DEST_CITY_NAME | Destination Airport, City Name **Note that this column has a comma in it**
8|DEST_STATE_ABR | Destination Airport, State Code
9|DEP_TIME | Actual Departure Time (local time: hhmm)
10|DEP_DELAY_NEW | Difference in minutes between scheduled and actual departure time. Early |departures set to 0.
11|DEP_DEL15 | Departure Delay Indicator, 15 Minutes or More (1.00=Yes, 0.00=No)
12|ARR_TIME | Actual Arrival Time (local time: hhmm)
13|ARR_DELAY_NEW | Difference in minutes between scheduled and actual arrival time. Early |arrivals set to 0.
14|ARR_DEL15 | Arrival Delay Indicator, 15 Minutes or More (1.00=Yes, 0.00=No)
15|CANCELLED | Cancelled Flight Indicator (1=Yes)
16|CANCELLATION_CODE | Specifies The Reason For Cancellation
17|DIVERTED | Diverted Flight Indicator (1=Yes)
18|AIR_TIME | Flight Time, in Minutes
19|FLIGHTS | Number of Flights
20|DISTANCE | Distance between airports (miles)
21|CARRIER_DELAY | Carrier Delay, in Minutes
22|WEATHER_DELAY | Weather Delay, in Minutes
23|NAS_DELAY | National Air System Delay, in Minutes
24|SECURITY_DELAY | Security Delay, in Minutes
25|LATE_AIRCRAFT_DELAY | Late Aircraft Delay, in Minutes
