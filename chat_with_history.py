from openai import OpenAI

from openai_client import load_api_key


class ChatWithHistory:
    def __init__(
        self,
        api_key: str,
        model: str = "gpt-4o",
        temperature: float = 0.2,
        max_tokens: int = 1024,
    ) -> None:
        self.client = OpenAI(api_key=api_key)
        self.model = model
        self.temperature = temperature
        self.max_tokens = max_tokens
        self.history: list[dict[str, str]] = []

    def clear(self) -> None:
        self.history = []
        print("Chat history cleared.")

    def chat(self, user_input: str) -> str:
        if not self.history:
            self.history.append(
                {
                    "role": "system",
                    "content": "You are a helpful assistant that can answer simple questions. Your answers should be concise and to the point.",
                }
            )

        print("User:", user_input)
        self.history.append({"role": "user", "content": user_input})

        try:
            message_return = self.client.chat.completions.create(
                model=self.model,
                temperature=self.temperature,
                max_tokens=self.max_tokens,
                messages=self.history,
            )
        except Exception as error:
            print(f"Error: {error}")
            return ""

        response = message_return.choices[0].message.content or ""
        print("Assistant:", response)
        self.history.append({"role": "assistant", "content": response})
        return response


def run_chat() -> None:
    chatbot = ChatWithHistory(load_api_key())
    quit_commands = {"quit", "exit", "bye", "stop"}

    while True:
        user_input = input("Enter whatever you want: ")
        command = user_input.lower()

        if command in quit_commands:
            break

        if command == "clear":
            chatbot.clear()
        else:
            chatbot.chat(user_input)


if __name__ == "__main__":
    run_chat()
