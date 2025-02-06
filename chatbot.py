from transformers import pipeline, AutoModelForCausalLM, AutoTokenizer

model_name = "deepseek-ai/deepseek-llm-7b-base"

# Load the model with increased timeout
model = AutoModelForCausalLM.from_pretrained(model_name, timeout=600)  # Timeout increased to 5 minutes
tokenizer = AutoTokenizer.from_pretrained(model_name, timeout=600)

# Initialize pipeline with loaded model
chatbot = pipeline("text-generation", model=model, tokenizer=tokenizer)

def get_chatbot_response(user_input: str):
    response = chatbot(user_input, max_length=100, do_sample=True)
    return response[0]['generated_text']

