from flask import Flask, request, jsonify

app = Flask(_chem_name)

# Store flashcards in-memory (not recommended for production)
flashcards = []

@app.route('/flashcards', methods=['POST'])
def create_flashcard():
    data = request.get_json()
    if 'question' in data and 'answer' in data:
        flashcard = {
            'question': data['question'],
            'answer': data['answer']
        }
        flashcards.append(flashcard)
        return jsonify({'message': 'Flashcard created successfully'})
    else:
        return jsonify({'error': 'Missing question or answer'}, 400)

@app.route('/flashcards', methods=['GET'])
def get_flashcards():
    return jsonify({'flashcards': flashcards})

if __name__ == '__main__':
    app.run(debug=True)
from flask import Flask, request, jsonify

app = Flask(_flash_name)

# Store chemistry flashcards in-memory (not recommended for production)
flashcards = []

@app.route('/flashcards', methods=['POST'])
def create_flashcard():
    data = request.get_json()
    if 'topic' in data and 'question' in data and 'answer' in data:
        flashcard = {
            'topic': data['topic'],
            'question': data['question'],
            'answer': data['answer']
        }
        flashcards.append(flashcard)
        return jsonify({'message': 'Chemistry flashcard created successfully'})
    else:
        return jsonify({'error': 'Missing topic, question, or answer'}, 400)

@app.route('/flashcards', methods=['GET'])
def get_flashcards():
    return jsonify({'flashcards': flashcards})

if __name__ == '__main__':
    app.run(debug=True)
