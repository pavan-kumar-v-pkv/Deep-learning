from groq import Groq
import re
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

def bullet_point_summary(client, text, num_points=5):
    """
    Summarize text into concise bullet points.

    Args:
        client (Groq): Groq client initialized with API key.
        text (str): Input text to summarize.
        num_points (int): Number of bullet points for the summary.

    Returns:
        str: Generated bullet-point style summary.
    """
    # Build prompt
    prompt = f"Summarize the following text in {num_points} concise bullet points:\n\n{text}"

    # TODO: Call Groq API with model = "llama-3.1-8b-instant"
    # Use temperature = 0.3 and max_completion_tokens = 300
    # Messages:
    # - system message: "You are a concise and clear summarizer."
    # - user message: Should contain the prompt

    # TODO: Parse and return the response text
    system_message = {"role":"system", "content":"You are a concise and clear summarizer."}
    user_message = {"role": "user", "content":prompt}

    reponse = client.chat.completions.create(
        model = "llama-3.1-8b-instant",
        messages = [system_message, user_message],
        temperature = 0.3,
        max_completion_tokens = 300,
    )
    return reponse.choices[0].message.content.strip()


def abstract_style_summary(client, text, sentence_count=5):
    """
    Summarize text in an academic abstract style.

    Args:
        client (Groq): Groq client initialized with API key.
        text (str): Input text to summarize.
        sentence_count (int): Number of sentences in the abstract.

    Returns:
        str: Generated abstract-style summary.
    """
    # Build prompt
    prompt = f"Summarize the following text as a {sentence_count}-sentence abstract:\n\n{text}"

    # TODO: Call Groq API with model = "llama-3.1-8b-instant"
    # Use temperature = 0.3 and max_completion_tokens = 300
    # Messages:
    # - system message: "You are a concise and clear summarizer."
    # - user message: Should contain the prompt

    # TODO: Parse and return the response text
    system_message = {"role":"system", "content":"You are a concise and clear summarizer."}
    user_message = {"role": "user", "content":prompt}

    reponse = client.chat.completions.create(
        model = "llama-3.1-8b-instant",
        messages = [system_message, user_message],
        temperature = 0.3,
        max_completion_tokens = 300,
    )
    return reponse.choices[0].message.content.strip()


def simple_english_summary(client, text, sentence_count=5):
    """
    Summarize text in simple English for a younger audience.

    Args:
        client (Groq): Groq client initialized with API key.
        text (str): Input text to summarize.
        sentence_count (int): Number of sentences in the summary.

    Returns:
        str: Generated simple-English style summary.
    """
    # Build prompt
    prompt = (
        f"Summarize the following text in simple English suitable for a 12-year-old, "
        f"in {sentence_count} sentences:\n\n{text}"
    )

    # TODO: Call Groq API with model = "llama-3.1-8b-instant"
    # Use temperature = 0.3 and max_completion_tokens = 300
    # Messages:
    # - system message: "You are a kind teacher explaining things simply."
    # - user message: Should contain the prompt

    # TODO: Parse and return the response text
    system_message = {"role":"system", "content":"You are a kind teacher explaining things simply."}
    user_message = {"role": "user", "content":prompt}

    reponse = client.chat.completions.create(
        model = "llama-3.1-8b-instant",
        messages = [system_message, user_message],
        temperature = 0.3,
        max_completion_tokens = 300,
    )
    return reponse.choices[0].message.content.strip()


# Keyword extractor function
def extract_keywords(text):
    """
    Extract keywords from the given text.

    Args:
        text (str): Input text.

    Returns:
        set: Set of extracted keywords.
    """

    # TODO: Split text into words
    # TODO: Convert words to lowercase
    # TODO: Strip punctuation (.,!?) at the start or end of words.
    # TODO: Ignore words with length <= 4
    # TODO: Collect results into a set and return
    words = text.lower().split()
    clean_words = set()
    for w in words:
        w = re.sub(r"^[.,!?]+|[.,!?]+$", "", w)
        if len(w) > 4:
            clean_words.add(w)
    return clean_words


# Choose best summary (Keyword Overlap)
def best_summary_by_keywords(article, summaries) -> str:
    """
    Choose the best summary by measuring keyword overlap with the article.

    Steps:
    - Extract keywords from the article.
    - For each summary:
        * Extract keywords.
        * Compute overlap score using the formula:

          score = overlap_count / (total_article_keywords + 1)

        * Print the score for each summary in the format:
          print(f"Keyword overlap score for {label}: {score:.4f}")

    - Track the summary with the highest score:
        if score > best_score:
            best_label, best_summary, best_score = label, summary, score
    - Return the best summary label and content.

    Args:
        article (str): The original article text.
        summaries (dict): Dictionary of summaries with labels as keys.

    Returns:
        str: The best summary (label + text).
    """
    # TODO: Extract keywords from article
    article_keywords = extract_keywords(article)
    # TODO: Iterate over summaries
    #    - Extract keywords for each summary
    #    - Compute overlap with article keywords
    #    - Calculate score using formula
    #    - Print score in required format
    #    - Update best summary if score is higher
    best_label, best_summary, best_score = None, None, -1

    for label, summary in summaries.items():
        summary_keywords = extract_keywords(summary)
        overlap = article_keywords & summary_keywords
        score = len(overlap) / (len(article_keywords) + 1)
        print(f"Keyword overlap score for {label}: {score:.4f}")
        if score > best_score:
            best_label, best_summary, best_score = label, summary, score
    # TODO: Return the best summary with label and text like:
    #       f"Best Summary (by keywords: {best_label}):\n{best_summary}"

    return f"Best Summary (by keywords: {best_label}):\n{best_summary}"

if __name__ == "__main__":
    # Get API key from environment variable
    api_key = os.getenv("GROQ_API_KEY")
    if not api_key:
        api_key = input("Enter your Groq API key: ").strip()
    
    client = Groq(api_key=api_key)

    filepath = "article.txt"
    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()

    bullet_summary = bullet_point_summary(client, content, num_points=5)
    abstract_summary = abstract_style_summary(client, content, sentence_count=5)
    simple_summary = simple_english_summary(client, content, sentence_count=5)

    print("\n--- Bullet-point Summary ---\n", bullet_summary)
    print("\n--- Abstract Summary ---\n", abstract_summary)
    print("\n--- Simple English Summary ---\n", simple_summary)

    summaries = {
        "Bullet Points": bullet_summary,
        "Abstract": abstract_summary,
        "Simple English": simple_summary,
    }

    final_summary = best_summary_by_keywords(content, summaries)
    print("\nFinal Chosen Summary:\n", final_summary)
