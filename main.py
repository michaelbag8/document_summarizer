from dotenv import load_dotenv

load_dotenv()

from prompts.prompt_manager import build_summary_prompt
from services.ai_service import GroqAIModel, generate_summary

document_text = input("Enter your document: ")

summary_prompt = build_summary_prompt(document_text)

model = GroqAIModel()

result = generate_summary(summary_prompt, model)

print(result)