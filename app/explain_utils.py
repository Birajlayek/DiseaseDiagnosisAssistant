from transformers import pipeline

# Load LLM
llm = pipeline("text2text-generation", model="google/flan-t5-large")

def get_disease_explanation(disease):
    prompt = f"Explain the disease {disease} with its symptoms, causes, and treatments."
    response = llm(prompt, max_length=200, num_return_sequences=1)
    return response[0]['generated_text']