from data_setup import db

def run(target_data, source=''):
    '''Function to get multiple target currency and
    convert them to USD value or EUR value
    Input: target_data(string), represent a SQL query
    that conatains multiple source (target) prices,
    and source(string), represent which base currencies (USD, EUR) you want to Convert
    the default value is empty i.e convert to both USD and test_run_EUR
    Output: String value that conatins the conveted currencies'''

    output = ''
    # If source empty(default) or the user enter a wrong value,
    # Then set the source to be equal to USD and EUR
    # otherwise save the source in tuple, to be easy reachable in SQL query
    if source not in ['USD', 'EUR']:
        source = 'USD', 'EUR'
    else:
        source = (source,'')

    if target_data:
        data = db.execute('''select date_rate, a_price, target,CAST(((1/value)*a_price) AS NUMERIC(16,5))as output_value, source from rates,
                          ({}) as target_data
                          where date_rate=date_date and target=target_currency and source in {};'''.format(target_data, source)).fetchall()
    # If data has some output, loop through it
    # and append it to the sting value to return it
    if data:
        for i in data:
            output += "At the date of {}, the {} {} equal to {} {} \n".format(*i)
    else:
        output += "Please check the date or the target currency!"

    # Delete the not need spaces, i.e the last line using strip function
    return output.strip()

if __name__ == '__main__':
    print(run('''SELECT CAST('2019-01-10' AS DATE) AS date_date, CAST('EUR' AS CHAR(3)) AS target_currency,
              CAST('11.11' AS NUMERIC(14,4)) AS a_price UNION SELECT CAST('2019-03-18' AS DATE) AS date_date,
              CAST('GBP' AS CHAR(3)) AS target_currency, CAST('12.12' AS NUMERIC(14,4)) AS a_price UNION
              SELECT CAST('2019-08-29' AS DATE) AS date_date, CAST('RUB' AS CHAR(3)) AS target_currency,
              CAST('333.33' AS NUMERIC(14,4)) AS a_price'''))

    # print(run('''SELECT CAST('2022-08-09' AS DATE) AS date_date, CAST('CAD' AS CHAR(3)) AS target_currency,
    #         CAST('675.34' AS NUMERIC(14,4)) AS a_price UNION SELECT CAST('2000-03-13' AS DATE) AS date_date,
    #         CAST('GBP' AS CHAR(3)) AS target_currency, CAST('52' AS NUMERIC(14,4)) AS a_price UNION
    #         SELECT CAST('1800-06-11' AS DATE) AS date_date, CAST('RUB' AS CHAR(3)) AS target_currency,
    #         CAST('3.5' AS NUMERIC(14,4)) AS a_price'''))
