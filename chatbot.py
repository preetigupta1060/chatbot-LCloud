


from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# Basic rule-based response logic
def get_bot_response(user_input):
    user_input = user_input.lower()

    responses = {
        "what is the new migration strategy": "We are moving from split environments to lift n shift approach!",
        "Migration Timeline": "Migration Timelines are still being developed!",
        "Where are LCloud documents stored": "You can find the documents at https://teams.microsoft.com/l/channel/19%3AU8yJakAm-sKMzViwPKnAbEcb5Dfz-DcM6jkEemGs1YQ1%40thread.tacv2/General?groupId=6d068f51-0740-4be7-bbc8-6c9fd39062f1&tenantId=d6b0474e-14ab-41bb-adbd-8c39f8f21582",
        "Talk to the Team": "Protera",
        "bye": "Goodbye!"
    }

    for key in responses:
        if key.lower() in user_input:
            return responses[key]
    return "Sorry, I didn't understand that."

@app.route("/")
def home():
    return render_template("chat3.html")

@app.route("/chat", methods=["POST"])
def chat():
    user_message = request.json.get("message")
    response = get_bot_response(user_message)
    return jsonify({"response": response})

if __name__ == "__main__":
    app.run(debug=True)