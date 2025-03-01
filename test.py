from transformers import pipeline

generator = pipeline("text2text-generation", model="fine_tune/fine_tuned_model", tokenizer="fine_tune/fine_tuned_model")

print(generator("Skills: Coding, Interests: AI, Budget: $5000. Suggest a startup idea.", max_length=100)[0]["generated_text"])
