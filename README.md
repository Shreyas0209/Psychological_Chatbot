# Psychological_Chatbot

Mano - The AI Psychological Therapist
Mano is a web-based, AI-powered chatbot designed to provide a safe, empathetic, and non-judgmental space for users to explore their thoughts and feelings. It leverages the power of a large language model (Google Gemini) to engage in caring and supportive conversations, guided by principles of Cognitive Behavioral Therapy (CBT).

✨ Features
Empathetic & Caring Persona: The chatbot is instructed by a detailed system prompt to always be supportive, kind, and understanding.

AI-Powered Conversations: Utilizes the Google Gemini API for intelligent, nuanced, and human-like conversational abilities.

Calming User Interface: A warm, clean, and inviting UI designed with a light orange color palette to create a sense of comfort and trust.

Therapeutic Guidance: Can offer well-known, safe coping techniques (like guided breathing) and gently guide users to reframe their thoughts.

Built-in Ethical Guardrails: Includes a clear disclaimer that it is not a substitute for professional therapy and provides a crisis warning.

Web-Based & Accessible: Built with Flask, making it easily accessible from any modern web browser.

🛠️ Tech Stack
Backend: Python, Flask

Frontend: HTML, CSS, JavaScript

AI / NLP: Google Gemini API

Python Libraries:

Flask

google-generativeai

🚀 Setup and Installation
Follow these steps to get the application running on your local machine.

1. Prerequisites
Python 3.7 or newer installed on your system.

pip (Python's package installer).

2. Get the Code
Clone this repository or download the project files into a local directory.

bash
git clone <your-repository-url>
cd psychology_chatbot_webapp
3. Create a Virtual Environment
It's highly recommended to use a virtual environment to manage project dependencies.

bash
# For macOS/Linux
python3 -m venv venv
source venv/bin/activate

# For Windows
python -m venv venv
.\venv\Scripts\activate
4. Install Dependencies
Create a file named requirements.txt in your project's root directory and add the following lines to it:

text
Flask
google-generativeai
Now, install the required packages using pip:

bash
pip install -r requirements.txt
⚙️ Configuration
The most important step is to add your API key.

Open the app.py file.

Find the following line:

python
API_KEY = "YOUR_GEMINI_API_KEY_HERE"
Replace "YOUR_GEMINI_API_KEY_HERE" with your actual API key from Google AI Studio. The application will not start without a valid key.

▶️ How to Run the Application
Make sure your virtual environment is activated.

Run the Flask application from your terminal:

bash
python app.py
The terminal will show that the server is running. Open your web browser and navigate to:

text
http://127.0.0.1:5000
You should now see the Mano chatbot interface, ready to start a conversation.

⚠️ Important Disclaimer
This application is an AI experiment and is not a substitute for professional therapy or medical advice. It is designed for reflection and emotional exploration only. If you are in crisis or believe you may have a mental health condition, please seek immediate help from a qualified human professional or a crisis hotline.
