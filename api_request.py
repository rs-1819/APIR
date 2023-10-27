import os, requests

def make_request(endpoint, method='GET', data=None, params=None, filters=None, paging=None):
    # Get the API key from the environment variable
    API_KEY = os.getenv('API_KEY')

    headers = {
        'X-API-Key': API_KEY,
        'Accept': 'application/json'
    }

    if filters:
        headers['X-Filter'] = filters

    if paging:
        headers['X-Paging'] = paging


    url = endpoint

    if method == 'GET':
        response = requests.get(url, headers=headers, params=params)
    elif method == 'POST':
        print(data)        
        response = requests.post(url, headers=headers, json=data)
    elif method == 'DELETE':
        response = requests.delete(url, headers=headers, params=params)
    elif method in ['PUT', 'PATCH']:
        response = requests.request(method, url, headers=headers, json=data)
    else:
        raise ValueError('Invalid method')

    if response.status_code in [200, 201]:  # Success responses
        return response.json()
    elif response.status_code == 400:  # Bad Request
        return 'The request is malformed', response.json()
    elif response.status_code == 403:  # Unauthorized
        raise PermissionError('Resource exists but you do not have access', response.json())
    elif response.status_code == 404:  # Not Found
        raise FileNotFoundError('Resource does not exist', response.json())
    elif response.status_code == 204:  # No record found to delete
        return None
    else:
        response.raise_for_status()  # Raise an exception for any other error codes

def api_request(endpoint, method='GET', **kwargs):
    # Convert array parameters to multiple query parameters
    for key, value in kwargs.items():
        if isinstance(value, list):
            kwargs[key] = ','.join(map(str, value))

    filters = kwargs.pop('filters', None)
    paging = kwargs.pop('paging', None)
    data = kwargs.pop('data', None)

    if method.upper() in ['GET', 'DELETE']:
        response = make_request(endpoint, method=method, params=kwargs, filters=filters, paging=paging)
    elif method.upper() in ['POST', 'PUT', 'PATCH']:
        response = make_request(endpoint, method=method, data=data, filters=filters, paging=paging)
    else:
        raise ValueError('Invalid method', method)

    return response  # Return the response