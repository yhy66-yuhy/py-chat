import requests
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def chat():
    if request.method == 'POST':
        message = request.form['message']
        response = get_chat_response(message)
        return render_template('index.html', message=message, response=response)
    return render_template('index.html')

def get_chat_response(message):
    url = "https://openkey.cloud/v1/chat/completions"
    headers = {
        'Content-Type': 'application/json',
        'Authorization': 'Bearer sk-eVdeKLXCkRNdZzH0468aAe59C26e4082Aa968b0eEa17Ef7e'
    }
    data = {
        "model": "gpt-3.5-turbo",
        "messages": [{"role": "user", "content": message}]
    }
    response = requests.post(url, headers=headers, json=data)
    return response.json()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True, threaded=True)
