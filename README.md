# Trade Opportunities API

A FastAPI service that analyzes market data and provides trade opportunity insights for specific sectors in India using Google Gemini AI.

## Features
- **Market Data Collection**: Automatically searches for the latest news and trends using DuckDuckGo.
- **AI Analysis**: Uses Gemini 1.5 Flash to generate structured markdown reports.
- **Security**:
    - API Key Authentication (`X-API-Key` header).
    - Rate Limiting (10 requests per minute).
    - In-memory session tracking.
- **Async Implementation**: Fully asynchronous for better performance.

## Setup Instructions

### 1. Prerequisites
- Python 3.8+
- [Google Gemini API Key](https://aistudio.google.com/app/apikey)

### 2. Installation
```powershell
# Clone or move to the project directory
cd "Trade Opportunities API"

# Create a virtual environment (optional but recommended)
python -m venv venv
.\venv\Scripts\Activate

# Install dependencies
pip install -r requirements.txt
```

### 3. Configuration
Create a `.env` file in the root directory (you can copy `.env.example`):
```env
GEMINI_API_KEY=your_actual_gemini_api_key
API_KEY=my_secret_token
```

### 4. Running the API
```powershell
python main.py
```
The server will start at `http://localhost:8000`.

## API Usage

### Single Endpoint: Analyze Sector
`GET /analyze/{sector}`

**Headers:**
- `X-API-Key`: `my_secret_token` (as configured in .env)

**Example Request:**
`GET http://localhost:8000/analyze/pharmaceuticals`

**Expected Response:**
A structured Markdown report including Executive Summary, Market Trends, Opportunities, Risks, and Recommendations.

## Documentation
FastAPI automatically generates documentation:
- **Swagger UI**: `http://localhost:8000/docs`
- **ReDoc**: `http://localhost:8000/redoc`

## Project Structure
- `main.py`: Entry point and API routes.
- `services/`: Core logic (Data collection, AI analysis).
- `components/`: API models and Security/Middleware.
