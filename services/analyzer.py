import google.generativeai as genai
import os
from dotenv import load_dotenv
import logging

load_dotenv()

logger = logging.getLogger(__name__)

class AIAnalyzer:
    def __init__(self, api_key: str = None):
        api_key = api_key or os.getenv("GEMINI_API_KEY")
        if not api_key:
            raise ValueError("GEMINI_API_KEY is not set.")
        genai.configure(api_key=api_key)
        self.model = genai.GenerativeModel('gemini-flash-latest')

    async def analyze_sector(self, sector: str, market_data: str) -> str:
        """
        Uses Gemini API to analyze market data and generate a structured markdown report.
        """
        prompt = f"""
        Analyze the following market data for the '{sector}' sector in India and generate a comprehensive trade opportunities report.
        
        Market Data:
        {market_data}
        
        The report should be in structured Markdown format and include:
        1. Executive Summary
        2. Current Market Trends (India specific)
        3. Key Trade Opportunities
        4. Potential Risks and Challenges
        5. Strategic Recommendations
        
        Ensure the report is professional, data-driven (based on the provided snippets), and actionable.
        Return ONLY the markdown content.
        """
        
        try:
            response = await self.model.generate_content_async(prompt)
            return response.text
        except Exception as e:
            logger.error(f"Error during AI analysis: {str(e)}")
            return f"# Analysis Error\n\nFailed to generate report: {str(e)}"
