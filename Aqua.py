from flask import Flask, render_template, request, jsonify
import openai

app = Flask(__name__)

openai.api_key = "api key"

def generate_response(prompt):
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=150
    )
    return response['choices'][0]['text']

@app.route("/")
def index():
    return render_template("chatbot.html")

@app.route("/generate_response", methods=["POST"])
def generate_response_route():
    data = request.get_json()
    user_input = data["prompt"]

    bot_response = generate_response(user_input)

    return jsonify({"bot_response": bot_response})

if __name__ == "__main__":
    app.run(debug=True)
