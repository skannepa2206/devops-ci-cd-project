from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "🚀 DevOps Automation in Action!"

if __name__ == "__main__":
    # Bind to all network interfaces, not just 127.0.0.1
    app.run(host="0.0.0.0", port=5000, debug=False)