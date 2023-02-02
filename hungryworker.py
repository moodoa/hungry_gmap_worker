import googlemaps


class HUNGRYWORKER:
    def __init__(self):
        self.gmaps = googlemaps.Client(key="YOUR_GOOGLE_MAP_API_KEY")

    def get_shop(self, user_location, category, user_radius):
        output = ""
        geocode_result = self.gmaps.geocode(user_location)
        loc = geocode_result[0]["geometry"]["location"]
        output += f"{user_location}為中心{str(user_radius)}公尺的{category}店家: \n\n"
        shops = self.gmaps.places_nearby(
            keyword=category, location=loc, radius=user_radius, language="zh-TW"
        )
        for shop in sorted(shops["results"], key=lambda x: x["rating"], reverse=True):
            output += "🥢" + (shop["name"]) + "\n"
            output += self._get_shop_status(shop)
            output += f'評分：{(shop["rating"])}\n'
            output += f"電話：{self._get_shop_number(shop)}\n"
            output += f"地址：{shop['vicinity']}\n\n"
        return output

    def _get_shop_status(self, shop):
        status = "休息中\n"
        try:
            opening = shop["opening_hours"]["open_now"]
            if opening:
                status = "營業中\n"
        except:
            status = "待確認\n"
        return status

    def _get_shop_number(self, shop):
        number = "待確認"
        try:
            number = self.gmaps.place(place_id=shop["place_id"], language="zh-TW")[
                "result"
            ]["formatted_phone_number"]
        except:
            pass
        return number
