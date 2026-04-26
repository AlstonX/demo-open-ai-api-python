from __future__ import annotations

from flask import Flask, jsonify, render_template, request

from chat_with_history import ChatWithHistory
from openai_client import load_api_key


app = Flask(__name__)

chatbot = ChatWithHistory(load_api_key())


def visible_history() -> list[dict[str, str]]:
    return [message for message in chatbot.history if message["role"] != "system"]


@app.get("/")
def index() -> str:
    return render_template("index.html")


@app.get("/api/history")
def history() -> tuple[object, int]:
    return jsonify({"history": visible_history()}), 200


@app.post("/api/chat")
def chat() -> tuple[object, int]:
    payload = request.get_json(silent=True) or {}
    message = str(payload.get("message", "")).strip()

    if not message:
        return jsonify({"error": "Message cannot be empty."}), 400

    response = chatbot.chat(message)
    if not response:
        return jsonify({"error": "The assistant did not return a response."}), 502

    return jsonify({"response": response, "history": visible_history()}), 200


@app.post("/api/clear")
def clear() -> tuple[object, int]:
    chatbot.clear()
    return jsonify({"history": []}), 200


if __name__ == "__main__":
    app.run(debug=True)
