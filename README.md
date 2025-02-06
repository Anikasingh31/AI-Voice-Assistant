# AI Voice Assistant (Maya)

This project implements a Flask-based AI Voice Assistant named **Maya**. It integrates speech recognition and text-to-speech functionalities, using **pyttsx3** for voice output and **Google’s Speech Recognition API** for voice input. The assistant answers questions using a pre-defined conversation list or an external API (DeepInfra).

## Features:
- Greet users with a personalized message.
- Recognize speech and provide a response.
- Use text-to-speech to reply to the user.
- Integrates with **OpenAI's DeepInfra API** for intelligent responses.

## Project Structure:

/voice-assistant
  ├── app.py                   # Flask backend
  ├── chatbot_deepinfra.py      # Your existing chatbot logic
  ├── templates/
  │   ├── index.html           # Frontend UI (HTML)
  ├── conversation.txt         # Predefined conversation data
  ├── requirements.txt         # Dependencies file


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
'''

