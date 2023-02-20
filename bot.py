from faculty import faculti_list
from scraper import telenews_scraping
from telegram_env import adid,api_key
import telegram
import traceback
import asyncio
import time

async def process_faculties(faculties):
    bot = telegram.Bot(token=api_key)
    while True:
        for faculty in faculties:
            try:
                await telenews_scraping(faculty)
            except Exception as e:
                # If there is any exception, send a warning message to admin
                error_message = f"Error processing faculty {faculty.sheetName}: {traceback.format_exc()}"
                await bot.send_message(chat_id=adid, text=error_message)
            time.sleep(60)

        time.sleep(3600)   

# Create a new event loop
loop = asyncio.new_event_loop()

# Set the new event loop as the default event loop
asyncio.set_event_loop(loop)

# Run your async function inside the new event loop
loop.run_until_complete(process_faculties(faculti_list))

# Close the event loop
loop.close()
