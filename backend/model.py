from transformers import pipeline
import os


script_dir = os.path.dirname(os.path.abspath(__file__))
model_path = os.path.abspath(os.path.join(script_dir, "../fine_tune/fine_tuned_model"))


generator = pipeline("text2text-generation", model=model_path, tokenizer=model_path)

def generate_startup_idea(skills, interests, budget):
    prompt = f"Skills: {skills}, Interests: {interests}, Budget: {budget}. Suggest a startup idea."
    response = generator(prompt, max_length=300)
    return response[0]['generated_text']
