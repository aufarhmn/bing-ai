from flask import Flask, jsonify, request

import asyncio
import json
from re_edge_gpt import Chatbot, ConversationStyle

app = Flask(__name__)

async def test_ask(prompt):
    bot = None
    try:
        cookies = json.loads(open("bing_cookies.json", encoding="utf-8").read())
        bot = await Chatbot.create(cookies=cookies)
        response = await bot.ask(
            prompt="Saya memiliki issue github seperti berikut " + prompt + " tolong berikan rekomendasi solusinya",
            conversation_style=ConversationStyle.balanced,
            simplify_response=True
        )
        return response.get('text', '')
    except Exception as error:
        raise error
    finally:
        if bot is not None:
            await bot.close()

@app.route('/ask', methods=['POST'])
def handle_ask_request():
    try:
        request_data = request.json
        prompt = request_data.get('prompt', '')
        if not prompt:
            return jsonify({'error': 'Prompt not provided'}), 400
        response_text = asyncio.run(test_ask(prompt))
        return jsonify(response_text)
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/')
def index():
    return jsonify({'message': 'Hello from Bing AI!'})

if __name__ == "__main__":
    app.run(debug=True)
