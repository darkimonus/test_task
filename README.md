# Text Summarization API

This is a FastAPI application that provides an endpoint to summarize text using the `facebook/bart-large-cnn` model from Hugging Face.

## Prerequisites

Before you begin, ensure you have the following installed:

- Python 3.7 or later
- pip (Python package installer)

## Installation

1. **Clone the repository**:

    ```sh
    git clone https://github.com/darkimonus/test_task.git
    cd test_task
    ```

2. **Create a virtual environment** (optional but recommended):

    ```sh
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. **Install the dependencies**:

    ```sh
    pip install -r requirements.txt
    ```

4. **Set up environment variable**:

    ```sh
    export API_TOKEN=['your_api_token']  # On Windows use `set API_TOKEN=your_api_token`
    ```

## Running the Application

To run the FastAPI application, use the following command:

```sh
uvicorn main:app --reload
