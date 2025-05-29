import whisper


class STTAgent:
    def __init__(self):
        self.model = whisper.load_model("base")

    def transcribe(self, audio_file):
        audio = whisper.load_audio(audio_file)
        audio = whisper.pad_or_trim(audio)

        mel = whisper.log_mel_spectrogram(audio, n_mels=self.model.dims.n_mels)

        _, probs = self.model.detect_language(mel)
        lang = max(probs, key=probs.get)
        conf = probs[lang]

        options = whisper.DecodingOptions()
        result = whisper.decode(self.model, mel, options)

        return {
            "transcript": result.text,
            "language": lang,
            "confidence": conf
        }
