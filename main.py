from prompts.prompt_manager import build_summary_prompt
from services.ai_service import FakeAIModel,AnotherFakeAIModel ,generate_summary



document_text = input("Enter your prompt: ")
document_summary = build_summary_prompt(document_text)

model = FakeAIModel()
fakemodel = AnotherFakeAIModel()


print(generate_summary(document_summary, model))
print(generate_summary(document_summary, fakemodel))
