# Mini-Macro

A simple FastAPI application for analyzing macronutrients in foods using an LLM.

## Overview

Mini-Macro accepts food descriptions and returns macronutrient breakdowns by having an AI analyze the nutritional content.

## Getting Started

### Prerequisites

- Python 3.10+
- API key for one of the supported LLM providers:
  - Generic OpenAI-compatible API (Grok, etc.)
  - OpenAI

### Installation

1. Clone the repository
2. Install dependencies: `pip install -r requirements.txt`
3. Create `.env` file with your API key:

   ```
   # For generic LLM client
   LLM_API_KEY=your_api_key_here
   LLM_BASE_URL=https://api.x.ai  # or your preferred LLM provider
   LLM_MODEL=grok-2-latest        # or your preferred model
   
   # For OpenAI client (if using)
   OPENAI_API_KEY=your_openai_key_here
   OPENAI_MODEL=gpt-3.5-turbo
   ```

### Running

```
uvicorn app.main:app --reload
```

## API Endpoints

- `GET /`: Basic app info
- `GET /healthcheck`: Health check
- `POST /view/nutrients`: Extract nutrition info from food description

Example request:
```json
{
  "description": "a banana, 2 eggs, coffee"
}
```