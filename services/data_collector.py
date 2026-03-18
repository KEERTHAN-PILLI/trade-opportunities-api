import asyncio
from ddgs import DDGS
import logging

logger = logging.getLogger(__name__)

class DataCollector:
    def __init__(self):
        self.ddgs = DDGS()

    async def collect_market_data(self, sector: str) -> str:
        """
        Collects recent market news and data for a given sector in India.
        """
        query = f"latest market trends and trade opportunities in {sector} sector India 2024 2025"
        logger.info(f"Searching for: {query}")
        
        try:
            # Running in a thread pool since ddgs might be blocking or complex
            loop = asyncio.get_event_loop()
            results = await loop.run_in_executor(None, lambda: list(self.ddgs.text(query, max_results=10)))
            
            if not results:
                return "No recent market data found for this sector."
            
            formatted_data = "\n\n".join([
                f"Title: {res.get('title')}\nSnippet: {res.get('body')}\nSource: {res.get('href')}"
                for res in results
            ])
            return formatted_data
            
        except Exception as e:
            logger.error(f"Error collecting data: {str(e)}")
            return f"Error during data collection: {str(e)}"
