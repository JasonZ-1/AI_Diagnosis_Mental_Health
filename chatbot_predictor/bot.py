# if there is an error, run "pip install -U google-generativeai" to install the package for ai
try:
    import google.generativeai as genai
except ModuleNotFoundError:
    import subprocess
    import sys
    subprocess.run([sys.executable, "-m", "pip", "install", "-U", "google-generativeai"])
    import google.generativeai as genai

key = ""
with open("chatbot_predictor/ApiKey.txt", "r") as f:
    key = f.read().strip()

genai.configure(api_key=key)
model = genai.GenerativeModel("gemini-2.0-flash-exp")

prompt = """
Someone has a cough. Provide a list of 15 yes or no questions about other symptoms they may be having to try to predict a diagnosis. The questions should be related to a health problem they might be having. Provide the questions in JSON format.

Use this JSON schema:

questions = list[str]
"""

response = model.generate_content(prompt)
print(response.text)