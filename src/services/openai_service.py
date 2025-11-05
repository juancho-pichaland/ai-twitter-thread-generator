import openai
import os

class OpenAIService:
    def __init__(self):
        openai.api_key = os.getenv("OPENAI_API_KEY")
        self.model = "gpt-3.5-turbo"

    def create_thread(self, topic):
        prompt = f"Crea un hilo de Twitter informativo y atractivo sobre el tema: '{topic}'. Limita cada tweet a 280 caracteres."
        response = openai.ChatCompletion.create(
            model=self.model,
            messages=[{"role": "user", "content": prompt}],
            temperature=0.7
        )
        return response['choices'][0]['message']['content']
