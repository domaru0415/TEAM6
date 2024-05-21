from django.db import models

class SpeechResult(models.Model):
    audio_file = models.FileField(upload_to='audio/')
    recognized_text = models.TextField(blank=True)

    def __str__(self):
        return self.recognized_text[:50]
