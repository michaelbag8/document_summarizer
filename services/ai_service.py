
class FakeAIModel:
    def generate(self, prompt):
        return f"AI-generated summary: {prompt}"

def generate_summary(prompt, model_service):
    return model_service.generate(prompt)
    r

model = FakeAIModel()
prompt = "Who are you?"

print(generate_summary(prompt, model))