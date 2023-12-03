import requests
class breweryData:
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
    def list_breweries_by_states(self, states):
        if self.data:
            for state in states:
                state_breweries = [brewery['name'] for brewery in self.data if state.lower() in brewery.get('state', '').lower()]
                print(f"Breweries in {state}: {', '.join(state_breweries)}")
    def count_breweries_by_states(self, states):
        if self.data:
            for state in states:
                state_breweries = [brewery for brewery in self.data if state.lower() in brewery.get('state', '').lower()]
                print(f"number of breweries in {state}: {len(state_breweries)}")
    def count_types_by_city(self, state):
        if self.data:
            cities = set(brewery.get('city', '') for brewery in self.data if state.lower() in brewery.get('state', '').lower())
            for city in cities:
                city_breweries = [brewery for brewery in self.data if state.lower() in brewery.get('state', '').lower() and brewery.get('city', '') == city]
                types_count = len(set(brewery.get('brewery_type', '') for brewery in city_breweries))
                print(f"City: {city}, Types Count: {types_count}")
    def count_and_list_websites_by_states(self, states):
        if self.data:
            for state in states:
                state_breweries_with_website = [brewery for brewery in self.data if state.lower() in brewery.get('state', '').lower() and brewery.get('website_url')]
                print(f"number of breweries with websites in {state}: {len(state_breweries_with_website)}")
                if state_breweries_with_website:
                    websites = [brewery['website_url'] for brewery in state_breweries_with_website]
                    print(f"Websites: {', '.join(websites)}")
# URL
url = "https://api.openbrewerydb.org/breweries"
brewery_data = breweryData(url)
# breweries in states of Alaska, Maine, and New York
brewery_data.list_breweries_by_states(['Alaska', 'Maine', 'New York'])
# breweries in each state
brewery_data.count_breweries_by_states(['Alaska', 'Maine', 'New York'])
# types of breweries in individual cities of states 
brewery_data.count_types_by_city('Alaska')
brewery_data.count_types_by_city('Maine')
brewery_data.count_types_by_city('New York')
# list breweries with websites in states of Alaska, Maine, and New York
brewery_data.count_and_list_websites_by_states(['Alaska', 'Maine', 'New York'])
