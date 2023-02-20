from telegram_env import adid
import telegram
import sheet

MAX_MESSAGE_LENGTH = 4000 # maximum message length allowed by Telegram

async def send_message_with_photo_pdfs (bot_token, faculty, photo_url, caption, description,save_link, pdf_urls=None, pdf_titles=None):
    bot = telegram.Bot(token=bot_token)
    
    
    message = f"<b>{caption}</b>\n{description}"
    
   
    save_message=f"<b>{caption}</b>\n<a href='{save_link}'>الرابط</a>"

    if pdf_urls:
        for i, pdf_url in enumerate(pdf_urls):
            title = pdf_titles[i] if pdf_titles and i < len(pdf_titles) else "link1"
            message += f"\n<a href='{pdf_url}'>{title}</a>"
            
    try :
       sent_mm= await bot.send_photo(chat_id=faculty.chat_id, photo=photo_url, caption=message, parse_mode='html',write_timeout=120)
       if sent_mm is not None:
            sheet.insert_news(caption,faculty.sheetName)
    except Exception as e:
        try:
            sent_mm= await bot.send_photo(chat_id=faculty.chat_id, photo=photo_url, caption=save_message, parse_mode='html',write_timeout=60)
            if sent_mm is not None:
                sheet.insert_news(caption,faculty.sheetName)
        except Exception as ee:
            await bot.send_message(chat_id=adid, text="too long  "+str(len(message))+"--"+str(len(save_message)))
