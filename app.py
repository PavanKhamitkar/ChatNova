from flask import Flask, render_template, request, jsonify
import google.generativeai as genai
import re

# Initialize Flask app
app = Flask(__name__)

# Set up the API key and configure the Gemini Pro model
GOOGLE_API_KEY = "AIzaSyCijKCTJnI6DJwzeZ-Dc085E1gbMN4A6J8"  # Replace with your actual API key
genai.configure(api_key=GOOGLE_API_KEY)
model = genai.GenerativeModel("gemini-1.5-pro")
chat = model.start_chat(history=[])

# Function to check if the question is asking about the bot's name
def is_name_question(question):
    name_patterns = [
        r'what(?:\s+is)?(?:\s+your)?(?:\s+name)',
        r'who(?:\s+are)?(?:\s+you)',
        r'your(?:\s+name)',
        r'(?:may\s+)?i(?:\s+)know(?:\s+your)?(?:\s+name)',
    ]
    return any(re.search(pattern, question.lower()) for pattern in name_patterns)

# Function to get response from Gemini Pro model
def get_gemini_response(question):
    if is_name_question(question):
        return "My name is ChatNova."
    response_chunks = chat.send_message(question, stream=True)
    return "".join(chunk.text for chunk in response_chunks)

# Main route for the chat interface
@app.route('/')
def home():
    return render_template("check.html")

# Route to handle user message and get the bot's response
@app.route('/send_message', methods=['POST'])
def send_message():
    data = request.get_json()
    user_question = data.get("question", "")
    response_text = get_gemini_response(user_question)
    return jsonify({"response": response_text})

if __name__ == "__main__":
    app.run(debug=True)
