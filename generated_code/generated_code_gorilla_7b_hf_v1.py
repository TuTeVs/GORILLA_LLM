
from transformers import pipeline

def load_model():
    generator = pipeline('text-generation', model='gpt2-large')
    return generator

def process_data(input_text, generator):
    response = generator(input_text, max_length=100, num_return_sequences=1)
    return response[0]['generated_text']

input_text = "Create a meal planning application that generates healthy and balanced meals based on the user's preferences and budget."

# Load the model
generator = load_model()

# Process the data
response = process_data(input_text, generator)

print(response)