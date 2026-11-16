
import os
from flask import Flask, jsonify

app = Flask(__name__)

# Configuration par variables d'environnement
MESSAGE = os.getenv("APP_MESSAGE","Bienvenue dans la version 1.0.1 ")
APP_VERSION = os.getenv("APP_VERSION", "1.0.0")


@app.route("/")
def home():
    return f"""
    <!DOCTYPE html>
    <html lang="fr">
    <head>
        <meta charset="UTF-8">
        <title>DevOps Flask App</title>
        <style>
            body {{
                font-family: Arial, sans-serif;
                background: #f1f5f9;
                text-align: center;
                padding: 100px 20px;
            }}
            .container {{
                background: white;
                padding: 40px;
                border-radius: 15px;
                max-width: 600px;
                margin: auto;
                box-shadow: 0 5px 20px #0001;
            }}
            h1 {{ color: #2563eb; }}
        </style>
    </head>
    <body>
        <div class="container">
            <h1>DevOps Flask Application</h1>
            <h2>{MESSAGE}</h2>
            <p>Version : {APP_VERSION}</p>
            <p>Application conteneurisée avec Docker</p>
        </div>
    </body>
    </html>
    """


@app.route("/health")
def health():
    return jsonify({
        "status": "healthy",
        "application": "DevOps Flask App",
        "version": APP_VERSION
    })


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
