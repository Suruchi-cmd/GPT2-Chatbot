# Chatbot Flask Application

A chatbot application that serves a fine-tuned GPT-2 model using Flask, with the model deployed on Hugging Face Spaces.

## Table of Contents
- [Chatbot Flask Application](#chatbot-flask-application)
  - [Table of Contents](#table-of-contents)
  - [Introduction](#introduction)
  - [Features](#features)
  - [Installation](#installation)
    - [Prerequisites](#prerequisites)
    - [Setup](#setup)
  - [Usage](#usage)
    - [Running the Flask App](#running-the-flask-app)
    - [Using the Jupyter Notebook](#using-the-jupyter-notebook)
  - [Dependencies](#dependencies)
  - [Contributing](#contributing)
  - [License](#license)
  - [Contact](#contact)

## Introduction

This project provides a Flask-based web interface for interacting with a fine-tuned GPT-2 model. The model has been trained on specific conversation data to function as a chatbot, capable of carrying out dialogue and booking appointments.

## Features

- Interactive chatbot interface
- Integration with Hugging Face Spaces for model inference
- Web server accessible via ngrok

## Installation

### Prerequisites

- Python 3.x
- pip
- Jupyter Notebook

### Setup

1. Clone the repository:

   ```bash
   git clone https://github.com/your-username/your-repo-name.git
   cd your-repo-name

2. Create a virtual environment and activate it:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`

3. Install required dependencies
   ```bash
   pip install -r requirements.txt

4. Set Up ngrok
   ```bash
   import ngrok
   ngrok.set_auth_token('your_ngrok_auth_token')


### Usage
## Running the Flask App

1.Navigate to the project directory and run the Flask app:
  ```bash
  export FLASK_APP=chatbot.py  # On Windows use `set FLASK_APP=chatbot.py`
  flask run

### Dependencies
Flask
transformers
torch
jupyter
ngrok


   
