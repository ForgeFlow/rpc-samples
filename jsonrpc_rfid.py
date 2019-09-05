import json
import requests


card_code = input("Enter Card Code:")
# Credential Variables required
server_url = 'http://localhost:8069' # Odoo instance IP
db_name = '12.0-odoo-training-tai-2'
username = 'admin'
password = 'admin'
# Json specific configuration
json_endpoint = "%s/jsonrpc" % server_url
headers = {"Content-Type": "application/json"}


def get_json_payload(service, method, *args):
    return json.dumps({
            "jsonrpc": "2.0",
            "method": 'call',
            "params": {
            "service": service,
            "method": method,
            "args": args,
            },
    })


# Get user_id
payload = get_json_payload("common", "login", db_name, username, password)
response = requests.post(json_endpoint, data=payload, headers=headers)
user_id = response.json()['result']
if user_id:
    # Register Attendance
    payload = get_json_payload("object", "execute_kw", db_name, username, password,
                                        'hr.employee', 'register_attendance',
                                        [card_code])
    response = requests.post(json_endpoint, data=payload, headers=headers)
    call_attendance = response.json()
    print(call_attendance)
