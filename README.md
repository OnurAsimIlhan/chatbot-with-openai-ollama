# Q&A Chatbot With OpenAI & Ollama

This project is an enhanced Q&A chatbot built using Streamlit and OpenAI's language models and Ollama open source models. The chatbot allows users to ask questions and receive responses from selected models.

## Features

- Select from multiple  models.
- Adjust response parameters such as temperature and max tokens.
- User-friendly interface built with Streamlit.

## Streamlit Deployment

The application is deployed using Streamlit. You can access it without running the code locally by visiting the following link:

[Streamlit App](https://next-word-prediction-lstm-ztw4a4hu54tnpgn7943pmx.streamlit.app/)

## Setup (if you want to run locally)

1. Clone the repository:
    ```sh
    git clone https://github.com/OnurAsimIlhan/chatbot-with-openai-ollama.git
    cd chatbot-with-openai-ollama
    ```

2. Create and activate a virtual environment:
    ```sh
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. Install the required packages:
    ```sh
    pip install -r requirements.txt
    ```

4. Create a `.env` file in the root directory and add your OpenAI API key:
    ```env
    LANGCHAIN_API_KEY=your_openai_api_key
    ```
## Usage
1. Run the Streamlit app:
    ```sh
    streamlit run app.py
    ```
2. Open your web browser and go to `http://localhost:8501`.

3. Enter your OpenAI API key in the sidebar.

4. Select the desired OpenAI model, adjust the response parameters, and ask your questions in the main interface.
