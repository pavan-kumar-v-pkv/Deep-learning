# Study Assistant

Welcome to the **Study Assistant** project! This is an AI-powered tool designed to help students answer their study-related questions by intelligently processing and retrieving relevant information from large documents.

## Project Overview

The Study Assistant helps students quickly find answers from extensive study materials such as textbooks, research articles, and lecture notes. Instead of manually searching through long documents, the assistant breaks down the content into manageable chunks and retrieves the most relevant context for your specific questions.

This is particularly useful when dealing with:
- Long textbooks or course materials
- Research papers and academic articles
- Lecture notes and study guides
- Reference documents

## How It Works

The Study Assistant uses a sophisticated approach called **Retrieval-Augmented Generation (RAG)**:

1. **Document Processing**: Breaks down your study material into smaller, overlapping chunks
2. **Context Retrieval**: Finds the most relevant chunks based on your question keywords
3. **Answer Generation**: Uses AI to provide accurate, contextual answers based on the retrieved information

## Project Structure

This project is organized into two main parts:

### Part 1: Document Processing and Context Retrieval ✅
- **Document Loading**: Reads and processes text files
- **Text Chunking**: Intelligently splits documents into manageable pieces with overlap
- **Context Matching**: Scores and retrieves the most relevant chunks for your question
- **Keyword Analysis**: Uses sophisticated matching algorithms to find relevant content

### Part 2: Answer Generation with LLM ✅
- **AI Integration**: Uses Groq's Llama-3.3-70b-versatile model for answer generation
- **Prompt Engineering**: Constructs optimized prompts with context and questions
- **Response Generation**: Provides accurate, contextual answers based on your study materials

## Features

- **Intelligent Document Processing**: Automatically chunks large documents with smart overlap
- **Advanced Context Retrieval**: Uses keyword matching to find the most relevant information
- **AI-Powered Answers**: Generates accurate responses using state-of-the-art language models
- **Easy File Integration**: Simply place your study materials as `document.txt`
- **Interactive Interface**: User-friendly command-line interface for asking questions

## Prerequisites

Before using the Study Assistant, ensure you have:

1. **Python 3.7+** installed on your system
2. **Groq API Key** - Sign up at [Groq Console](https://console.groq.com/) to get your API key
3. **Study Materials** - A text file containing your study content

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

2. **Prepare your study material**:
   - Create a file named `document.txt` in the project directory
   - Copy and paste your study content (textbook chapters, notes, etc.) into this file

3. **Verify the project structure**:
   ```
   study assistant/
   ├── main.py
   ├── .env
   ├── document.txt
   └── README.md
   ```

## Usage

1. **Prepare your study material**:
   - Ensure your `document.txt` file contains the content you want to query
   - The file can contain multiple chapters, sections, or topics

2. **Run the Study Assistant**:
   ```bash
   python main.py
   ```

3. **Ask your questions**:
   - The system will automatically process your document
   - Enter your study-related question when prompted
   - Receive AI-generated answers based on your material

## Example Usage

```
Loading document...
Splitting into chunks...
Enter your question: What are the main principles of machine learning?

Answer:
Based on your study material, the main principles of machine learning include:
1. Data-driven learning from examples
2. Pattern recognition and generalization
3. Model training and validation
4. Feature extraction and selection...
```

## Configuration

### Environment Variables
- `GROQ_API_KEY`: Your Groq API key for accessing the AI model

### Processing Parameters
- **Chunk Size**: 300 words per chunk (optimized for context retrieval)
- **Overlap**: 50 words overlap between chunks (prevents information loss)
- **Model**: `llama-3.3-70b-versatile` (high-quality responses)
- **Temperature**: 0.3 (balanced creativity and accuracy)

## File Structure

- **`main.py`**: Core application with all processing and AI functionality
- **`.env`**: Environment configuration file (keep secure!)
- **`document.txt`**: Your study material (create this file with your content)
- **`README.md`**: Project documentation (this file)

## Functions Overview

### Document Processing Functions
- `load_document()`: Reads and validates text files
- `chunk_text()`: Intelligently splits documents into overlapping chunks
- `score_chunk()`: Calculates relevance scores based on keyword matching
- `get_best_chunk()`: Retrieves the most relevant context for questions

### AI Integration Functions
- `build_prompt()`: Constructs optimized prompts for the AI model
- `get_answer_from_groq()`: Interfaces with Groq API for answer generation

## Advanced Features

### Smart Chunking Algorithm
The assistant uses an intelligent chunking strategy:
- **Optimal Size**: 300-word chunks provide good context without overwhelming the AI
- **Smart Overlap**: 50-word overlap ensures important information isn't split
- **Context Preservation**: Maintains coherent meaning across chunk boundaries

### Keyword-Based Retrieval
- Converts questions and chunks to lowercase for better matching
- Uses set intersection for efficient keyword overlap calculation
- Scores chunks based on relevance to your specific question

## Tips for Best Results

1. **Quality Input**: Use well-formatted, clear study materials
2. **Specific Questions**: Ask focused questions for more accurate answers
3. **Document Structure**: Organize your `document.txt` with clear sections and topics
4. **Question Variety**: Try different phrasings if you don't get the expected answer

## Troubleshooting

### Common Issues

1. **"File 'document.txt' not found" error**:
   - Create a `document.txt` file in the project directory
   - Add your study content to this file

2. **"No module named 'groq'" error**:
   ```bash
   pip install groq python-dotenv
   ```

3. **API key errors**:
   - Verify your API key is correctly set in the `.env` file
   - Ensure your Groq account has API access
   - Check for extra spaces or quotes around the API key

4. **Poor answer quality**:
   - Ensure your `document.txt` contains relevant information
   - Try rephrasing your question with different keywords
   - Check that your study material is well-formatted

## Study Tips

### Optimizing Your Study Material
- **Clear Formatting**: Use headers, bullet points, and clear sections
- **Comprehensive Content**: Include definitions, examples, and explanations
- **Logical Organization**: Structure content from basic to advanced concepts
- **Key Terms**: Include important terminology and concepts

### Effective Questioning
- **Be Specific**: "What is photosynthesis?" vs "Tell me about biology"
- **Use Keywords**: Include important terms from your study material
- **Ask Follow-ups**: Build on previous answers for deeper understanding
- **Context Matters**: Reference specific topics or chapters when relevant

## Future Enhancements

Potential improvements for future versions:
- Multiple document support
- PDF and Word document processing
- Advanced search algorithms
- Question history and bookmarking
- Study progress tracking
- Interactive study sessions

## Educational Benefits

This tool helps students:
- **Save Time**: Quickly find relevant information in large texts
- **Improve Understanding**: Get contextual explanations of complex topics
- **Study Efficiently**: Focus on specific questions rather than reading everything
- **Review Effectively**: Quickly revisit key concepts and definitions

## Security Notes

- **Keep API keys secure** - Never share your `.env` file publicly
- **Use separate keys** for development and production if needed
- **Monitor API usage** to avoid unexpected charges

## Contributing

This is an educational project perfect for learning about:
- Document processing and text chunking
- Information retrieval systems
- AI integration and prompt engineering
- Natural language processing concepts

## License

This project is for educational purposes. Please respect the terms of service for the Groq API and any study materials you use.

---

**Happy studying!** 📚🤖✨