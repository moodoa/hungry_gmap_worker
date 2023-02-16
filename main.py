from flask import Flask, request, abort
from linebot import LineBotApi, WebhookHandler
from linebot.exceptions import InvalidSignatureError
from linebot.models import MessageEvent, TextMessage, TextSendMessage, ImageSendMessage
from hungryworker import HUNGRYWORKER
from painter import PAINTER
import requests


app = Flask(__name__)

line_bot_api = LineBotApi('YOUR_CHANNEL_ACCESS_TOKEN')
handler = WebhookHandler('YOUR_CHANNEL_SECRET')


@app.route("/callback", methods=["POST"])
def callback():
    signature = request.headers["X-Line-Signature"]
    body = request.get_data(as_text=True)
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
    if keyword.startswith("找店家") and "/" in keyword:
        gmap = HUNGRYWORKER()
        targets = keyword.split("/")
        location = targets[1]
        category = targets[2]
        radius = targets[3]
        output = gmap.get_shop(location, category, int(radius))
        line_bot_api.reply_message(event.reply_token, TextSendMessage(text=output))

    elif keyword.startswith("畫圖") and "/" in keyword:
        painter = PAINTER()
        text = keyword.split("/")[1]
        url = painter.get_drawing_url(text)
        line_bot_api.reply_message(
            event.reply_token,
            ImageSendMessage(original_content_url=url, preview_image_url=url),
        )
    
    elif keyword.startswith("改履歷") and "/" in keyword:
        text = keyword.split("/")[1]
        bot = PAINTER()
        first_version = bot.get_response(f"能幫我把以下的履歷改成英文的嗎?\n{text}")
        final_version = bot.get_response(
            f"critique the experience on a resume\n{first_version},and rewrite the above resume bullet points using the suggestions you provided"
        )
        line_bot_api.reply_message(
            event.reply_token, TextSendMessage(text=final_version)
        )



if __name__ == "__main__":
    app.run()

