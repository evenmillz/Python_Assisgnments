# Sets up a chatbot using the GPT-2 language model 
# (a powerful language model  used for generating human-like text responses.).
# It loads the GPT-2 model and tokenizer 
# (the element that prepares text for processing by a language model), 
# defines a function to generate responses based on user input, 
# and runs a chat loop where the user can interact with the chatbot by entering messages. 
# Each message is processed by the model, and the generated response is displayed.

import os
os.environ["TF_CPP_MIN_LOG_LEVEL"] = "3"  # Suppress TensorFlow warnings

import torch
from transformers import GPT2LMHeadModel, GPT2Tokenizer

# Load pre-trained model and tokenizer
model_name = "gpt2-medium" # Use a smaller model variant
model = GPT2LMHeadModel.from_pretrained(model_name)
tokenizer = GPT2Tokenizer.from_pretrained(model_name)

# Set device
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
model.to(device)

# Generate response using GPT-2
def generate_response(user_input):
    input_ids = tokenizer.encode(user_input, return_tensors="pt").to(device)
    output = model.generate(input_ids, max_length=60, pad_token_id=tokenizer.eos_token_id)
    response = tokenizer.decode(output[0], skip_special_tokens=True)

# Chat loop
while True:
    user_input = input("Enter your message: ")
    if user_input.lower() == "exit":
        print("Exiting chat.")
        break
    response = generate_response(user_input)
    print(f"ChatGPT: {response}")