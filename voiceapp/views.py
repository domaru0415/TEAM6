# voiceapp/views.py
import speech_recognition as sr
from django.shortcuts import render
from .models import SpeechResult

def recognize_speech(request):
    if request.method == 'POST' and 'audio_file' in request.FILES:
        audio_file = request.FILES['audio_file']
        recognizer = sr.Recognizer()
        
        # Save the audio file
        speech_result = SpeechResult(audio_file=audio_file)
        speech_result.save()

        # Recognize speech using Google Web Speech API
        audio_path = speech_result.audio_file.path
        with sr.AudioFile(audio_path) as source:
            audio_data = recognizer.record(source)
            try:
                text = recognizer.recognize_google(audio_data)
                speech_result.recognized_text = text
                speech_result.save()
            except sr.UnknownValueError:
                text = "Could not understand audio"
            except sr.RequestError:
                text = "Could not request results from Google Speech Recognition service"

        return render(request, 'voiceapp/recognize_result.html', {'text': text})

    return render(request, 'voiceapp/recognize.html')
