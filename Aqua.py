from flask import Flask, render_template, request, jsonify
import gradio as gr
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

iface = gr.Interface(
    fn=generate_response,
    inputs="text",
    outputs="text",
    live=True,
    title="Chatbot with GPT-3",
    description="zinc level in diabetic milletus group"
)

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
