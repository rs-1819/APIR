# Python API Request Wrapper

This Python module provides a flexible and easy-to-use function for making HTTP requests to APIs. The `api_request` function supports GET, POST, PUT, PATCH, and DELETE HTTP methods, and allows you to send parameters, data, and custom headers with your requests.

## Features

- Supports GET, POST, PUT, PATCH, and DELETE HTTP methods
- Easy integration with environment variables for API keys
- Custom headers for filtering and pagination
- Error handling for common HTTP status codes

## Installation

Before you can use this script, you need to install the required packages. You can install the required packages using pip:

```bash
pip install requests
```

## Usage

First, you need to set your API key as an environment variable. You can do this by running the following command in your terminal:

```bash
export API_KEY=your_api_key_here
```

### Importing the Module

You can import the `api_request` function from the script like this:

```python
from your_script_name import api_request
```

### Making a GET Request

Here's an example of how you can make a GET request:

```python
response = api_request('https://api.example.com/data', params={'param1': 'value1', 'param2': 'value2'})
print(response)
```

### Making a POST Request

And here's an example of how you can make a POST request:

```python
data = {'key1': 'value1', 'key2': 'value2'}
response = api_request('https://api.example.com/data', method='POST', data=data)
print(response)
```

### Using Filters and Paging

You can also add filters and paging to your requests:

```python
response = api_request('https://api.example.com/data', filters='your_filter', paging='your_paging_info')
print(response)
```

### Handling Errors

The script includes error handling for common HTTP status codes. For example, if you make a request to a non-existent resource, a `FileNotFoundError` will be raised.

## License

This project is licensed under the MIT License