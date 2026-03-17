from fastapi import FastAPI, Depends, HTTPException, Request
from fastapi.responses import PlainTextResponse, FileResponse
from fastapi.staticfiles import StaticFiles
from services.data_collector import DataCollector
from services.analyzer import AIAnalyzer
from components.security import get_api_key, limiter, session_tracker
from components.models import AnalysisReport
import datetime
import uvicorn
import logging
import os

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = FastAPI(
    title="Trade Opportunities API",
    description="Analyzes market data for Indian sectors using Gemini AI.",
    version="1.0.0"
)

# Mount static files
app.mount("/static", StaticFiles(directory="static"), name="static")

# Initialize services
collector = DataCollector()
analyzer = AIAnalyzer()

@app.get("/")
async def root():
    return FileResponse("static/index.html")

@app.get("/analyze/{sector}", 
         response_class=PlainTextResponse, 
         dependencies=[Depends(get_api_key)])
@limiter.limit("10/minute")
async def analyze_sector(request: Request, sector: str):
    """
    Analyzes the specified sector and returns a markdown report.
    """
    logger.info(f"Received request to analyze sector: {sector}")
    
    # Track session/useage in-memory
    client_host = request.client.host
    usage_count = session_tracker.track_request(client_host)
    logger.info(f"Client {client_host} usage count: {usage_count}")
    
    try:
        # Step 1: Collect Data
        market_data = await collector.collect_market_data(sector)
        
        # Step 2: Analyze Data
        report_md = await analyzer.analyze_sector(sector, market_data)
        
        # Return as raw markdown text as requested (suitable for .md file)
        return report_md
        
    except Exception as e:
        logger.error(f"Error processing analysis for {sector}: {str(e)}")
        raise HTTPException(status_code=500, detail=str(e))

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
