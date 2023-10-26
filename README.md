# Solution Code: Text Processing API Project


This API provides text processing functionalities, such as tokenization into words and sentences, and spelling correction, leveraging the capabilities of the TextBlob library.

## Installation

1. Clone this repository.
2. Navigate to the project directory:
   ```bash
   cd path_to_directory
   ```
3. Set up a virtual environment (recommended). Depending on your operating system, use one of the following:
   - On macOS and Linux:
     ```bash
     python -m venv venv
     source venv/bin/activate
     ```
   - On Windows:
     ```bash
     python -m venv venv
     .\venv\Scripts\activate
     ```
4. Install the required packages (Flask should be in the `requirements.txt`):
   ```shell
   pip install -r requirements.txt
   ```
5. And then, download the necessary corpora for TextBlob:
   ```bash
   python -m textblob.download_corpora
   ```
6. Run the API:
   * By default, the API will start on `http://127.0.0.1:5001/`.
   ```bash
   python path_to_file.py
   ```

## Endpoints and Usage

1. Home Endpoint:

   Navigate to `/` to get a welcome message.

2. Tokenization Endpoint (`/tokenize`):

   - Method: `POST`
   - Request Body: `{"text": "Your text here."}`
   - Response: A JSON with tokenized words and sentences.

3. Text Correction Endpoint (`/correct`):

   - Method: `POST`
   - Request Body: `{"text": "Your text with errrs."}`
   - Response: A JSON with the corrected text.

## Description

This API is built on Flask and utilizes the TextBlob library for natural language processing tasks, such as tokenization and spelling correction. The API is designed to be simple, intuitive, and cater to basic text processing needs.