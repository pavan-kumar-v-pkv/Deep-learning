# Smart Office Assistant

Welcome to the **Smart Office Assistant** project! This is an AI-powered tool that can automatically draft professional email replies based on user inputs and specified tone preferences.

## Project Overview

The Smart Office Assistant helps streamline email communication by generating contextually appropriate responses. Simply provide the original email, key bullet points you want to address, choose your preferred tone, and the AI will draft a professional reply for you.

## Project Structure

This project is organized into two main parts:

### Part 1: Prompt Construction ✅
- **Completed**: Input collection and prompt formatting
- Collects original email text from user
- Gathers bullet points for key response elements
- Allows tone selection (formal, friendly, concise, detailed)
- Constructs structured prompts for the AI model

### Part 2: AI-Powered Reply Generation ✅
- **Completed**: Integration with Groq LLM API
- Sends constructed prompts to AI model
- Generates professional email replies
- Returns formatted responses

## Features

- **Interactive Input Collection**: Easy-to-use prompts for gathering email content and preferences
- **Flexible Tone Selection**: Choose from 4 different response tones:
  - Formal
  - Friendly
  - Concise
  - Detailed
- **AI-Powered Generation**: Uses Groq's Llama-3.3-70b-versatile model for high-quality responses
- **Error Handling**: Graceful handling of API errors and invalid inputs

## Prerequisites

Before running the Smart Office Assistant, ensure you have:

1. **Python 3.7+** installed on your system
2. **Groq API Key** - Sign up at [Groq Console](https://console.groq.com/) to get your API key

## Installation

1. **Clone or download** the project files
2. **Install required dependencies**:
   ```bash
   pip install groq python-dotenv
   ```

## Setup

1. **Configure your API key**:
   - Open the `.env` file in the project directory
   - Replace the placeholder with your actual Groq API key:
     ```
     GROQ_API_KEY="your_actual_api_key_here"
     ```

2. **Verify the project structure**:
   ```
   smart office assistant/
   ├── main.py
   ├── .env
   └── README.md
   ```

## Usage

1. **Run the application**:
   ```bash
   python main.py
   ```

2. **Follow the interactive prompts**:
   - **Step 1**: Paste the original email text you want to reply to
   - **Step 2**: Enter key bullet points (comma-separated) you want to include in the response
   - **Step 3**: Choose your preferred tone (1-4)

3. **Review the generated reply**:
   - The application will display the constructed prompt for debugging
   - The AI-generated email reply will be shown
   - Copy and customize the reply as needed

## Example Usage

```
Paste the incoming email text:
Hello, I'm interested in your product pricing and would like to schedule a demo.

Enter the bullet points in comma-separated:
thank customer, provide pricing info, schedule demo call

Choose the tone of the reply:
1. Formal
2. Friendly
3. Concise
4. Detailed
Enter your choice (1-4): 2

Generated Prompt:
Draft a professional email reply in a friendly tone based on the following.
Original email: 'Hello, I'm interested in your product pricing and would like to schedule a demo.'
Key points to include: ['thank customer', 'provide pricing info', 'schedule demo call']
Reply:

Drafted Reply:
Thank you for your interest in our product! I'd be happy to provide you with pricing information and schedule a demo call...
```

## Configuration

### Environment Variables

The application uses environment variables stored in the `.env` file:

- `GROQ_API_KEY`: Your Groq API key for accessing the AI model

### Model Settings

The current configuration uses:
- **Model**: `llama-3.3-70b-versatile`
- **Temperature**: `0.3` (for consistent, professional responses)
- **Max Tokens**: `512` (sufficient for email replies)

## File Structure

- **`main.py`**: Main application file containing all core functionality
- **`.env`**: Environment configuration file (keep secure!)
- **`README.md`**: Project documentation (this file)

## Functions Overview

### Input Collection Functions
- `get_email_text()`: Collects the original email text
- `get_bullet_points()`: Collects and processes key points
- `choose_tone()`: Handles tone selection with validation

### Core Processing Functions
- `build_prompt()`: Constructs the formatted prompt for the AI
- `generate_reply()`: Sends prompt to Groq API and returns the response

## Error Handling

The application includes error handling for:
- Invalid tone selections (defaults to "formal")
- API connection issues
- Empty or malformed inputs

## Security Notes

- **Never commit your `.env` file** with real API keys to version control
- Keep your API key secure and don't share it publicly
- Consider using separate API keys for development and production

## Troubleshooting

### Common Issues

1. **"No module named 'groq'" error**:
   ```bash
   pip install groq python-dotenv
   ```

2. **API key errors**:
   - Verify your API key is correctly set in the `.env` file
   - Ensure your Groq account has API access
   - Check for any extra spaces or quotes around the API key

3. **Empty responses**:
   - Check your internet connection
   - Verify the Groq API service status
   - Ensure you have sufficient API credits

## Future Enhancements

Potential improvements for future versions:
- Email template management
- Multiple AI model support
- Response customization options
- Email history and learning
- Integration with email clients

## Contributing

This is a learning project. Feel free to experiment with:
- Different AI models
- Additional tone options
- Enhanced prompt engineering
- UI improvements

## License

This project is for educational purposes. Please respect the terms of service for the Groq API when using this tool.

---

**Happy emailing!** 📧✨