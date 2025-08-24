import requests
import configparser 
import requests # type: ignore
from app.reg_event import registration

from bot_logging.utils import log_revest_event, log_error  # ← ИЗМЕНИЛ

async def revest_operation(user_id: int, username: str, action: str):
    try:
        log_revest_event(user_id, username, "operation", f"action: {action}")
        # ваш код
        return True
    except Exception as e:
        log_error("RevestError", str(e), user_id)
        return False


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