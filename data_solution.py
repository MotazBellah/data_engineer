from data_setup import db

def run():
    data = db.execute('''select date_rate, target, source,(value*a_price) as output_value from rates, (SELECT CAST('2019-01-10' AS DATE) AS date_date, CAST('EUR' AS CHAR(3)) AS target_currency, CAST('11.11' AS NUMERIC(14,4)) AS a_price UNION
                      SELECT CAST('2019-03-18' AS DATE) AS date_date, CAST('GBP' AS CHAR(3)) AS target_currency, CAST('12.12' AS NUMERIC(14,4)) AS a_price UNION
                      SELECT CAST('2019-08-29' AS DATE) AS date_date, CAST('RUB' AS CHAR(3)) AS target_currency, CAST('333.33' AS NUMERIC(14,4)) AS a_price) as test
                      where date_rate=date_date and target=target_currency and source='USD' ;''').fetchall()
    return data

if __name__ == '__main__':
    print(run())
