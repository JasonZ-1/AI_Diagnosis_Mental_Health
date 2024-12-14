from flask import Flask, render_template, redirect, request

import sys
import os
import json

try:
    import google.generativeai as genai
except ModuleNotFoundError:
    import subprocess
    
    subprocess.run([sys.executable, "-m", "pip", "install", "-U", "google-generativeai"])
    import google.generativeai as genai
    
try:
    from dotenv import load_dotenv, dotenv_values
except ModuleNotFoundError:
    import subprocess
    
    subprocess.run([sys.executable, "-m", "pip", "install", "python-dotenv"])
    from dotenv import load_dotenv, dotenv_values

load_dotenv()

app = Flask(__name__)

app.config["TEMPLATES_AUTO_RELOAD"] = True

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        message = request.form.get("prompt")

        if not message:
            return redirect("/")
        
        output = askAI(f"""
    Someone says this: {message}. Provide a list of 15 yes or no questions about other symptoms they may be having to try to predict a diagnosis. The questions should be related to a health problem they might be having. Provide the questions in JSON format.

    Use this JSON schema:

    questions = list[str]
    """).text
        
        return render_template("index.html", output = output)
    else:
        return render_template("index.html")
    
def askAI(message):
    key = os.getenv("API_KEY")

    genai.configure(api_key=key)
    model = genai.GenerativeModel("gemini-2.0-flash-exp", generation_config={"response_mime_type": "application/json"})
    
    prompt = message
    response = model.generate_content(prompt)
    return response
