from flask import Flask, request

app = Flask(__name__)


@app.route("/")
def home():

    return """
    <html>

    <head>
        <title>AI Chatbot</title>
    </head>

    <body>

        <h1>AI Chatbot Testing App</h1>

        <form action="/chat" method="post">

            <input
                type="text"
                name="prompt"
                placeholder="Ask something"
                style="width:300px;height:40px;"
            >

            <button type="submit">
                Send
            </button>

        </form>

    </body>

    </html>
    """


@app.route("/chat", methods=["POST"])
def chat():

    prompt = request.form["prompt"]

    response = f"AI Response: {prompt}"

    return f"""
    <html>

    <body>

        <h2>{response}</h2>

        <a href="/">Go Back</a>

    </body>

    </html>
    """


@app.route("/api/chat", methods=["POST"])
def api_chat():

    data = request.json

    prompt = data.get("prompt")

    return {
        "response": f"AI Response: {prompt}"
    }


if __name__ == "__main__":

    app.run(debug=True)