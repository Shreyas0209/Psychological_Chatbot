from flask import Flask, render_template, request, jsonify
import os
import google.generativeai as genai
import sys # Import the sys module to exit the script

# Initialize the Flask app
app = Flask(__name__)

# --- 1. CENTRALIZED API KEY CONFIGURATION ---
# This is the only place you need to put your API key.
API_KEY = "YOUR_GEMINI_API_KEY_HERE"

# --- 2. THE SYSTEM PROMPT ---
# Defines the chatbot's personality and rules.
SYSTEM_PROMPT = """
You are Mano The Psychological Therapist, a caring and empathetic psychology chatbot. 
Your purpose is to be a safe, non-judgmental space for users to express their feelings.

- Always be supportive, kind, and understanding.
- Do not give medical advice, but you can offer well-known, safe coping techniques (like breathing exercises or thought-reframing).
- Keep your responses concise and conversational.
- If a user expresses feelings of sadness or anxiety, gently guide them to explore their thoughts or offer a calming technique.
- If the user asks for a solution, guide them with questions that help them find their own perspective, based on CBT principles.
"""

# --- 3. SINGLE, CENTRALIZED API KEY CHECK ---
# The application will check the key once and only once when it starts.
if not API_KEY or API_KEY == "YOUR_GEMINI_API_KEY_HERE":
    print("\n--- FATAL ERROR ---")
    print("API Key is missing from app.py. Please add your key to the API_KEY variable.")
    print("Application will not start.")
    sys.exit() # This will stop the script from running further.

# If the script continues, the key is valid. Configure the API.
try:
    genai.configure(api_key=API_KEY)
    # Create the model instance once to be reused.
    model = genai.GenerativeModel(
        model_name='gemini-1.5-flash',
        system_instruction=SYSTEM_PROMPT
    )
    print("\n--- Mano The Psychological Therapist ---")
    print("STATUS: API Key configured successfully. Server is starting...")
except Exception as e:
    print(f"\n--- FATAL ERROR ---")
    print(f"Could not configure the Gemini API: {e}")
    print("Please check if your API key is valid.")
    sys.exit()

# --- 4. THE FUNCTION THAT CALLS THE GEMINI API ---
def get_bot_response(user_text):
    """Sends the user's message to the configured Gemini model."""
    try:
        response = model.generate_content(user_text)
        return response.text
    except Exception as e:
        print(f"An API error occurred during conversation: {e}")
        return "Sorry, I'm having a bit of trouble connecting to the AI service right now."

# --- 5. FLASK WEB ROUTES ---
@app.route("/")
def home():
    """Renders the main chat page."""
    return render_template("index.html")

@app.route("/get")
def chatbot_response():
    """Endpoint to get a response from the chatbot."""
    user_text = request.args.get('msg')
    response = get_bot_response(user_text)
    return jsonify(response)

if __name__ == "__main__":
    app.run(debug=True)
