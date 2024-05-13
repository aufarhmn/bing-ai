# Bing AI API

This is a simple Flask API to mock Bing AI interface. It's main purpose is to return a JSON response with the same structure as Bing AI interface. The API is limited to handle request by authenticated users only. Therefore, the user must provide a valid cookies in the bing_cookies.json

## Installation
- Clone the repository
- Install the requirements
```
pip install flask asyncio re_edge_gpt
```
- Run the app
```
flask run
```

## Usage
Send a POST request to /ask with the following body:
```
{
    "prompt": "Enter your prompt here"
}
```