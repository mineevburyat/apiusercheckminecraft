import requests
from app.reg_event import registration


import configparser 
config = configparser.ConfigParser()
config.read('config.ini')

API_REG = config['API']['API_REG'].strip()

def register_nick(data: dict):
    try:
        nick_name = data.get("nick_name")

        url = f'{API_REG}/{nick_name}'

        
        response = requests.get(url)
        response.raise_for_status()

        response_data = response.json()
        if isinstance(response_data, dict) and response_data.get('result') is True:
            return response.status_code, {"status": "success", "message": "Nickname registered"}
        else:
            return response.status_code, {"error": "Unexpected server response", "data": response_data}

    except requests.HTTPError as http_err:
        return response.status_code, {"error": f"HTTP error: {http_err}"}
    except requests.RequestException as err:
        return 0, {"error": f"Connection error: {str(err)}"}
    except ValueError as e:
        return 500, {"error": f"Invalid server response: {str(e)}"}
