from groq import Groq

class GroqAIModel:
    def __init__(self, model_id="openai/gpt-oss-120b"):
        self.client = Groq()
        self.model_id = model_id

    def generate(self, prompt):
        completion = self.client.chat.completions.create(
            model=self.model_id,
            messages=[
                {
                    "role": "user",
                    "content": prompt
                }
            ]
        )

        return completion.choices[0].message.content

def generate_summary(prompt, model_service):
    return model_service.generate(prompt)