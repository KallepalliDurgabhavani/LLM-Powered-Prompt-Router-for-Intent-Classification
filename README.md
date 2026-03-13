# 🤖 LLM-Powered Prompt Router

An intelligent, intent-based routing service that classifies user requests and delegates them to specialized AI expert personas. Built with **Google Gemini** and designed for high precision and cost-efficiency.

---

## 🏗️ Architecture

The system follows a modular "Classify-then-Respond" design pattern. This ensures that user requests are handled by the most relevant "Expert Persona" rather than a generic monolithic prompt.

![Architecture Diagram](src/image.png)

### Core Components

- **Intent Classifier**: Uses Gemini's structured output to identify the user's goal (Code, Data, Writing, Career, or Unclear).
- **Expert Personas**: Sharp, opinionated system prompts that establish role, tone, and constraints.
- **Router Orchestrator**: Coordinates the flow between classification, routing, and response generation.
- **Audit Logger**: Records all interactions in a JSON Lines (`.jsonl`) format for observability.

---

## 📂 Project Structure

```text
.
├── src/                # Core application logic
│   ├── classifier.py   # Gemini-powered intent classification
│   ├── responder.py    # Expert persona response generation
│   ├── config.py       # Configuration & Environment management
│   ├── logger_utils.py # JSON Lines logging utilities
│   ├── main.py         # Main orchestration entry point
│   ├── prompts.json    # Expert persona definitions
│   └── image.png       # Architecture diagram
├── tests/              # Test suite
│   ├── test_classifier.py        # Classifier unit tests
│   └── test_router_integration.py # End-to-end integration tests
├── .env.example        # Template for environment variables
├── requirements.txt    # Python dependencies
├── Dockerfile          # Containerization setup
└── docker-compose.yml  # Multi-container orchestration
```

---

## 🛠️ Getting Started

### Prerequisites

- **Python 3.11+**
- **Google AI (Gemini) API Key**

### 1. Setup Environment

Clone the repository and create your local environment file:

```bash
cp .env.example .env
```

Update `.env` with your `GOOGLE_API_KEY`.

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 3. Run the Service

You can run the orchestrator directly from the root directory:

```bash
python -m src.main "how do i sort a list of objects in python?"
```

### 4. Run Tests

Execute the test suite using Python's module system from the root directory:

```bash
# Run all tests
python -m unittest discover tests

# Run specific test files
python -m tests.test_classifier
python -m tests.test_responder
python -m tests.test_router_integration
```

---

## 🐳 Running with Docker

Easily spin up the service using Docker Compose:

```bash
docker-compose up --build
```

---

## 📜 Expert Persona Definitions

The system current supports the following "expert" roles:

| Persona | Responsibility |
| :--- | :--- |
| **Code Expert** | Production-quality code with technical explanations. |
| **Data Analyst** | Statistical patterns, correlations, and visualizations. |
| **Writing Coach** | Feedback on clarity, tone, and structure. |
| **Career Advisor** | Pragmatic, actionable career guidance. |

---

## 📊 Observability & Logging

Every interaction is captured in `route_log.jsonl` for audit and refinement:

```json
{
  "intent": "code",
  "confidence": 1.0,
  "user_message": "how do i sort a list of objects in python?",
  "final_response": "..."
}
```"# LLM-Powered-Prompt-Router-for-Intent-Classification" 
