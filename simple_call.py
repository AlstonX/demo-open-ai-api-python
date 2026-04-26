from openai_client import create_client


def ask_nyc_24_hours() -> str:
    client = create_client()
    response = client.chat.completions.create(
        model="gpt-4o",
        temperature=0.2,
        max_tokens=1024,
        messages=[
            {
                "role": "system",
                "content": "You are a helpful assistant that can answer my simple questions. Your answer should be concise and to the point.",
            },
            {
                "role": "user",
                "content": "What places I can visit in New York City if I only have 24 hours to spend there?",
            },
        ],
    )
    return response.choices[0].message.content or ""


if __name__ == "__main__":
    print(ask_nyc_24_hours())
