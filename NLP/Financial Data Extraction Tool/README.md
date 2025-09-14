# Financial Data Extraction Tool

A Streamlit-based web application that uses OpenAI's GPT-3.5-turbo model to extract key financial information from text articles or financial documents.

## Features

- Extract financial metrics from text including:
  - Company Name
  - Stock Symbol
  - Revenue
  - Net Income
  - Total Assets
  - EBITDA
  - Stock Price
  - Earnings per Share (EPS)
- Clean, interactive web interface built with Streamlit
- Powered by OpenAI's GPT-3.5-turbo for accurate information extraction
- Returns structured data in a pandas DataFrame format

## Installation

1. Clone the repository:
```bash
git clone https://github.com/pavan-kumar-v-pkv/Deep-learning.git
cd "NLP/Financial Data Extraction Tool"
```

2. Create and activate a virtual environment:
```bash
python -m venv env
source env/bin/activate  # On Windows: env\Scripts\activate
```

3. Install required packages:
```bash
pip install streamlit openai python-dotenv pandas
```

## Configuration

1. Create a `.env` file in the project directory:
```bash
touch .env
```

2. Add your OpenAI API key to the `.env` file:
```
OPENAI_API_KEY=your_openai_api_key_here
```

To get an OpenAI API key:
- Visit [OpenAI API](https://platform.openai.com/api-keys)
- Create an account and generate an API key
- Make sure you have credits in your OpenAI account

## Usage

1. Run the Streamlit application:
```bash
streamlit run app.py
```

2. Open your web browser and go to `http://localhost:8501`

3. Enter or paste financial text/article in the text area

4. Click "Extract" to process the text and extract financial information

5. View the extracted data in the results table

## Example Input

```
Apple Inc. reported a revenue of $365.8 billion for the fiscal year 2021, with a net income of $94.7 billion. The company's total assets stood at $351 billion, and its EBITDA was $112.4 billion. As of December 31, 2021, Apple's stock price was $177.57, and its earnings per share (EPS) were $5.61.
```

## Example Output

| Measure | Value |
|---------|-------|
| Company Name | Apple Inc. |
| Stock Symbol | AAPL |
| Revenue | $365.8 billion |
| Net Income | $94.7 billion |
| Total Assets | $351 billion |
| EBITDA | $112.4 billion |
| Stock Price | $177.57 |
| EPS | $5.61 |

## Project Structure

```
Financial Data Extraction Tool/
├── app.py              # Main Streamlit application
├── helper.py           # OpenAI integration and data processing
├── .env               # Environment variables (not tracked in git)
└── README.md          # Project documentation
```

## Files Description

- **app.py**: Main Streamlit application file that creates the user interface
- **helper.py**: Contains the OpenAI API integration and financial data extraction logic
- **.env**: Environment file for storing sensitive API keys (should be created by user)

## Technologies Used

- **Streamlit**: Web application framework
- **OpenAI GPT-3.5-turbo**: Natural language processing for information extraction
- **Pandas**: Data manipulation and analysis
- **Python-dotenv**: Environment variable management

## Error Handling

The application includes error handling for:
- Invalid JSON responses from OpenAI
- Missing financial information in text
- API connection issues

If information cannot be extracted, the tool returns "Not Found" for missing fields.

## Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## License

This project is part of a Deep Learning repository. Please refer to the main repository for license information.

## Acknowledgments

- OpenAI for providing the GPT-3.5-turbo API
- Streamlit team for the excellent web framework
- Financial data extraction concept for educational purposes

## Troubleshooting

### Common Issues

1. **ModuleNotFoundError**: Make sure all packages are installed in your virtual environment
2. **OpenAI API Error**: Check your API key and ensure you have credits in your OpenAI account
3. **Streamlit not starting**: Ensure you're running the command from the correct directory

### Getting Help

If you encounter issues:
1. Check that your `.env` file contains the correct API key
2. Verify all dependencies are installed
3. Ensure you're using the correct Python environment
4. Check the terminal output for specific error messages