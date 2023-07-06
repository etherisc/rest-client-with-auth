# REST Client with Auth

## Environment

To run this python test client the following environment is assumed

* Python (version 3.9 or higher)
* Python requests library
* A `.env` file

## The .env File

Copy the file `dotenv` into `.env` and fill in the parameter values for client ID and client secret.

## Sample Session

Below a sample python session is provided

```python
>>>
from client import fetch_auth_token, post_policy
from client import fetch_auth_token, post_policy

token_response = fetch_auth_token()
token = token_response['access_token']

policy = {
  'name': 'babettli',
  'phone': '079 987 6543',
  'premium': 101,
  'suminsured': 1200
}

response = post_policy(token, policy)

print('policy: {}'.format(policy))
print('response: {} {} {}'.format(response.status_code, response.reason, response.json()))
```
