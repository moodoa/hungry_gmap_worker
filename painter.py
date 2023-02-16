import openai


class PAINTER:
    def __init__(self):
        self.key = "YOUR_API_KEY"

    def get_drawing_url(self, text):
        openai.api_key = self.key
        image = openai.Image.create(prompt=text, n=1, size="512x512")
        return image["data"][0]["url"]

    def get_response(self, text):
        openai.api_key = self.key
        response = openai.Completion.create(
            engine="text-davinci-003",
            prompt=text,
            max_tokens=128,
            n=1,
            temperature=1,
            top_p=0.75,
        )
        message = response.choices[0].text.strip()
        return message


