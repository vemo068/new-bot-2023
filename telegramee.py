import requests
import json
import telegram
import asyncio

async def send_message_with_photo_pdfs (bot_token, chat_id, photo_url, caption, description, pdf_urls=None, pdf_titles=None):
    bot = telegram.Bot(token=bot_token)

    message = f"<b>{caption}</b>\n{description}"

    if pdf_urls:
        for i, pdf_url in enumerate(pdf_urls):
            title = pdf_titles[i] if pdf_titles and i < len(pdf_titles) else "link1"
            message += f"\n<a href='{pdf_url}'>{title}</a>"

    await bot.send_photo(chat_id=chat_id, photo=photo_url, caption=message, parse_mode='html',write_timeout=60)

