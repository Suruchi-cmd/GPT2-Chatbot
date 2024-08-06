import os
from flask import Flask, request, jsonify, render_template
from transformers import GPT2LMHeadModel, GPT2Tokenizer
from datetime import datetime
import time
import ngrok
import threading

ngrok.set_auth_token('2kGrBZhxLDOSsT3UNs5tVpOJmfq_7Z8vLFaW6VvHEusYUHNme')

app = Flask(__name__)
# run_with_ngrok(app)

# Setup ngrok
def start_ngrok():
    public_url = ngrok.connect(5000)
    print("ngrok tunnel \"{}\" -> \"http://127.0.0.1:5000\"".format(public_url))

# Start ngrok when app is run
threading.Thread(target=start_ngrok).start()

# Load the fine-tuned model and tokenizer
model_name = "SuruchiDS/PetersLectures"
model = GPT2LMHeadModel.from_pretrained(model_name)
tokenizer = GPT2Tokenizer.from_pretrained(model_name)


import matplotlib.pyplot as plt

# Data for the graphs
categories = ['Manual Reading', 'AI Retrieval']
reading_time = [45, 5]  # in minutes

tasks = ['Searching for Information', 'Other Tasks']
time_spent = [2.5, 5.5]  # in hours per day

productivity = ['Without AI', 'With AI']
productivity_increase = [100, 140]  # percentage

disabilities = ['With Disabilities', 'Without Disabilities']
accessibility = [15, 85]  # percentage of world population

# Create subplots
fig, axs = plt.subplots(2, 2, figsize=(12, 10))

# Average Reading Time vs. AI Retrieval Time
axs[0, 0].bar(categories, reading_time, color=['blue', 'green'])
axs[0, 0].set_title('Average Reading Time vs. AI Retrieval Time')
axs[0, 0].set_ylabel('Time (minutes)')

# Time Spent Searching for Information
axs[0, 1].bar(tasks, time_spent, color=['blue', 'green'])
axs[0, 1].set_title('Time Spent Searching for Information')
axs[0, 1].set_ylabel('Time (hours per day)')

# Productivity Increase with AI
axs[1, 0].bar(productivity, productivity_increase, color=['blue', 'green'])
axs[1, 0].set_title('Productivity Increase with AI')
axs[1, 0].set_ylabel('Productivity (%)')

# Accessibility for People with Disabilities
axs[1, 1].pie(accessibility, labels=disabilities, autopct='%1.1f%%', colors=['blue', 'green'])
axs[1, 1].set_title('Accessibility for People with Disabilities')

# Adjust layout
plt.tight_layout()
plt.show()



# Initial system message setting the context
conversation_history = [ 
]

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():
    global conversation_history

    start_time = time.time()  # Capture start time

    user_input = request.json["user_input"]

    # Add user input to conversation history
    conversation_history.append({
        "role": "user",
        "content": user_input
    })

    # Generate response from the model
    def generate_answer(question, model, tokenizer):
        input_text = f" {question}"
        inputs = tokenizer(input_text, return_tensors='pt')
        outputs = model.generate(inputs.input_ids, max_length=200, num_return_sequences=1, no_repeat_ngram_size=2, early_stopping=True)
        answer = tokenizer.decode(outputs[0], skip_special_tokens=True)
        return answer

    ai_response = generate_answer(user_input, model, tokenizer)

    # Add AI response to conversation history
    conversation_history.append({
        "role": "assistant",
        "content": ai_response
    })

# Start Flask server
if __name__ == "__main__":
    app.run()
