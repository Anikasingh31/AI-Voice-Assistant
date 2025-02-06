from flask import Flask, render_template, request, jsonify
import pyttsx3
import speech_recognition as sr
from openai import OpenAI

app = Flask(__name__)

# Load conversation data
def read_conversation(filename):
    conversation_dict = {}
    with open(filename, 'r', encoding="utf-8") as file:
        for line in file:
            line = line.strip()
            if ',' in line:  # Ensure there is a comma before splitting
                question, answer = line.split(',', 1)
                conversation_dict[question.lower()] = answer
    return conversation_dict

conversation_dict = read_conversation('conversation.txt')

# DeepInfra API function
def get_deepinfra_response(prompt):
    openai = OpenAI(
        api_key="5hveEi9qdcEtFZXit3iNex1ZFhG0nQ8F",
        base_url="https://api.deepinfra.com/v1/openai",
    )

    chat_completion = openai.chat.completions.create(
        model="mistralai/Mixtral-8x7B-Instruct-v0.1",
        messages=[{"role": "user", "content": prompt}],
    )

    return chat_completion.choices[0].message.content

# Get chatbot response
def get_response(input_text):
    for question, answer in conversation_dict.items():
        if question in input_text.lower():
            return answer
    return get_deepinfra_response(input_text)

# Speech recognition function
def recognize_speech():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        recognizer.adjust_for_ambient_noise(source)
        print("Listening...")
        audio = recognizer.listen(source)
    try:
        recognized_text = recognizer.recognize_google(audio, language="en-US")
        return recognized_text
    except sr.UnknownValueError:
        return "Sorry, I couldn't understand."
    except sr.RequestError as e:
        return f"Error: {e}"

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/start_chat', methods=['POST'])
def start_chat():
    name = request.form.get('name')
    greeting = f"Hello {name}! How are you today? I am Maya, here to assist you."

    # Fix: Create a new pyttsx3 instance inside the function
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[1].id)  # Female voice
    engine.say(greeting)
    engine.runAndWait()

    return jsonify({"message": greeting})

@app.route('/listen', methods=['POST'])
def listen():
    user_input = recognize_speech()
    response = get_response(user_input)

    # Fix: Create a new pyttsx3 instance for every request
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[1].id)  # Female voice
    engine.say(response)
    engine.runAndWait()

    return jsonify({"user_input": user_input, "response": response})

if __name__ == '__main__':
    app.run(debug=True)
