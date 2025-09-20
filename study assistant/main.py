from groq import Groq
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

def load_document(file_path):
    """
    Load text from a file and return its content.

    Args:
        file_path (str): Path to the text file.

    Returns:
        str: Entire file content as a single string.
    """
    # TODO: Open the file and read its content
    if not os.path.exists(file_path):
        print(f"Error: File '{file_path}' not found")
        return ""

    with open(file_path, "r", encoding='utf-8') as f:
        text = f.read().strip()
    return text


def chunk_text(text, chunk_size=300, overlap=50):
    """
    Split the text into chunks of specified size with overlap.

    Args:
        text (str): The full document text.
        chunk_size (int): Maximum number of words per chunk.
        overlap (int): Number of overlapping words between chunks.

    Returns:
        list: List of text chunks (each as a string).
    """
    # TODO: Split text into words
    # TODO: Generate overlapping chunks of size 'chunk_size'
    # TODO: Append each chunk to a list
    words = text.split()
    chunks = []
    start = 0
    while start < len(words):
        end = start + chunk_size
        chunk = words[start:end]
        chunks.append(' '.join(chunk))
        start += chunk_size - overlap
    return chunks


def score_chunk(chunk, keywords):
    """
    Compute a score for a chunk based on overlapping keywords.

    Args:
        chunk (str): A text chunk.
        keywords (set): Set of keywords from the question.

    Returns:
        int: Number of overlapping words.
    """
    # TODO: Convert chunk to lowercase words
    # TODO: Turn into a set and count overlap with keywords
    chunk_words = set(chunk.lower().split())
    return len(chunk_words & keywords)


def get_best_chunk(chunks, question):
    """
    Select the chunk that best matches the question.

    Args:
        chunks (list): List of text chunks.
        question (str): User's input question.

    Returns:
        str: The chunk with the highest keyword overlap.
    """
    # TODO: Break question into lowercase keywords
    # TODO: Score each chunk using score_chunk

    # TODO: Return the chunk with the highest score
    keywords = set(question.lower().split())
    best_score = -1
    best_chunk = ""
    for chunk in chunks:
        score = score_chunk(chunk, keywords)
        if score > best_score:
            best_score = score
            best_chunk = chunk
    return best_chunk


def build_prompt(context, question):
    """
    Format the prompt with context and the question.

    Args:
        context (str): Best-matching text chunk.
        question (str): User's input question.

    Returns:
        str: Prompt string formatted for the LLM.
    """
    # The prompt must look like this:
    # Context:
    # {context}
    #
    # Question: {question}
    # Answer:
    prompt = f"Context:\n{context}\n\nQuestion:{question}\n\nAnswer:"
    # TODO: Return formatted string
    return prompt


def get_answer_from_groq(prompt, api_key):
    """
    Send the prompt to the Groq API and return the model's answer.

    Args:
        prompt (str): The input prompt containing context + question.
        api_key (str): Groq API key provided by the user.

    Returns:
        str: Model-generated answer.
    """
    # TODO: Initialize Groq client

    # TODO: Call chat.completions.create() with:
    #   - model="llama-3.3-70b-versatile"
    #   - messages=[{"role": "user", "content": prompt}]
    #   - temperature=0.3
    #   - max_completion_tokens=512
    client = Groq(api_key=api_key)
    completion = client.chat.completions.create(
      model="llama-3.3-70b-versatile",
      messages=[{"role": "user", "content": prompt}],
      temperature=0.3,
      max_completion_tokens=512
    )
    # TODO: Return the model's response text
    final_reply = completion.choices[0].message.content.strip()
    return final_reply


if __name__ == "__main__":
    print("Loading document...")
    doc_content = load_document("document.txt")

    print("Splitting into chunks...")
    chunks = chunk_text(doc_content)

    # Ask user question
    question = input("Enter your question: ").lower()

    # Find best chunk
    best_chunk = get_best_chunk(chunks, question)

    # Build prompt
    prompt = build_prompt(best_chunk, question)

    # Get API key from environment variables
    api_key = os.getenv('GROQ_API_KEY')
    if not api_key:
        print("Error: GROQ_API_KEY not found in environment variables.")
        print("Please set your API key in the .env file.")
        exit(1)

    # Call Groq API
    try:
        answer = get_answer_from_groq(prompt, api_key)
        print("\nAnswer:")
        print(answer.strip())
    except Exception as e:
        print(f"Error generating answer: {e}")
        print("Please check your API key and internet connection.")