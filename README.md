# CareReply - AI Patient Message Responder

CareReply is a web application designed for healthcare staff to generate professional, consistent, and empathetic responses to patient messages using the power of generative AI. This tool helps reduce response time while ensuring high-quality communication.

*This project serves as a complete prototype, from initial requirements to a secure, deployment-ready application.*

## 🚀 Core Features

-   **AI-Powered Responses:** Leverages the Google Gemini API to draft intelligent and context-aware replies.
-   **Professional & Empathetic Tone:** The AI is specifically prompted to maintain a supportive and professional tone suitable for healthcare settings.
-   **User-Friendly Interface:** A clean, futuristic, single-page web interface for ease of use.
-   **Review & Edit:** Staff can review and edit the AI-generated suggestion before use.
-   **Copy Functionality:** Easily copy the finalized response to the clipboard.

## 🛠️ Tech Stack

-   **Backend:** Python 3 with Flask
-   **Frontend:** HTML5, CSS3, vanilla JavaScript
-   **AI:** Google Gemini Pro (`gemini-1.0-pro`)
-   **Deployment:** Ready for production with Gunicorn and containerization using Docker.

## ⚙️ Setup and Running the Project Locally

To run this project on your local machine, please follow these steps:

1.  **Clone the repository:**
    ```sh
    git clone [https://github.com/Aditya-Rai0/CareReply-AI-Patient-Message-Responder.git](https://github.com/Aditya-Rai0/CareReply-AI-Patient-Message-Responder.git)
    cd CareReply-AI-Patient-Message-Responder
    ```

2.  **Create an environment file:**
    Create a file named `.env` in the root of the project. This file is ignored by Git to keep your secrets safe. Add your Google Gemini API key to this file:
    ```
    GEMINI_API_KEY="YOUR_API_KEY_HERE"
    ```

3.  **Install the required dependencies:**
    ```sh
    pip install -r requirements.txt
    ```

4.  **Run the Flask application:**
    ```sh
    python app.py
    ```

5.  Open your web browser and navigate to `http://127.0.0.1:5000`.

## 📜 License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
