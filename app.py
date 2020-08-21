from flask import Flask, request, abort

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import *

import random 
import requests as req


#======這裡是呼叫的檔案內容=====
#from massage import *
#from new import *
#from Function import *
#======這裡是呼叫的檔案內容=====

app = Flask(__name__)

# Channel Access Token
line_bot_api = LineBotApi('VcNCiNMRUPAdMhdubuBWdcx1OTeBpNMgYncC7tx/8RT7MjdJRrdv2N5LgGjUA9JLsbmWncrCKWIeHmGc8Dk/Jdjv1lwC4SGu6LpsujANhz6YiYvBvPQu/ucQzFNfumAREqoiyZKywDk4czKYj+bQEQdB04t89/1O/w1cDnyilFU=')
# Channel Secret
handler = WebhookHandler('35480a6cf7f6f8b8932cf1c70456915e')



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
    if 'yes' in msg:
        message1=[]
        message1.append( TextSendMessage('第一題') )
        message1.append( TextSendMessage('收到魔動訊號 北極星光閃耀\n飛向快樂星球\n稍息立正稍息立正站好\n超時空的邂逅 銀河系外接頭\n說出你的暗號：') )
        line_bot_api.reply_message(event.reply_token, message1 )
    if '魔動北極星' in msg:
        message1 = TextSendMessage(text='哇~好聰明恭喜你答對了!')
        message2 = TextSendMessage(text='請輸入2來進行下一題')
        sticker = StickerSendMessage(package_id=11537, sticker_id=52002734 ) 
        line_bot_api.reply_message(event.reply_token, [message1,message2,sticker])
    if '2' in msg:
        message1 = TextSendMessage(text='第二題(送分題)')
        message2 = TextSendMessage(text='請問你的寶貝女友愛吃甚麼?')
        message3 = TextSendMessage(text='A.番茄蛋花湯\nB.火鍋\nC.乳酪蛋糕')
        message4 = TextSendMessage(text='請回答(你要是錯了就死定了^^)')
        line_bot_api.reply_message(event.reply_token, [message1,message2,message3,message4])
        

    
    else:
        message = TextSendMessage(text=msg)
        line_bot_api.reply_message(event.reply_token, message)

@handler.add(MessageEvent, message=StickerMessage)
def handle_sticker_message(event):
    pid1=1
    sid1_1=random.randint(1,21)
    sid1_2=random.randint(100,139)
    sid1_3=random.randint(401,430)
    pid2=2
    sid2_1=random.randint(18,47)
    sid2_2=random.randint(140,179)
    sid2_3=random.randint(501,527)
    pid3=3
    sid3=random.randint(180, 259)
    pid4=4
    sid4_1=random.randint(260,307)
    sid4_2=random.randint(601,632)
    a1=(pid1,sid1_1)
    a2=(pid1,sid1_2)
    a3=(pid1,sid1_3)
    b1=(pid2,sid2_1)
    b2=(pid2,sid2_2)
    b3=(pid2,sid2_3)
    c1=(pid3,sid3)
    d1=(pid4,sid4_1)
    d2=(pid4,sid4_2)
    (s1,s2)=random.choice([a1,a2,a3,b1,b2,b3,c1,d1,d2])
    line_bot_api.reply_message(
        event.reply_token, 
        StickerSendMessage(package_id=s1, sticker_id=s2)
    )





import os
if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
    
