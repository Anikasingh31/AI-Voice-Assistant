# AI Voice Assistant (Maya)

This project implements a Flask-based AI Voice Assistant named **Maya**. It integrates speech recognition and text-to-speech functionalities, using **pyttsx3** for voice output and **Google’s Speech Recognition API** for voice input. The assistant answers questions using a pre-defined conversation list or an external API (DeepInfra).

## Features:
- Greet users with a personalized message.
- Recognize speech and provide a response.
- Use text-to-speech to reply to the user.
- Integrates with **OpenAI's DeepInfra API** for intelligent responses.

## Project Structure:
```
/voice-assistant
  ├── app.py                   # Flask backend
  ├── chatbot_deepinfra.py      # Your existing chatbot logic
  ├── templates/
  │   ├── index.html           # Frontend UI (HTML)
  ├── conversation.txt         # Predefined conversation data
  ├── requirements.txt         # Dependencies file
```

## Prerequisites:
- **Python 3.x**
- **Flask**
- **pyttsx3**
- **SpeechRecognition**
- **OpenAI API** (for the DeepInfra integration)

## Installation & Setup:

### 1. Clone the repository:
```bash
git clone https://github.com/yourusername/voice-assistant.git
cd voice-assistant
```
### 1. Install Dependencies:
```bash
pip install -r requirements.txt
```

### 3. API Key:
You'll need an OpenAI API key for the DeepInfra API integration.
Replace the api_key in the chatbot_deepinfra.py file with your actual OpenAI API key:

```
openai = OpenAI(
    api_key="YOUR_API_KEY",
    base_url="https://api.deepinfra.com/v1/openai",
)
```
### 4. Conversation Data:
Prepare a file conversation.txt that contains the conversation data in the format
  question1, answer1
  question2, answer2

### 5. 5. Running the Flask App:
Run the Flask app using the following command
```
python app.py

```
### Additional Notes:
Speech Recognition: The app uses Google’s Speech Recognition API for converting speech to text. Make sure you have a working microphone for this functionality.
Text-to-Speech: The app uses pyttsx3 to generate speech output.
Flask: Flask serves the frontend and handles API routes for starting the chat and listening to speech.
DeepInfra API: The assistant uses DeepInfra (based on OpenAI's models) to handle complex user queries.


