from linebot import (LineBotApi, WebhookHandler)
from linebot.exceptions import (InvalidSignatureError)
from linebot.models import *

def sticker(event)
    pid = event.message.package_id
    sid = event.message.sticker_id
    line_bot_api.reply_message(
        event.reply_token, 
        StickerSendMessage(package_id=pid, sticker_id=sid)
    )
