import speech_recognition as sr
from gtts import gTTS
import os
import streamlit as st
from transformers import pipeline


def recognize_speech(src_lang):
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Please speak...")
        audio = recognizer.listen(source)
    try:
        # Recognizing speech in the selected language
        text = recognizer.recognize_google(audio, language=src_lang)
        return text
    except sr.UnknownValueError:
        return "Sorry, could not understand your speech."
    except sr.RequestError:
        return "Service unavailable."


def translate_text(input_text, src_lang, tgt_lang):
    # Use the facebook/m2m100_418M model for translation between any languages
    translator = pipeline("translation", model="facebook/m2m100_418M")
    translation = translator(input_text, src_lang=src_lang, tgt_lang=tgt_lang)
    return translation[0]['translation_text']


def text_to_speech(text, tgt_lang, output_file):
    # Convert text to speech in the target language
    tts = gTTS(text=text, lang=tgt_lang)
    tts.save(output_file)
    os.system(f"start {output_file}")


# Expanded list of available languages (with codes for source and target)
languages = {
    "English": "en",
    "Spanish": "es",
    "French": "fr",
    "German": "de",
    "Italian": "it",
    "Portuguese": "pt",
    "Dutch": "nl",
    "Hindi": "hi",
    "Chinese": "zh",
    "Arabic": "ar",
    "Russian": "ru",       
    "Japanese": "ja",      
    "Korean": "ko",        
    "Turkish": "tr",      
    "Swedish": "sv",      
    "Polish": "pl",       
    "Greek": "el",         
    "Thai": "th",        
    "Indonesian": "id",    
    "Finnish": "fi",       
    "Czech": "cs",       
    "Danish": "da"        
}


st.title("Speech Translation Tool")


# Language selection
src_lang = st.selectbox("Select Source Language", list(languages.keys()))
tgt_lang = st.selectbox("Select Target Language", list(languages.keys()))


# Get language codes based on selection
src_lang_code = languages[src_lang]
tgt_lang_code = languages[tgt_lang]


if st.button("Speak and Translate"):
    st.text("Listening...")
    recognized_text = recognize_speech(src_lang_code)
    st.write(f"Recognized Text: {recognized_text}")


    if recognized_text:
        translated_text = translate_text(recognized_text, src_lang_code, tgt_lang_code)
        st.write(f"Translated Text: {translated_text}")


        st.text("Generating Speech...")
        output_file = "translated_speech.mp3"
        text_to_speech(translated_text, tgt_lang_code, output_file)
        st.audio(output_file)



