from flask import Flask, request, jsonify, render_template, send_from_directory
from transformers import pipeline
import os

app = Flask(__name__, static_folder="../frontend", template_folder="../frontend")


model_path = os.path.join(os.path.dirname(__file__), "../fine_tune/fine_tuned_model")


if not os.path.exists(model_path):
    raise ValueError(f"Model directory not found: {model_path}")

print(f"Loading fine-tuned model from: {model_path}")


generator = pipeline("text2text-generation", model=model_path, tokenizer=model_path)

@app.route("/", methods=["GET"])
def home():
    return render_template("create an account.html")

@app.route("/generate", methods=["POST"])
def generate():
    data = request.json
    skills = data.get("skills", "").strip()
    interests = data.get("interests", "").strip()
    budget = data.get("budget", "").strip()

    
    if not skills or not interests or not budget:
        return jsonify({"error": "All fields (skills, interests, budget) are required"}), 400

   
    prompt = (
        f"Based on the following details:\n"
        f"- Skills: {skills}\n"
        f"- Interests: {interests}\n"
        f"- Budget: ${budget}\n"
        f"Suggest a unique, well-detailed startup idea including:\n"
        f"- Business model\n"
        f"- Target audience\n"
        f"- Revenue model\n"
        f"- Competitive advantage\n"
        f"- Implementation steps."
    )

    
    print(f"Prompt sent to model: {prompt}")

    
    result = generator(prompt, max_length=300, temperature=0.7, top_p=0.9, top_k=50, num_return_sequences=1)

   
    generated_idea = result[0]["generated_text"]
    print(f"Generated Output: {generated_idea}")

    return jsonify({"startup_idea": generated_idea})

@app.route('/<path:filename>')
def static_files(filename):
    return send_from_directory(app.static_folder, filename)

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000, debug=True)
