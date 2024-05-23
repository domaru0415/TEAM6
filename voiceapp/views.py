from django.http import JsonResponse
from google.cloud import speech

def recognize(request):
    if request.method == 'POST' and 'text' in request.POST:
        text = request.POST['text']

        # Google Cloud Speech-to-Text API 호출
        client = speech.SpeechClient()
        audio = speech.RecognitionAudio(content=text)
        config = speech.RecognitionConfig(
            encoding=speech.RecognitionConfig.AudioEncoding.LINEAR16,
            language_code='en-US'
        )

        response = client.recognize(config=config, audio=audio)
        recognized_text = response.results[0].alternatives[0].transcript

        return JsonResponse({'recognized_text': recognized_text})

    return JsonResponse({'error': 'Invalid request'})

