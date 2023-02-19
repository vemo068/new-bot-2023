class Faculty:
    def __init__(self, chat_id,sheetName,website):
        self.website=website
        self.chat_id=chat_id
        self.sheetName=sheetName



# Create objects for each chat ID and sheet name
chatidLang = -1001606282820
sourceLang = 'http://faculty.univ-eloued.dz/faculty/fll'
telebot_lang = Faculty(chatidLang, 'telebot langs', sourceLang)

chatidIktis = -1001671233931
sourceIktis = 'http://faculty.univ-eloued.dz/faculty/fsecg'
telebot_iktis = Faculty(chatidIktis, 'telebot iktisad', sourceIktis)

chatidIjti = -1001630187666
sourceIjti = 'http://faculty.univ-eloued.dz/faculty/fssh'
telebot_ijti = Faculty(chatidIjti, 'telebot ijtim', sourceIjti)

chatidse = -1001677326246
source_se="http://faculty.univ-eloued.dz/faculty/fse"
telebot_se = Faculty(chatidse, 'telebot se news',source_se)

chatidTicno = -1001124432957
source_ticno="http://faculty.univ-eloued.dz/faculty/ft"
telebot_ticno = Faculty(chatidTicno, 'telebot ticno',source_ticno)

chatidBio = -1001561428808
sourceBio = 'http://faculty.univ-eloued.dz/faculty/fsnv'
telebot_bio = Faculty(chatidBio, 'telebot bio', sourceBio)

chatidHo = -1001604610191
sourceHo = 'http://faculty.univ-eloued.dz/faculty/fdsp'
telebot_ho = Faculty(chatidHo, 'telebot ho', sourceHo)

chatidIsl = -1001687171271
sourceIsl = 'http://faculty.univ-eloued.dz/faculty/isi'
telebot_isl = Faculty(chatidIsl, 'telebot isl', sourceIsl)

# Create a list of all the objects
faculti_list = [telebot_isl,telebot_se, telebot_ticno, telebot_bio, telebot_ho, telebot_lang, telebot_iktis,telebot_ijti]