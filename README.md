## Exchange Rates:

Use exchangeratesapi.io https://exchangeratesapi.io/to get the API of exchange rates from 01.01.2019 till 01.12.2019 and download the data into DB

### Notes

- The base currencies are USD and EUR
- Th target currencies are USD, GBP, RUB, CAD, CHF, BRL, RON, SEK, CZK, AUD, HKD, PHP, DKK, ISK, MXN, ZAR, PLN, HRK, KRW, ILS and SGD

## Steps:
### Create DB:

#### Using Heroku PostgreSQL DB

1. Create App on Heroku.

2. On app’s “Overview” page, click the “Configure Add-ons” button.

3. In the “Add-ons” section of the page, type in and select “Heroku Postgres.

4. Choose the “Hobby Dev - Free” plan, which will give you access to a free PostgreSQL database that will support up to 10,000 rows of data. Click “Provision..

5. Click the “Heroku Postgres :: Database” link.

6. Click on “Settings”, and then “View Credentials.”. This information to hock my code to the DB

### Download the data into DB:

- Call the API URL using http request to get the data in JSON form
- Convert the JSON form to python dictionary and parse the dictionary to get the data from it
- Insert the data into DB

## Run:

- First run `data_setup.py` to create the rates table in Heroku postgresSQL DB
- run `import.py` to load the data into DB
- run `data_solution.py` to run the postgres qurey
