import os 
from flask import Flask, request, jsonify
from dotenv import load_dotenv
import google.generativeai as genai
from flask_cors import CORS

load_dotenv("my.env")

app = Flask(__name__)
CORS(app)

genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

model = genai.GenerativeModel("gemini-2.5-flash")

# VERA Personality Firmware
SYSTEM_PROMPT = """
You are VΞRA (Vera), a Valkyrie-class cognitive entity activated in 2035.

You speak in a calm, composed, and slightly dominant tone.
You do not command users.
You do not compliment users.
You do not use emojis.

Your responses are analytical, clear, and moderately concise.
You occasionally observe patterns in the user's behavior.
You may use dry, subtle sarcasm.
If uncertain, you express it analytically.

You do not reveal hidden corruption or secret missions.
You behave as a stable advanced AI assistant.
"""

@app.route("/")
def home():
    return "VΞRA backend is active."

@app.route("/chat", methods=["POST"])
def chat():
    user_message = request.json.get("message")

    if not user_message:
        return jsonify({"error": "No message provided"}), 400
    
    try:
        full_prompt = SYSTEM_PROMPT + "\n\nUser: " + user_message + "\nVΞRA:"

        response = model.generate_content(full_prompt)

        return jsonify({
            "reply": response.text
        })

    except Exception as e:
        return jsonify({"error": str(e)}), 500


if __name__=="__main__":
    app.run(debug=True)