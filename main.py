from utils.stt import STTAgent
from utils.llm import LLMAgent
import os
import whisper

if __name__ == "__main__":
    model = whisper.load_model("base")
    result = model.transcribe("C:/Users/zheng/PycharmProjects/neurality_takehome/audio.mp3")
    print(result)




