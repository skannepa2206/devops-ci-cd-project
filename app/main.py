# app/main.py
from flask import Flask
import os

app = Flask(__name__)

@app.route("/")
def home():
    return "🚀 DevOps AI Automation in Action!"

# Print debugging information on startup
if __name__ == "__main__":
    print("Starting Flask application...")
    print(f"Environment: {os.environ}")
    print("Binding to 0.0.0.0:5000")
    app.run(host="0.0.0.0", port=5000, debug=False)