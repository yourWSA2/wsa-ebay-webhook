from flask import Flask, request, jsonify
import hashlib

app = Flask(__name__)

VERIFICATION_TOKEN = "WSAListingAutomationVerification12345"
ENDPOINT = "https://wsa-ebay-webhook.onrender.com/notify"

@app.route("/notify", methods=["GET", "POST"])
def notify():
    challenge_code = request.args.get("challenge_code")

    if challenge_code:
        challenge_response = hashlib.sha256(
            (challenge_code + VERIFICATION_TOKEN + ENDPOINT).encode("utf-8")
        ).hexdigest()
        return jsonify({"challengeResponse": challenge_response}), 200

    return "", 200

@app.route("/", methods=["GET"])
def home():
    return "OK", 200
