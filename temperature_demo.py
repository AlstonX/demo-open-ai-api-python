from openai import OpenAI

from openai_client import create_client


def get_response(client: OpenAI, temperature: float) -> str:
    response = client.chat.completions.create(
        model="gpt-4o",
        temperature=temperature,
        max_tokens=1024,
        messages=[
            {
                "role": "system",
                "content": "You are a helpful assistant that can answer my simple questions. Your answers should be concise and to the point.",
            },
            {
                "role": "user",
                "content": "What places I can visit in Jersey City if I only have 24 hours to spend there?",
            },
        ],
    )
    return response.choices[0].message.content or ""


def run_temperature_demo() -> None:
    client = create_client()
    temperatures = [0.2, 0.5, 0.8]

    for temperature in temperatures:
        print("temperature:", temperature)
        print(get_response(client, temperature))
        print()


if __name__ == "__main__":
    run_temperature_demo()
