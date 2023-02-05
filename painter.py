import openai


class PAINTER:
    def get_drawing_url(self, text):
        openai.api_key = "YOUR KEY"
        image = openai.Image.create(prompt=text, n=1, size="512x512")
        return image["data"][0]["url"]
