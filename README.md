# A Zipcode API App for my [Weather App](https://github.com/OwenKoehler/weather-react)

## Running the App

Running requires flask and pymysql.
These can be installed with:

```sudo apt-get install python3-flask```

```sudo apt-get install python3-pymysql```

You must also edit MySQL configuration in db_config.py to correspond to your MySQL DB.

In my case, the DB was named "weather" and the table "zipcodes".

My table contained 2 columns: ID(INT) and ZIP(CHAR).

Finally, run the app with:

```FLASK_APP=hello.py flask run```