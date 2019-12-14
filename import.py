import httplib2
import json
from data_setup import db
import psycopg2


def getExchangeData():
    '''Get the data from exchangeratesapi API and load it to DB'''

    urls = (
    '''https://api.exchangeratesapi.io/history?start_at=2019-01-01&end_at=2019-12-01&base=USD&symbols=EUR,GBP,RUB,CAD,CHF,BRL,RON,SEK,CZK,AUD,HKD,PHP,DKK,ISK,MXN,ZAR,PLN,HRK,KRW,ILS,SGD''',
    '''https://api.exchangeratesapi.io/history?start_at=2019-01-01&end_at=2019-12-01&base=EUR&symbols=USD,GBP,RUB,CAD,CHF,BRL,RON,SEK,CZK,AUD,HKD,PHP,DKK,ISK,MXN,ZAR,PLN,HRK,KRW,ILS,SGD'''
    )

    h = httplib2.Http()
    for url in urls:
        dict_data = json.loads(h.request(url, 'GET')[1])
        data = ((rates[0], dict_data['base'], target, rates[1][target]) for rates in dict_data['rates'].items() for target in rates[1].keys())
        for i in data:
            # print(i)
            date_rate, source, target, value = i
            db.execute('''INSERT INTO rates (date_rate, source, target, value) VALUES (:date_rate, :source, :target, :value)''',
                       {"date_rate": date_rate, "source": source, "target": target, "value": value})
            print("Loading...")
        db.commit()

    print("Done")


if __name__ == '__main__':
    getExchangeData()
