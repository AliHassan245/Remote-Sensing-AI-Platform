import ollama
import os


def ask_image(image_path: str, question: str):

    print("Image:", image_path)
    print("Exists:", os.path.exists(image_path))
    print("Question:", question)

    prompt = f"""
You are an AI assistant for remote sensing image analysis.

Analyze the uploaded image carefully.

Rules:
- Answer ONLY the user's question.
- Be concise and accurate.
- Do NOT explain your reasoning.
- Do NOT think step by step.
- Do NOT include internal thoughts.
- If asked to list objects, use bullet points.
- If you are uncertain, say so instead of guessing.

Question:
{question}
"""

    try:

        response = ollama.chat(
            model="qwen3-vl:8b",
            messages=[
                {
                    "role": "user",
                    "content": prompt,
                    "images": [image_path]
                }
            ]
        )

        print("\n========== OLLAMA RESPONSE ==========")
        print(response)
        print("=====================================\n")

        answer = response.message.content.strip()

        # Sometimes Qwen3-VL reaches the token limit and
        # returns an empty content field.
        if answer == "":

            print("Empty response received. Retrying...")

            retry_response = ollama.chat(
                model="qwen3-vl:8b",
                messages=[
                    {
                        "role": "user",
                        "content": f"""
Give ONLY the final answer.

No reasoning.
No thinking.
No explanation.

Question:
{question}
""",
                        "images": [image_path]
                    }
                ]
            )

            answer = retry_response.message.content.strip()

        if answer == "":

            answer = (
                "The model could not generate a final answer. "
                "Please try asking a shorter or simpler question."
            )

        return answer

    except Exception as e:

        print("VLM Error:", str(e))

        return f"Error: {str(e)}"