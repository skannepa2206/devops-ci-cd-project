from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "🚀 DevOps Automation in Action!"

if __name__ == "__main__":
    # Make sure to bind to 0.0.0.0 to be accessible from outside the container
    app.run(host="0.0.0.0", port=5000, debug=False)