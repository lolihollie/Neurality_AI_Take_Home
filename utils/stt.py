import whisper

class STTAgent:
    def __init__(self):
        self.model = whisper.load_model("turbo")

    def transcribe(self, audio_path):
        transcription = self.model.transcribe(audio_path)
        return transcription["text"]

