from flask import Flask, request, abort

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import *


#======這裡是呼叫的檔案內容=====
from message import *
from new import *
from Function import *
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
        message = TextSendMessage(text='武器飛走了')
        line_bot_api.reply_message(event.reply_token, message)
    elif '速速前' in msg:
        message = TextSendMessage(text='咻~')
        line_bot_api.reply_message(event.reply_token, message)
    else:
        message = TextSendMessage(text=msg)
        line_bot_api.reply_message(event.reply_token, message)
        


import os
if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
