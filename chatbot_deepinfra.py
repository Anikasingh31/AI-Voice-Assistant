import pyttsx3
import speech_recognition as sr
from openai import OpenAI

def read_conversation(filename):
    conversation_dict = {}
    with open(filename, 'r', encoding="utf-8") as file:
        for line in file:
            line = line.strip()
            if ',' in line:  # Ensure there is a comma before splitting
                question, answer = line.split(',', 1)
                conversation_dict[question.lower()] = answer
            else:
                print(f"Skipping invalid line: {line}")  # Debugging message
    return conversation_dict


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

def recognize_speech(engine, recognizer):
    conversation_dict = read_conversation('conversation.txt')
    print("Listening for audio...")

    while True:
        with sr.Microphone() as source:
            recognizer.adjust_for_ambient_noise(source)  # Adjust for background noise
            print("Listening for audio...")
            audio = recognizer.listen(source)

        try:
            print("Recognizing audio...")
            recognized_text = recognizer.recognize_google(audio, language="en-US")  # Specify language
            print("You said:", recognized_text)

            # Conversation logic
            response = get_response(recognized_text, conversation_dict)
            print("Responding:", response)
            engine.say(response)
            engine.runAndWait()

            # Exit if user says "goodbye"
            if recognized_text.lower() == "goodbye":
                print("Conversation ended.")
                break

        except sr.UnknownValueError:
            print("Sorry, I couldn't understand the audio.")
        except sr.RequestError as e:
            print("Error occurred; {0}".format(e))

def get_response(input_text, conversation_dict):
    # Search for question in conversation_dict
    for question, answer in conversation_dict.items():
        if question in input_text.lower():
            return answer
    return get_deepinfra_response(input_text)  # Use Deep Infra API for unknown questions

if __name__ == "__main__":
    name = input("What is your name? ")
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[1].id)
    recognizer = sr.Recognizer()  # Initialize the recognizer object

    print("Hello", name + "! How are you today? I am maya. I am here to help you in this lab with everything you need.")
    engine.say("Hello " + name + "! How are you today? I am maya. I am here to help you in this lab with everything you need.")
    engine.runAndWait()

    recognize_speech(engine, recognizer)  # Pass the recognizer object to the recognize_speech function
