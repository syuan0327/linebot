#這些是LINE官方開放的套件組合透過import來套用這個檔案上
from linebot import (LineBotApi, WebhookHandler)
from linebot.exceptions import (InvalidSignatureError)
from linebot.models import *

#ImagemapSendMessage(組圖訊息)
def img_message():
    message = ImagemapSendMessage(
        base_url="https://github.com/syuan0327/linebot1/blob/master/deer.jpg?raw=true",
    )
    return message