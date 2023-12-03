import requests
class countryData:
    def __init__(self, url):
        self.url = url
        self.data = self.fetch_data()
    def fetch_data(self):
        response = requests.get(self.url)
        if response.status_code == 200:
            return response.json()
        else:
            print(f"failed to fetch data. status code: {response.status_code}")
            return None
    def display_country_info(self):
        if self.data:
          for country in self.data:
                name = country.get('name', {}).get('common', 'N/A')
                currencies = country.get('currencies', {})
                if currencies:
                    currency_name = ', '.join(currencies.keys())
                    currency_symbol = ', '.join([value.get('symbol', 'N/A') for value in currencies.values()])
                    print(f"country: {name}, currencies: {currency_name}, currency Symbols: {currency_symbol}")
                else:
                    print(f"country: {name}, No currency information available")
    def display_dollar_countries(self):
        if self.data:
            dollar_countries = [country.get('name', {}).get('common', 'N/A') for country in self.data
                                if 'USD' in country.get('currencies', {})]
            if dollar_countries:
                print("countries with DOLLAR currency:", ', '.join(dollar_countries))
            else:
                print("no countries found with DOLLAR currency")
    def display_euro_countries(self):
        if self.data:
            euro_countries = [country.get('name', {}).get('common', 'N/A') for country in self.data
                              if 'EUR' in country.get('currencies', {})]
            if euro_countries:
                print("countries with EURO currency:", ', '.join(euro_countries))
            else:
                print("no countries found with EURO currency")
# URL
url = "https://restcountries.com/v3.1/all"
country_data = countryData(url)
# display country info
country_data.display_country_info()
# display countries with Dollar currency
country_data.display_dollar_countries()
# display countries with Euro currency
country_data.display_euro_countries()
