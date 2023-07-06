import os
import requests

from dotenv import load_dotenv

AUDIENCE = 'https://etherisc.com/api/rest'
DOMAIN = 'dev-etherisc.eu.auth0.com'
DOMAIN_URL = 'https://{}/oauth/token'.format(DOMAIN)

SERVER_URL = 'https://rest-api.integration.etherisc.com/'

# load client id and secret from .env file
load_dotenv()
CLIENT_ID = os.getenv('CLIENT_ID')
CLIENT_SECRET = os.getenv('CLIENT_SECRET')


def fetch_auth_token() -> dict:
    payload = {
        'client_id': CLIENT_ID,
        'client_secret': CLIENT_SECRET,
        'audience': AUDIENCE,
        'grant_type': 'client_credentials'
    }

    headers = {
        'content-type': 'application/x-www-form-urlencoded'
    }

    response = requests.post(DOMAIN_URL, data=payload, headers=headers)

    if response.status_code == 200:
        return response.json()
    else:
        return {
            'error': f'Received status code {response.status_code}'
        }


def post_policy(token, policy):
    header = {
        'authorization': f'Bearer {token}',
        'content-type': 'application/json'
    }

    response = requests.post(url=SERVER_URL, json=policy, headers=header)

    return response
