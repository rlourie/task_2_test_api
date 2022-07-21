import requests
from datetime import date
import pytest


class Test:

    def latest(self, symbols, symbols1, base):
        url = f"https://api.apilayer.com/fixer/latest?symbols={symbols}%2C{symbols1}&base={base}"

        headers = {
            "apikey": "2K2YEf6Ejl0jldg2OQgvkub41S3xxZxw"
        }

        response = requests.request("GET", url, headers=headers)
        status = response.status_code
        result = response.json()
        return result, status

    def date(self, symbols, symbols1, base):
        url = f"https://api.apilayer.com/fixer/2001-01-03?symbols={symbols}%2C{symbols1}&base={base}"
        headers = {
            "apikey": "2K2YEf6Ejl0jldg2OQgvkub41S3xxZxw"
        }
        response = requests.request("GET", url, headers=headers)
        status = response.status_code
        result = response.json()
        return result, status

    # Проверка статус кода
    def test_case_1(self):
        result, status = self.latest('EUR', 'RUB', 'USD')
        assert status == 200

    # Проверка структуры положительного ответа
    def test_case_2(self):
        result, status = self.latest('EUR', 'RUB', 'USD')
        assert (
                       "base" in result and 'date' in result and 'rates' in result and 'success' in result and 'timestamp' in result) \
               and ('EUR' in result.get('rates') and 'RUB' in result.get('rates'))

    # Проверка соответсвия даты
    def test_case_3(self):
        result, status = self.latest('EUR', 'RUB', 'USD')
        assert result.get('date') == str(date.today())

    # Проверка что во временно точке только цифры
    def test_case_4(self):
        result, status = self.latest('EUR', 'RUB', 'USD')
        assert str(result.get('timestamp')).isdigit()

    # Проверка что база такая же
    def test_case_5(self):
        result, status = self.latest('EUR', 'RUB', 'USD')
        assert result.get('base') == 'USD'

    # Проверка что c маленькими буквами тоже работает
    def test_case_6(self):
        result, status = self.latest('eur', 'rub', 'usd')
        assert status == 200

    # Проверка что c маленькими буквами такаяже структура
    def test_case_7(self):
        result, status = self.latest('eur', 'rub', 'usd')
        assert (
                       "base" in result and 'date' in result and 'rates' in result and 'success' in result and 'timestamp' in result) \
               and ('EUR' in result.get('rates') and 'RUB' in result.get('rates'))

    ################################################################

    # Проверка что код 200
    def test_case_8(self):
        result, status = self.date('EUR', 'RUB', 'USD')
        assert status == 200

    # Проверка что структура правильная
    def test_case_9(self):
        result, status = self.date('EUR', 'RUB', 'USD')
        assert (
                       "base" in result and 'date' in result and 'historical' in result and 'rates' in result and 'success' in result and 'timestamp' in result) \
               and ('EUR' in result.get('rates') and 'RUB' in result.get('rates'))

    # Проверка что дата правильная
    def test_case_10(self):
        result, status = self.date('EUR', 'RUB', 'USD')
        assert result.get('date') == '2001-01-03'

    # Проверка что во временной точке только цифры
    def test_case_11(self):
        result, status = self.date('EUR', 'RUB', 'USD')
        assert str(result.get('timestamp')).isdigit()

    # Проверка что база такая же
    def test_case_12(self):
        result, status = self.date('EUR', 'RUB', 'USD')
        assert result.get('base') == 'USD'

    # Проверка что c маленькими буквами тоже работает
    def test_case_13(self):
        result, status = self.date('eur', 'rub', 'usd')
        assert status == 200

    # Проверка что c маленькими буквами такаяже структура
    def test_case_14(self):
        result, status = self.date('eur', 'rub', 'usd')
        assert (
                       "base" in result and 'date' in result and 'historical' in result and 'rates' in result and 'success' in result and 'timestamp' in result) \
               and ('EUR' in result.get('rates') and 'RUB' in result.get('rates'))
