from flask import Flask
import os

app = Flask(__name__)

@app.route("/")
def home():
    return "🚀 DevOps Automation in Action!"

if __name__ == "__main__":
    # Print startup information
    print("Starting Flask application...")
    print(f"FLASK_APP: {os.environ.get('FLASK_APP')}")
    print("Binding to 0.0.0.0:5000")
    # Explicitly bind to all interfaces
    app.run(host="0.0.0.0", port=5000, debug=False)