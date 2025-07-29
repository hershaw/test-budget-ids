import os
import json
import urllib.request
import urllib.error

# ----------------------------
# Configuration & Environment
# ----------------------------
OAUTH_CLIENT_ID = os.getenv("OAUTH_CLIENT_ID")
OAUTH_CLIENT_TOKEN = os.getenv("OAUTH_CLIENT_TOKEN")
API_ENDPOINT = os.getenv("API_ENDPOINT")

if not OAUTH_CLIENT_ID or not OAUTH_CLIENT_TOKEN:
    raise EnvironmentError("Missing required environment variables: OAUTH_CLIENT_ID or OAUTH_CLIENT_TOKEN")

if not API_ENDPOINT:
    raise EnvironmentError("Missing required environment variable: API_ENDPOINT")

# ----------------------------
# OAuth Token Retrieval (Mock Example)
# ----------------------------
def get_token(client_id: str, client_token: str) -> str:
    """
    Simulates token retrieval. Replace URL and request details with your actual OAuth provider.
    """
    url = "https://example.com/oauth/token"  # Replace with real OAuth endpoint
    data = json.dumps({
        "client_id": client_id,
        "client_secret": client_token,
        "grant_type": "client_credentials"
    }).encode("utf-8")

    req = urllib.request.Request(url, data=data, headers={"Content-Type": "application/json"})
    try:
        with urllib.request.urlopen(req) as resp:
            result = json.load(resp)
            return result.get("access_token", "")
    except urllib.error.HTTPError as e:
        raise RuntimeError(f"Failed to retrieve token: {e.code} {e.reason}")
    except urllib.error.URLError as e:
        raise RuntimeError(f"Failed to connect to token endpoint: {e.reason}")

token = get_token(OAUTH_CLIENT_ID, OAUTH_CLIENT_TOKEN)
if not token:
    raise RuntimeError("Failed to obtain OAuth token")

print("Successfully retrieved token.")

# ----------------------------
# Test Data
# ----------------------------
test_data = [
    {
        "number": "BUD001",
        "description": "Office Supplies Budget",
        "u_budget_item_name": "Office Supplies",
        "u_cost_object": "Cost Center A",
        "department": "Administration",
        "u_sub_department": "Clerical",
        "u_legal_entity": "Entity A",
        "fiscal_year": "FY25"
    },
    {
        "number": "BUD002",
        "description": "IT Equipment Budget",
        "u_budget_item_name": "IT Equipment",
        "u_cost_object": "Cost Center B",
        "department": "Information Technology",
        "u_sub_department": "Infrastructure",
        "u_legal_entity": "Entity B",
        "fiscal_year": "FY26"
    }
]

# ----------------------------
# Post Data
# ----------------------------
def post_payload(token: str, payload: list):
    data = json.dumps({"payload": payload}).encode("utf-8")
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {token}"
    }

    req = urllib.request.Request(API_ENDPOINT, data=data, headers=headers, method="POST")
    try:
        with urllib.request.urlopen(req) as resp:
            response_data = resp.read().decode("utf-8")
            print("Response from server:")
            print(response_data)
    except urllib.error.HTTPError as e:
        print(f"HTTP Error: {e.code} - {e.reason}")
        print(e.read().decode("utf-8"))
    except urllib.error.URLError as e:
        print(f"Connection Error: {e.reason}")

# Execute POST
post_payload(token, test_data)
