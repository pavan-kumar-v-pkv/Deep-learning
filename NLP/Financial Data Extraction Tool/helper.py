from openai import OpenAI
from dotenv import load_dotenv
import json
import pandas as pd
import os

load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def get_prompt():
    return '''Please retrieve Company Name, Stock Symbol, Revenue, Net Income, Total Assets, EBITDA, Stock Price, earnings per share (EPS) from the given financial text or the news article. If you can't find the information from the text or the news article then return "Not Found". DO NOT MAKE UP ANY INFORMATION.
    For the Stock Symbol, return the ticker symbol of the company. For example, if the company name is "Apple Inc.", then return "AAPL" as the Stock Symbol.
    Always return your response in the below JSON format:
    {
        "Company Name": "Walmart Inc.",
        "Stock Symbol": "WMT",
        "Revenue": "$559.2 billion",
        "Net Income": "$13.7 billion",
        "Total Assets": "$252.5 billion",
        "EBITDA": "$22.5 billion",
        "Stock Price": "$177.57",
        "Earnings per Share (EPS)": "$5.61"
    }
    News Article: 
    =============
'''

def extract_financial_info(text):
    get_prompt_text = get_prompt() + text

    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "user", "content": get_prompt_text}
        ]
    )
    content = response.choices[0].message.content
    print("Response from OpenAI:", content)  # Debugging line to see the raw response
    try:
        json_object = json.loads(content)
        return pd.DataFrame(json_object.items(), columns=["Measure", "Value"])
    except json.JSONDecodeError:
        pass  # Handle the error as needed

    return pd.DataFrame({
        "Measure": ["Company Name", "Stock Symbol", "Revenue", "Net Income", "Total Assets", "EBITDA", "Stock Price", "EPS"],
        "Value": ["Not Found"] * 8
    })




if __name__ == "__main__":
    text = '''
    Apple Inc. reported a revenue of $365.8 billion for the fiscal year 2021, with a net income of $94.7 billion. The company's total assets stood at $351 billion, and its EBITDA was $112.4 billion. As of December 31, 2021, Apple's stock price was $177.57, and its earnings per share (EPS) were $5.61.
    '''
    data = extract_financial_info(text)