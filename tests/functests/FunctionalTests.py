import requests
import yaml
import json


def post_req(payload, host, port, path):
    """Return the result of POST request."""
    result = requests.post("http://" + host + ":" + port + path, data=payload)
    return result


def get_req(host, port, path):
    """Return the result of GET request."""
    result = requests.get("http://" + host + ":" + port + path)
    return result


def check_res(result, expected, is_json=True):
    """Takes a Request result and compare it to expected
    
    Parameters:
    -----------
    result -- The result of a previous Request from post_req() or get_req()
    expected -- The String retrieved from the file requests.yaml containing expected result
    is_json -- Boolean that indicates if the result and expected should be JSON (default True)
    
    Returns:
    --------
    None - The script exits if a fail occurs
    """
    
    if result.status_code != expected["Status_Code"]:
        print("Status Code check failed.\n")
        print("Request Status Code: " + str(result.status_code) + ". Expected: " + str(expected["Status_Code"]) + "\n")
        exit(2)
    else:
        print("Status Code check succeeded.\n")
        print("Request Status Code: " + str(result.status_code) + ". Expected: " + str(expected["Status_Code"]) + "\n")

    if is_json:
        response = json.loads(result.text)
        expected_res = json.loads(expected["Response"])
    else:
        response = result.text.rstrip()
        expected_res = expected["Response"]
    
    if response != expected_res:
        print("Response check failed.\n")
        print("Request response: \n" + str(response) + "\nExpected: \n" + str(expected_res) + "\n")
        exit(2)
    else:
        print("Response check succeeded.\n")
        print("Request response: \n" + str(response) + "\nExpected: \n" + str(expected_res) + "\n")


SERVICE_HOST = "localhost"
SERVICE_PORT = "8082"

with open("requests.yaml") as f:
    request_list = yaml.safe_load(f)

for request in request_list:
    if request["Type"] == "POST":
        req_result = post_req(request["Data"], SERVICE_HOST, SERVICE_PORT, request["Route"])
        check_res(req_result, request["Expected"]["Success"])
        
        # Tampering data to check failed request
        failed_req_result = post_req(request["Data"][:-3], SERVICE_HOST, SERVICE_PORT, request["Route"])
        check_res(failed_req_result, request["Expected"]["Failure"])
    else:
        req_result = get_req(SERVICE_HOST, SERVICE_PORT, request["Route"])
        check_res(req_result, request["Expected"]["Success"])
        
        # Tampering route to check failed request
        failed_req_result = get_req(SERVICE_HOST, SERVICE_PORT, request["Route"][:-1])
        check_res(failed_req_result, request["Expected"]["Failure"], False)
