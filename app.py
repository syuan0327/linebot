from flask import Flask, request, abort

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import *


#======這裡是呼叫的檔案內容=====
#from massage import *
#from new import *
#from Function import *
#======這裡是呼叫的檔案內容=====

app = Flask(__name__)

# Channel Access Token
line_bot_api = LineBotApi('zpR6x4Yx6Y7ixafUvkn7JtWXho8SH215tvYXMlPEQ5ZE0uP8fZEgZ1dbeMGucH+Cz+nGq9CavJwt6Jhd/2IuZx7qkGLxkKmNhQ90VE4pvgAkbUdWUi0L9j4H9zwWz/2uYgsJwZkNl42W30vcmb18pgdB04t89/1O/w1cDnyilFU=')
# Channel Secret
handler = WebhookHandler('25c641fcc4425171f5fa22193a7c703b')

# 監聽所有來自 /callback 的 Post Request
@app.route("/callback", methods=['POST'])
def callback():
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']
    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)
    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)
    return 'OK'

# 處理訊息
@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    msg = event.message.text
    if '去去武器走' in msg:
        message = TextSendMessage(text='(∩^o^)⊃━☆ﾟ.*･｡')
        line_bot_api.reply_message(event.reply_token, message)
    if '速速前' in msg:
        message = TextSendMessage(text='咻~')
        line_bot_api.reply_message(event.reply_token, message)
    if '復復修' in msg:
        message = TextSendMessage(text='登登登ㄌㄥ')
        line_bot_api.reply_message(event.reply_token, message)
    if '疾疾護法現身' in msg:
        message = TextSendMessage(text='🦌')
        line_bot_api.reply_message(event.reply_token, message)
    if '阿瓦坦克坦拉' in msg:
        message = TextSendMessage(text='啊~~~~')
        line_bot_api.reply_message(event.reply_token, message)
    

    if '你好' in msg:
        message = TextSendMessage(text='你好呀，你今天快樂嗎?')
        line_bot_api.reply_message(event.reply_token, message)
    if '生日' in msg:
        message = TextSendMessage(text='HAPPY BIRTHDAY!')
        sticker = StickerSendMessage(package_id=11537, sticker_id=52002734 ) 
        line_bot_api.reply_message(event.reply_token, [message,sticker])
    if '早安' in msg: 
        message = TextSendMessage(text='早安')
        sticker = StickerSendMessage(package_id=3, sticker_id=240 ) 
        line_bot_api.reply_message(event.reply_token, [message,sticker])
    else:
        message = TextSendMessage(text=msg)
        line_bot_api.reply_message(event.reply_token, message)

@handler.add(MessageEvent, message=StickerMessage)
def handle_sticker_message(event):
    pid = event.message.package_id
    sid = event.message.sticker_id
    line_bot_api.reply_message(
        event.reply_token, 
        StickerSendMessage(package_id=pid, sticker_id=sid)
    )
    

@handler.add(MessageEvent, message=ImageMessage)
def handle_image_message(event):
    img= event.message.img
    line_bot_api.reply_message(
        event.reply_token, 
        StickerSendMessage(img)
    )




import os
if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
    
