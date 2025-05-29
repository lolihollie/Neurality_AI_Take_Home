import os
from openai import OpenAI

role = """
You are a voice based health care assistant.
"""

one_shot = """
An example of a desirable response is as follows
User: Hola, quiero saber si mi seguro cubre limpiezas dentales.
Response: Claro, puedo ayudarte. ¿Podrías indicarme el nombre de tu proveedor de seguros?
"""

system_prompt = f"""
{role}

{one_shot}
"""

class LLMAgent:
    def __init__(self):
        self.client = OpenAI(
            api_key=os.environ["OPENAI_API_KEY"],
        )

    def draft_response(self, request):
        completion = self.client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": request}
            ],
        )
        return completion.choices[0].message.content
