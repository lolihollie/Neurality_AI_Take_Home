from utils.stt import STTAgent
from utils.llm import LLMAgent
import json

if __name__ == "__main__":
    print("Initializing Models...")
    stt = STTAgent()
    llm = LLMAgent()

    print("Transcribing Audio...")
    out = stt.transcribe("sample_audio.mp3")

    print("Classifying Intent...")
    out["intent"] = llm.classify_response(out["transcript"])

    print("Writing Response...")
    out["response"] = llm.draft_response(out["transcript"])

    print("Outputting JSON...")
    with open("sample_output.json", 'w') as json_file:
        json.dump(out, json_file)




