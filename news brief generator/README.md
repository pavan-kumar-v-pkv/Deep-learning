# News Brief Generator 🚀

A powerful AI-driven tool that automatically generates different styles of summaries from long text documents such as news articles, blogs, or reports using Groq's LLM API.

![Python](https://img.shields.io/badge/Python-3.7+-blue.svg)
![Groq](https://img.shields.io/badge/Groq-LLM%20API-green.svg)
![License](https://img.shields.io/badge/License-MIT-yellow.svg)

## 🎯 Project Overview

The News Brief Generator is a text summarization tool that creates three distinct summary styles:

- **🎯 Bullet-point style** → Key points in short, concise bullets
- **📝 Abstract style** → A formal, research-paper-like abstract of the text  
- **👶 Simple English style** → A simplified explanation, suitable for a 12-year-old reader

The tool also includes an intelligent comparison system that determines the best summary based on keyword overlap analysis.

## ✨ Features

- **Multi-Style Summarization**: Generate three different summary formats from a single input
- **Intelligent Summary Selection**: Automatically chooses the best summary using keyword overlap scoring
- **Keyword Extraction**: Advanced text processing to identify key terms and concepts
- **Environment Variable Support**: Secure API key management through `.env` files
- **Customizable Parameters**: Adjustable number of bullet points, sentences, and summary length

## 🛠️ Technology Stack

- **Python 3.7+**: Core programming language
- **Groq API**: LLM service using `llama-3.1-8b-instant` model
- **python-dotenv**: Environment variable management
- **Regular Expressions**: Text processing and keyword extraction

## 📦 Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/pavan-kumar-v-pkv/Deep-learning.git
   cd Deep-learning/news\ brief\ generator/
   ```

2. **Install required packages**:
   ```bash
   pip install groq python-dotenv
   ```

3. **Set up environment variables**:
   Create a `.env` file in the project directory:
   ```env
   GROQ_API_KEY=your_groq_api_key_here
   ```

4. **Prepare your content**:
   Add your text content to `article.txt` file in the project directory.

## 🚀 Usage

### Basic Usage

```bash
python main.py
```

The program will:
1. Read your API key from the `.env` file (or prompt for input if not found)
2. Load content from `article.txt`
3. Generate all three summary styles
4. Display each summary type
5. Analyze and recommend the best summary based on keyword overlap

### Example Output

```
--- Bullet-point Summary ---
• Major breakthrough in renewable energy technology announced
• Solar panel efficiency increased by 40% through new materials
• Cost reduction expected to make solar power more accessible
• Implementation planned across multiple countries by 2025
• Environmental impact could reduce carbon emissions significantly

--- Abstract Summary ---
This article discusses a significant advancement in renewable energy technology, 
specifically focusing on improved solar panel efficiency. The breakthrough involves 
innovative materials that enhance energy conversion rates while reducing manufacturing 
costs. The development promises widespread implementation and substantial environmental 
benefits through reduced carbon emissions. Industry experts anticipate major market 
disruption and increased adoption of solar energy solutions globally.

--- Simple English Summary ---
Scientists have made solar panels much better at collecting sunlight and turning it 
into electricity. These new solar panels work 40% better than old ones and cost less 
money to make. This means more people can use clean energy from the sun. Many countries 
plan to start using these better solar panels by 2025. This will help protect our 
planet by making less pollution.

Keyword overlap score for Bullet Points: 0.1234
Keyword overlap score for Abstract: 0.1456
Keyword overlap score for Simple English: 0.1123

Best Summary (by keywords: Abstract):
This article discusses a significant advancement in renewable energy technology...
```

## 🔧 Configuration

### Summary Parameters

You can customize the output by modifying parameters in the main function:

```python
# Adjust number of bullet points (default: 5)
bullet_summary = bullet_point_summary(client, content, num_points=7)

# Adjust number of sentences in abstract (default: 5)
abstract_summary = abstract_style_summary(client, content, sentence_count=3)

# Adjust number of sentences in simple summary (default: 5)
simple_summary = simple_english_summary(client, content, sentence_count=4)
```

### Model Settings

The tool uses the following Groq API configuration:
- **Model**: `llama-3.1-8b-instant`
- **Temperature**: `0.3` (for consistent, focused outputs)
- **Max Completion Tokens**: `300`

## 📁 Project Structure

```
news brief generator/
├── main.py              # Main application script
├── article.txt          # Input text file
├── .env                 # Environment variables (not in repo)
├── README.md           # Project documentation
└── requirements.txt    # Python dependencies (optional)
```

## 🧪 How It Works

### Part 1: Multi-Style Summarization

1. **Bullet Point Summary**: Uses a concise summarizer persona to extract key points
2. **Abstract Summary**: Employs academic writing style for formal summaries
3. **Simple English Summary**: Utilizes a teacher persona to explain complex topics simply

### Part 2: Best Summary Selection

The system uses keyword overlap analysis to determine the most representative summary:

```python
score = overlap_count / (total_article_keywords + 1)
```

The summary with the highest keyword overlap score is selected as the best representation.

## 🔒 Security

- API keys are stored securely in `.env` files
- Environment variables are loaded using `python-dotenv`
- No hardcoded credentials in the source code

## 🤝 Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📋 Requirements

Create a `requirements.txt` file:
```
groq>=0.4.0
python-dotenv>=0.19.0
```

## 🐛 Troubleshooting

### Common Issues

1. **API Key Error**: Ensure your `GROQ_API_KEY` is correctly set in the `.env` file
2. **File Not Found**: Make sure `article.txt` exists in the project directory
3. **Import Error**: Install required packages using `pip install groq python-dotenv`

### Getting Groq API Key

1. Visit [Groq Console](https://console.groq.com/)
2. Sign up for an account
3. Navigate to API Keys section
4. Generate a new API key
5. Add it to your `.env` file

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- **Groq** for providing the LLM API
- **Llama 3.1** model for high-quality text generation
- **Python community** for excellent libraries and tools

## 📞 Contact

**Pavan Kumar V**
- GitHub: [@pavan-kumar-v-pkv](https://github.com/pavan-kumar-v-pkv)
- Repository: [Deep-learning](https://github.com/pavan-kumar-v-pkv/Deep-learning)

---

⭐ If you found this project helpful, please give it a star!