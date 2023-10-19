from flask import Flask, request, jsonify

app = Flask(__name__)

# Mock data for flashcards
flashcards = [
    {"id": 1, "question": "What is the capital of France?", "answer": "Paris"},
    {"id": 2, "question": "What is the largest planet in our solar system?", "answer": "Jupiter"},
]

# API endpoint to get all flashcards
@app.route('/flashcards', methods=['GET'])
def get_flashcards():
    return jsonify({"flashcards": flashcards})

# API endpoint to get a specific flashcard by ID
@app.route('/flashcards/<int:card_id>', methods=['GET'])
def get_flashcard(card_id):
    card = next((card for card in flashcards if card["id"] == card_id), None)
    if card is not None:
        return jsonify(card)
    return jsonify({"error": "Flashcard not found"}), 404

# API endpoint to create a new flashcard
@app.route('/flashcards', methods=['POST'])
def create_flashcard():
    data = request.get_json()
    new_id = len(flashcards) + 1
    flashcard = {"id": new_id, "question": data["question"], "answer": data["answer"]}
    flashcards.append(flashcard)
    return jsonify(flashcard), 201

# API endpoint to update a flashcard by ID
@app.route('/flashcards/<int:card_id>', methods=['PUT'])
def update_flashcard(card_id):
    card = next((card for card in flashcards if card["id"] == card_id), None)
    if card is not None:
        data = request.get_json()
        card["question"] = data["question"]
        card["answer"] = data["answer"]
        return jsonify(card)
    return jsonify({"error": "Flashcard not found"}), 404

# API endpoint to delete a flashcard by ID
@app.route('/flashcards/<int:card_id>', methods=['DELETE'])
def delete_flashcard(card_id
