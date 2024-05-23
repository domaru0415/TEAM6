from django.http import JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
import speech_recognition as sr
from pydub import AudioSegment
import io

@csrf_exempt
def speech_to_text(request):
    if request.method == 'POST':
        recognizer = sr.Recognizer()
        audio_file = request.FILES['audio']
        
        # 오디오 파일을 WAV 형식으로 변환
        audio = AudioSegment.from_file(audio_file, format="webm")
        wav_io = io.BytesIO()
        audio.export(wav_io, format="wav")
        wav_io.seek(0)
        
        with sr.AudioFile(wav_io) as source:
            audio = recognizer.record(source)
        
        try:
            text = recognizer.recognize_google(audio, language="ko-KR")
            return JsonResponse({'text': text})
        except sr.UnknownValueError:
            return JsonResponse({'error': 'Could not understand audio'})
        except sr.RequestError as e:
            return JsonResponse({'error': f'Service error: {e}'})
    return JsonResponse({'error': 'Invalid request method'})

def index(request):
    return render(request, 'index.html')

