import os
import google.generativeai as genai
from flask import Flask, render_template, request, jsonify
from dotenv import load_dotenv

# Load security credentials from the .env file
load_dotenv()

# Initialize the web application
app = Flask(__name__)

# --- Configure the Google Gemini API ---
try:
    # Get the API key from the environment variable
    api_key = os.getenv("GEMINI_API_KEY")
    if not api_key:
        raise ValueError("GEMINI_API_KEY not found. Please check your .env file.")
    
    # Set up the Google AI client
    genai.configure(api_key=api_key)
    
    # Create the specific AI model we'll use
    model = genai.GenerativeModel('gemini-2.0-flash')
except Exception as e:
    print(f"🔴 Error configuring Google Gemini: {e}")
    model = None

# --- Application Routes ---

# This route serves the main webpage (index.html)
@app.route('/')
def index():
    return render_template('index.html')

# This route is our API endpoint for getting AI responses
@app.route('/api/generate-response', methods=['POST'])
def generate_response():
    # Check if the AI model was loaded correctly
    if not model:
        return jsonify({"error": "Google Gemini API not configured correctly."}), 500

    # Get the patient's message from the request
    data = request.get_json()
    patient_message = data.get('patient_message')

    # Ensure we received a message
    if not patient_message:
        return jsonify({"error": "Patient message is required."}), 400

    try:
        # This is the prompt we send to the AI.
        # It gives the AI its role, instructions, and the patient's message.
        prompt = f"""
        You are CareReply, an AI assistant for healthcare staff.
        Your task is to draft a professional, warm, and empathetic response to a patient's message.
        Do not provide medical advice. If the message suggests an emergency, advise them to call 911 or their doctor's office immediately.
        Keep the response concise and clear.

        Patient's message: "{patient_message}"

        Drafted response:
        """
        
        # Send the prompt to the Gemini model
        response = model.generate_content(prompt)

        # Return the AI's text response in JSON format
        return jsonify({"ai_response": response.text.strip()})

    except Exception as e:
        print(f"🔴 An error occurred during AI generation: {e}")
        return jsonify({"error": "Failed to generate response from AI."}), 500

# --- Run the Application ---
if __name__ == '__main__':
    # This starts the web server on http://127.0.0.1:5000
    app.run(debug=True)