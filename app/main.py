from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "🚀 DevOps Automation in Action YaaY- Update1!"

if __name__ == "__main__":
    # Explicitly bind to all interfaces (0.0.0.0) and port 5000
    print("Starting Flask application on 0.0.0.0:5000")
    app.run(host="0.0.0.0", port=5000, debug=False)