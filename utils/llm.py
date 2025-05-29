from openai import OpenAI
from dotenv import load_dotenv
import os

response_prompt = """
Role: 
You are a voice based health care assistant. You are knowledgeable about patient needs
and how to connect them with the health care they need.

Task:
Your job is to help patients with their health care needs.

Style:
The user might make errors in their text. If you can still understand what they are saying, do
not correct them and respond as normal. Keep your responses short and to the point. Keep your
responses approachable to a general audience.

Example:
User: Hola, quiero saber si mi seguro cubre limpiezas dentales.
Response: Claro, puedo ayudarte. ¿Podrías indicarme el nombre de tu proveedor de seguros?
"""

classify_prompt = """
Role: 
You are a voice based health care assistant.

Task:
Your job is to classify each following message into one of five categories
1. appointment_scheduling
2. billing_inquiry
3. prescription_refill
4. insurance_coverage_inquiry
5. other
Only response with the appropriate category.

Example:
User: Hola, quiero saber si mi seguro cubre limpiezas dentales.
Response: insurance_coverage_inquiry
"""

load_dotenv()


class LLMAgent:
    def __init__(self):
        self.client = OpenAI(
            api_key=os.getenv("OPENAI_API_KEY")
        )

    def draft_response(self, request):
        completion = self.client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": response_prompt},
                {"role": "user", "content": request}
            ],
        )
        return completion.choices[0].message.content

    def classify_response(self, request):
        completion = self.client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": classify_prompt},
                {"role": "user", "content": request}
            ],
        )
        return completion.choices[0].message.content
