from flask import Flask, render_template, request, jsonify
import google.generativeai as genai

# Initialize Flask app
app = Flask(__name__)

# Set up the API key and configure the Gemini Pro model
GOOGLE_API_KEY = ""  # Replace with your actual API key
genai.configure(api_key=GOOGLE_API_KEY)
model = genai.GenerativeModel("gemini-pro")
chat = model.start_chat(history=[])

# Function to get response from Gemini Pro model
def get_gemini_response(question):
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
