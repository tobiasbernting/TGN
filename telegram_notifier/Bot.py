import telegram

class Bot:

  def __init__(self, token, chat_id):
    self.token = token
    self.chat_id = chat_id
    self.bot = telegram.Bot(token='%s' % self.token)

  def send_message(self, message):
    try:
      self.bot.send_message(chat_id=self.chat_id, text='%s' % (message))
    except Exception as err:
      print("Whoops, something wrong %s" % err)