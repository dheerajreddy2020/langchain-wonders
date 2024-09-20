# FastAPI LangChain Chatbot

This project is a chatbot powered by FastAPI, LangChain, and OpenAI's GPT model. The project includes a simple frontend to interact with the chatbot.

## Features

- Backend: FastAPI with LangChain for OpenAI GPT-3 integration
- Frontend: Basic HTML/JS to interact with the chatbot
- Containerized using Docker
- LangSmith logging for conversations

## Running Locally

### Prerequisites

- **Docker** (For containerized deployment)
- **Python 3.9+** (For running locally without Docker)
- **OpenAI API Key** (For GPT-4 interaction)
- **LangSmith API Key** (For conversation logging)

### Setup

- **Clone the repository**:
   ```bash
   git clone https://github.com/dheerajreddy2020/langchain-wonders.git
   cd langchain-wonders
   ```

### Running with Docker

To build a chatbot using Docker, follow these steps:

1. **Build docker image:**

    ```bash
    docker build -t mychatbot .
    ```

2. **Run docker image:**

    ```bash
    docker run -p 3000:3000 -p 8000:8000 mychatbot
    ```

3. **Access the Application:**

    - **Frontend**: Open your web browser and go to `http://localhost:3000` to view the frontend.
    - **Backend API**: The FastAPI application will be available at `http://localhost:8000`.

### Running the Application Without Docker

To test the application locally without Docker, follow these steps:

1. **Install Python Dependencies:**

    ```bash
    pip install -r requirements.txt
    ```

2. **Start the FastAPI Application:**

    ```bash
    python ./app/app.py
    ```

3. **Serve the Frontend Files:**

    Open a new terminal window and navigate to the `frontend` directory:

    ```bash
    cd ./frontend
    ```

    Then, start a simple HTTP server to serve the static files:

    ```bash
    python -m http.server 3000
    ```

4. **Access the Application:**

    - **Frontend**: Open your web browser and go to `http://localhost:3000` to view the frontend.
    - **Backend API**: The FastAPI application will be available at `http://localhost:8000`.



