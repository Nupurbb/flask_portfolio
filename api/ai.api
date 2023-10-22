import openai
from flask import Flask, request, jsonify

app = Flask(__name)

# Your OpenAI API key
api_key = 'YOUR_OPENAI_API_KEY'

# Set your GPT-3 API key
openai.api_key = api_key

@app.route('/generate_text', methods=['POST'])
def generate_text():
    data = request.get_json()
    if 'prompt' in data:
        prompt = data['prompt']
        response = openai.Completion.create(
            engine="davinci",  # You can choose the engine that best suits your needs.
            prompt=prompt,
            max_tokens=50,    # Adjust the response length as needed.
            n = 1             # Number of responses to generate.
        )
        return jsonify({'response': response.choices[0].text})
    else:
        return jsonify({'error': 'Missing prompt'}, 400)

if __name__ == '__main__':
    app.run(debug=True)
