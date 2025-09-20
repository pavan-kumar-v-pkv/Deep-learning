import os
from dotenv import load_dotenv
from groq import Groq

# Load environment variables from .env file
load_dotenv()

def get_email_text():
    """
    Prompt the user to enter the incoming email text.

    TODO:
    1. Use input() to ask the user:
       "Paste the incoming email text:"
    2. Store the input in a variable.
    3. Return it as a string.

    """

    # TODO: return the entered email text
    email = input("Paste the incoming email text:\n")
    return email.strip()


def get_bullet_points():
    """
    Prompt the user to enter bullet points (comma-separated).

    TODO:
    1. Ask the user:
       "Enter bullet points (comma-separated):"
    2. Split the input string by commas → input.split(',')
    3. Strip whitespace from each bullet point.
    4. Filter out any empty points.
    5. Return the cleaned bullet points as a list.

    Example:
    Input:  "thank customer, provide pricing, send brochure"
    Output: ["thank customer", "provide pricing", "send brochure"]
    """

    # TODO: return a list of cleaned bullet points
    bullet_points_input = input("Enter the bullet points in comma-separated:\n")
    bullet_points = [point.strip() for point in bullet_points_input.split(",") if point.strip()]
    return bullet_points


def choose_tone():
    """
    Prompt the user to choose a tone for the email reply.

    TODO:
    1. Print the following options:
         1. Formal
         2. Friendly
         3. Concise
         4. Detailed
    2. Ask the user: "Enter your choice (1-4):"
    3. Map the choice to a tone string:
         "1" → "formal"
         "2" → "friendly"
         "3" → "concise"
         "4" → "detailed"
    4. If input is invalid, default to "formal".
    5. Return the tone string.
    """

    # TODO: return the selected tone string
    print("Choose the tone of the reply:")
    print("1. Formal")
    print("2. Friendly")
    print("3. Concise")
    print("4. Detailed")
    choice = input("Enter your choice (1-4): ").strip()
    tone_map = {"1": "formal", "2": "friendly", "3": "concise", "4": "detailed"}
    return tone_map.get(choice, "formal")


def build_prompt(email_text, bullet_points, tone):
    """
    Construct the final prompt string using all inputs.

    The prompt must follow this exact format:

    Draft a professional email reply in a {tone} tone based on the following.
    Original email: "{email_text}"
    Key points to include: {bullet_points}
    Reply:

    TODO:
    1. Use an f-string to format the prompt.
    2. Insert {tone}, {email_text}, and {bullet_points}.
    3. Return the formatted prompt string.
    """
    prompt = (
        f"Draft a professional email reply in a {tone} tone based on the following.\n"
        f"Original email: '{email_text}'\n"
        f"Key points to include: {bullet_points}\n"
        f"Reply:"
    )
    # TODO: return the formatted prompt string
    return  prompt


def generate_reply(prompt, api_key):
    """
    Send the prompt to the Groq LLM API and return the reply.

    TODO:
    1. Initialize the Groq client with the API key:

    2. Call the chat completions endpoint: 
    - model="llama-3.3-70b-versatile",
    - messages=[{"role": "user", "content": prompt}],
    - temperature=0.3,
    - max_completion_tokens=512

    3. Extract the reply text:
         completion.choices[0].message.content.strip()
    4. Return the reply.
    """

    # TODO: return the assistant's drafted reply
    client = Groq(api_key=api_key)

    completion = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.3,
        max_completion_tokens=512
    )

    drafted_reply = completion.choices[0].message.content.strip()
    return drafted_reply


if __name__ == "__main__":
    # Get inputs
    email_text = get_email_text()
    bullet_points = get_bullet_points()
    tone = choose_tone()

    # Build the prompt
    prompt = build_prompt(email_text, bullet_points, tone)

    # Helpful for debugging
    print("\nGenerated Prompt:\n", prompt)  

    # Get API key from environment variables
    api_key = os.getenv('GROQ_API_KEY')
    if not api_key:
        print("Error: GROQ_API_KEY not found in environment variables.")
        print("Please set your API key in the .env file.")
        exit(1)

    # Call Groq API
    try:
        reply = generate_reply(prompt, api_key)
        print("\nDrafted Reply:\n", reply)
    except Exception as e:
        print(f"Error: {e}")
