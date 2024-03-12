
from requests import Request, Session
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
import json

def fetch_data():
    url = 'https://sandbox-api.coinmarketcap.com/v1/cryptocurrency/listings/latest'
    #url = "https://pro-api.coinmarketcap.com/v1/cryptocurrency/map"
    #url = 'https://pro-api.coinmarketcap.com/v1/global-metrics/quotes/latest'
    parameters = {
        'start':'1',
        'limit':'5000'
    }
    headers = {
        'Accepts': 'application/json',
        'X-CMC_PRO_API_KEY': '10034dc8-e61d-4c1c-8b15-08b36752a95f',
    }

    session = Session()
    session.headers.update(headers)

    try:
        response = session.get(url, params=parameters)
        json_data = json.loads(response.text)
        saved_file_path = f'dags/api_data/{json_data["status"]["timestamp"]}.json'
        json_string = json.dumps(json_data)

        with open(saved_file_path, 'w+') as file:
            file.write(json_string)
        return saved_file_path
        
    except (ConnectionError, Timeout, TooManyRedirects) as e:
        print(e)
