from flask import Flask, request, jsonify
import hashlib
import base64

app = Flask(__name__)

VERIFICATION_TOKEN = "WSAListingAutomationVerification12345"
ENDPOINT = "https://wsa-ebay-webhook.onrender.com/notify"

@app.route("/notify", methods=["GET", "POST"])
def notify():
    challenge_code = request.args.get("challenge_code")

    if challenge_code:
        challenge = challenge_code + VERIFICATION_TOKEN + ENDPOINT
        digest = hashlib.sha256(challenge.encode("utf-8")).digest()
        response = base64.b64encode(digest).decode()
        return jsonify({"challengeResponse": response})

    return "", 200

@app.route("/", methods=["GET"])
def home():
    return "OK", 200
