from flask import Flask, render_template
import requests
import os

app = Flask(__name__)

BACKEND_URL = os.environ.get("BACKEND_URL", "http://backend-service:5000/api/message")

@app.route("/")
def home():
    message = "Unable to connect to backend"
    try:
        response = requests.get(BACKEND_URL, timeout=5)
        if response.status_code == 200:
            message = response.json().get("message", "No message received")
    except Exception as e:
        message = f"Error: {str(e)}"
    return render_template("index.html", message=message)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001)