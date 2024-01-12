import openai

# Replace 'your-api-key' with your actual OpenAI GPT-3 API key
openai.api_key = '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'

def generate_image(prompt):
    try:
        response = openai.Completion.create(
            engine="code-davinci-002",  # You might need to adjust the engine based on the latest available options
            prompt=prompt,
            max_tokens=150
        )

        generated_image = response.choices[0].text.strip()
        print(f"Generated Image: {generated_image}")

    except Exception as e:
        print(f"Error: {e}")

# Example usage
prompt_text = "A surreal landscape with floating islands"
generate_image(prompt_text)
