# AI Voice Assistant

This AI Voice Assistant utilizes **DeepInfra API** for AI-generated responses, **Google Speech Recognition** for voice input processing, and **pyttsx3** for text-to-speech conversion.

## Features
- Recognizes speech using **Google Speech Recognition**.
- Generates AI-driven responses using **DeepInfra's Mistral-8x7B-Instruct model**.
- Converts text responses to speech using **pyttsx3**.
- Uses a predefined conversation dictionary to answer common queries.
- Falls back on DeepInfra API for unknown queries.

## Dependencies
Ensure you have the following Python libraries installed:
```sh
pip install pyttsx3 SpeechRecognition openai
```

## Setup Instructions
1. **Generate a DeepInfra API Key:**
   - Go to [DeepInfra](https://deepinfra.com) and create an account.
   - Navigate to the API section and generate your API key.
   - Replace `YOUR_API_KEY_HERE` in the code with your actual API key.

2. **Run the Program:**
```sh
python deepinfra.py
```

## **3. Running on NVIDIA Jetson (Optional):**

We tested this program on an NVIDIA Jetson due to its powerful GPU capabilities.
In the future, if we decide to use a Local Language Model (LLM) instead of the DeepInfra API, we plan to leverage the Jetson's processing power for efficient model inference.
## Usage
- Run the script and follow the on-screen instructions.
- Speak into your microphone when prompted.
- The AI will recognize your speech and respond accordingly.

## Error Handling
- If the conversation file (`conversation.txt`) contains improperly formatted lines, the program may throw a `ValueError`. Ensure that each line follows the format:
  ```
  question,answer
  ```
- If the microphone is not detected, check your audio input settings.
- If DeepInfra API is unavailable, verify your API key and internet connection.


## Contributors
- Developed by students at **SRM Institute of Science and Technology**.


