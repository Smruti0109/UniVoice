# UniVoice
UniVoice is a Streamlit-based application that enables users to translate spoken language into another language, providing both text and speech output. The tool utilizes speech recognition, translation models, and text-to-speech conversion.

## Features

- **Speech Recognition**: Converts spoken words into text.
- **Text Translation**: Translates recognized text into a target language.
- **Text-to-Speech**: Converts translated text into speech.
- **Multi-Language Support**: Supports over 20 languages for translation and speech synthesis.

## Technologies Used

- **Streamlit**: For building the web interface.
- **SpeechRecognition**: For converting speech to text.
- **Google Text-to-Speech (gTTS)**: For text-to-speech conversion.
- **Hugging Face Transformers**: For translation using the facebook/m2m100_418M model.
- **Python**: Core language for development.

## Installation

Follow the steps below to set up the project on your local machine:

### 1. Clone the repository

```bash
git clone https://github.com/Smruti0109/UniVoice.git
```
### 2. Install dependencies

```bash
pip install -r requirements.txt
```
### 2. Run the Flask Application

```bash
streamlit run app.py
```
## How it Works

- **Select Languages**: Choose source and target languages from the dropdown menus.
- **Speak**: Click the Speak and Translate button and speak in the selected source language.
- **Processing**:The app converts speech to text then the text is translated into the target language and finaaly the translated text is converted into speech.
- **Listen**: The translated speech is played back to the user.

## Acknowledgements

- **Hugging Face Transformers**: For multilingual translation.
- **Google Speech Recognition**: For speech-to-text processing.
- **Google Text-to-Speech (gTTS)**: For converting text to speech.
