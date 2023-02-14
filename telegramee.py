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

    await bot.send_photo(chat_id=chat_id, photo=photo_url, caption=message, parse_mode='html')


asyncio.run(send_message_with_photo_pdfs("5007987214:AAGkFb4FuNVD4AwvCyPXA_UIM6qIuz4ZdpU",1026024415,"http://faculty.univ-eloued.dz/storage/images/8vpcs3I2rfej4nh3C69SQ5qeQi3uPAgFWk77zMiXi1.jpg","إعلان خاص بطلبة قسم الإعلام الآلي ( تذكير )",
"على جميع طلبة قسم الإعلام الآلي - جميع المستويات -  الولوج إلى الرابط أدناه وملأ الإستمارة بعناية وذلك قبل يوم 28/02/2023 ."
+
"ملاحظة : ملأ الإستمارة إجباري لجميع طلبة القسم .",["http://faculty.univ-eloued.dz/attachment/rvXFxlwRHaVETGranjsqIsEBestWmuF268uJDn8tEw.pdf",
"http://faculty.univ-eloued.dz/attachment/BPdiVG1mVdBg49CBsrzwyJGlqFLq5VgMb9QfoLdao9.pdf","http://faculty.univ-eloued.dz/attachment/AtlsAwd7hTe72lpEfPJaOXjU7dLruBPDfgHzVEUryc.pdf"],
[" اللجنة البيداغوجية سنة 3.pdf"," اللجنة البيداغوجية سنة 3.pdf"," اللجنة البيداغوجية سنة 3.pdf"]))