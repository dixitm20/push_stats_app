import json
import requests

from push_stats.entities import APILoadResponse


def load_to_api(msg):
    endpoint = "https://flaky.dev.insify.io/v1/ingress"
    payload = json.dumps(msg)
    headers = {
        'Content-Type': 'application/json',
        'Authorization': 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMjM0NTY3ODkwIiwibmFtZSI6IkhhY2tlciBib3kiLCJpYXQiOjE1MTYyMzkwMjJ9.tXSV6E8zEzi3socXwbikGo9eg-yLmpGz1_xsmgwE5jw'
    }
    for retry in range(3):
        response = requests.request("POST", endpoint, headers=headers, data=payload)
        if response.status_code == 200:
            break

    return APILoadResponse(payload=payload, status_code=response.status_code, response_content=response.content)
