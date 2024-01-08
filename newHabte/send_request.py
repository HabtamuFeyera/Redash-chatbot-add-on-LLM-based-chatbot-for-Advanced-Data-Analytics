import requests
import json

# URL of the Flask application
url = 'http://127.0.0.1:5000/nl_to_sql'

# Natural language query
nl_query = "Show me the total revenue by product category"

# Create JSON payload
payload = {"nl_query": nl_query}

# Send POST request
response = requests.post(url, json=payload)

# Print the response
print(response.json())
