from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "🚀 DevOps Automation in Action YaaaY!"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)


#Test4