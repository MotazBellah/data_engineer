import unittest
from data_setup import db
from data_solution import run

class TestRun(unittest.TestCase):

    def test_run_USD(self):
        input = '''SELECT CAST('2019-08-09' AS DATE) AS date_date, CAST('CAD' AS CHAR(3)) AS target_currency,
                CAST('675.34' AS NUMERIC(14,4)) AS a_price UNION SELECT CAST('2019-03-13' AS DATE) AS date_date,
                CAST('GBP' AS CHAR(3)) AS target_currency, CAST('52' AS NUMERIC(14,4)) AS a_price UNION
                SELECT CAST('2019-06-11' AS DATE) AS date_date, CAST('RUB' AS CHAR(3)) AS target_currency,
                CAST('3.5' AS NUMERIC(14,4)) AS a_price'''
        response = run(input, 'USD')
        # print(response)
        excepected_output = '''At the date of 2019-06-11, the 3.5000 RUB equal to 0.05426 USD \nAt the date of 2019-03-13, the 52.0000 GBP equal to 68.43922 USD \nAt the date of 2019-08-09, the 675.3400 CAD equal to 511.11499 USD'''
        self.assertEqual(response, excepected_output)

    def test_run_EUR(self):
        input = '''SELECT CAST('2019-08-09' AS DATE) AS date_date, CAST('CAD' AS CHAR(3)) AS target_currency,
                CAST('675.34' AS NUMERIC(14,4)) AS a_price UNION SELECT CAST('2019-03-13' AS DATE) AS date_date,
                CAST('GBP' AS CHAR(3)) AS target_currency, CAST('52' AS NUMERIC(14,4)) AS a_price UNION
                SELECT CAST('2019-06-11' AS DATE) AS date_date, CAST('RUB' AS CHAR(3)) AS target_currency,
                CAST('3.5' AS NUMERIC(14,4)) AS a_price'''
        response = run(input, 'EUR')
        # print(response)
        excepected_output = '''At the date of 2019-06-11, the 3.5000 RUB equal to 0.04793 EUR \nAt the date of 2019-03-13, the 52.0000 GBP equal to 60.54960 EUR \nAt the date of 2019-08-09, the 675.3400 CAD equal to 456.43417 EUR'''
        self.assertEqual(response, excepected_output)

    def test_run_DATE(self):
        input = '''SELECT CAST('2022-08-09' AS DATE) AS date_date, CAST('CAD' AS CHAR(3)) AS target_currency,
                CAST('675.34' AS NUMERIC(14,4)) AS a_price UNION SELECT CAST('2000-03-13' AS DATE) AS date_date,
                CAST('GBP' AS CHAR(3)) AS target_currency, CAST('52' AS NUMERIC(14,4)) AS a_price UNION
                SELECT CAST('1800-06-11' AS DATE) AS date_date, CAST('RUB' AS CHAR(3)) AS target_currency,
                CAST('3.5' AS NUMERIC(14,4)) AS a_price'''
        response = run(input)
        # print(response)
        excepected_output = '''Please check the date or the target currency!'''
        self.assertEqual(response, excepected_output)


if __name__ == '__main__':
    unittest.main()
