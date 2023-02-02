from flask import Flask, request, abort
from linebot import LineBotApi, WebhookHandler
from linebot.exceptions import InvalidSignatureError
from linebot.models import MessageEvent, TextMessage, TextSendMessage
from hungryworker import HUNGRYWORKER
import requests


app = Flask(__name__)

line_bot_api = LineBotApi('YOUR_CHANNEL_ACCESS_TOKEN')
handler = WebhookHandler('YOUR_CHANNEL_SECRET')


@app.route("/callback", methods=["POST"])
def callback():
    signature = request.headers["X-Line-Signature"]
    body = request.get_data(as_text=True)
    # app.logger.info("Request body: " + body)
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        print(
            "Invalid signature. Please check your channel access token/channel secret."
        )
        abort(400)
    return "OK"


@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    keyword = event.message.text.lower()
    gmap = HUNGRYWORKER()
    if keyword.startswith("找店家") and "/" in keyword:
        targets = keyword.split("/")
        location = targets[1]
        category = targets[2]
        radius = targets[3]
        output = gmap.get_shop(location, category, int(radius))
        line_bot_api.reply_message(event.reply_token, TextSendMessage(text=output))


if __name__ == "__main__":
    app.run()
