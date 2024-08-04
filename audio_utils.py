import requests
import numpy as np
import soundfile as sf
import speech_recognition as sr
from config import language

def download_file(file_url):
    file_path = "voice_message.ogg"
    with open(file_path, "wb") as f:
        response = requests.get(file_url)
        f.write(response.content)
    return file_path

def convert_to_pcm16(file_path):
    data, samplerate = sf.read(file_path)
    data = (data * 32767).astype(np.int16)
    sf.write('new.wav', data, samplerate)

def progress_audio_file(file_path):
    recognizer = sr.Recognizer()
    with sr.AudioFile(file_path) as source:
        audio_data = recognizer.listen(source)
    try:
        text = recognizer.recognize_google(audio_data, language)
        return text
    except sr.UnknownValueError:
        return None
