![portfolio-10-large](https://github.com/user-attachments/assets/749e34a6-0035-442e-9c81-9f9d3f587ede)

ExplainToMe.ai 🎓🤖

Welcome to **[ExplainToMe.ai](https://explaintome.streamlit.app/)**! This is an interactive Streamlit application built with LangChain and Python that provides explanations and trivia questions about any topic at varying levels of difficulty: Novice, Intermediate, Advanced, and Expert. Perfect for learners of all stages! 📘💡

## Features ✨

- **Interactive Explanations**: Enter a topic, and get detailed explanations tailored to different expertise levels.
- **Trivia Questions**: Challenge yourself with trivia questions related to the topic, complete with multiple-choice answers and explanations.
- **Background Loading**: Explanations and questions for all levels load in the background for a smooth user experience.
- **Stylish Interface**: Sleek and intuitive UI with support for both light and dark modes.

## Getting Started 🚀

### Prerequisites 📋

Make sure you have the following installed:
- Python 3.7 or higher
- Pip
- Git

### Installation 🔧

1. **Clone the repository**:
   ```bash
   git clone https://github.com/yourusername/ExplainToMeAI.git
   cd ExplainToMeAI
   ```

2. **Create and activate a virtual environment**:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
   ```

3. **Install the required packages**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up your environment variables**:
   - Create a `.env` file in the root directory.
   - Add your OpenAI API key to the `.env` file:
     ```env
     OPENAI_API_KEY=your_openai_api_key_here
     ```

### Running the Application ▶️

Run the following command to start the Streamlit application:
```bash
streamlit run explaintome.py
```

## File Structure 🗂️

```plaintext
Explain-AI/
├── .env                # Environment variables
├── .gitignore          # Git ignore file
├── explaintome.py      # Main application code
├── requirements.txt    # Python dependencies
```

## Example Usage 🌟

1. **Enter a Topic**: In the sidebar, type in a topic you want to learn about and hit "Search" (or press Enter).
2. **Explore Explanations**: Navigate through different tabs (Novice, Intermediate, Advanced, Expert) to see explanations tailored to each level.
3. **Answer Trivia Questions**: Try out the trivia questions to test your knowledge. Click "Show Correct Answer" to see if you got it right!

## Contributing 🤝

Contributions are welcome! Please fork the repository and submit a pull request for any improvements or bug fixes.

1. **Fork the repository**.
2. **Create a new branch**:
   ```bash
   git checkout -b feature/YourFeatureName
   ```
3. **Commit your changes**:
   ```bash
   git commit -m 'Add some feature'
   ```
4. **Push to the branch**:
   ```bash
   git push origin feature/YourFeatureName
   ```
5. **Open a pull request**.


## Acknowledgments 🙏

- Thanks to [OpenAI](https://www.openai.com/) for their powerful language model.
- Inspired by interactive learning platforms and educational tools.

---

Made with ❤️ by Matt Lieb (https://github.com/matthewlieb)
