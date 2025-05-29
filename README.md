# Neurality_AI_Take_Home

**Tools & Libraries**
- OpenAI (intent classification + response generation)
- OpenAI Whisper (speech parsing + language identification)

**Assumptions & Shortcuts**
- For the sake of time, the code does not have all the sufficient error handling necessary for production level code.
- The input language is one of the supported types that both ChatGPT 3.5 Turbo and Whisper can parse.

**Scaling + Production Considerations**
- To run a similar model into production, the LLM solution would need to be customized to best fit the array of intents that the voice agent would be used for
- This code would either be hosted in the cloud (ex Amazon AWS) or would be hosted on a local server farm and be accessible through an API endpoint (ex. Django, Flask)
