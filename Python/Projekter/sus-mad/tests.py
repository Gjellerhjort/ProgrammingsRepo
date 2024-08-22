from bs4 import BeautifulSoup
import requests
import urllib.parse

class FoodItem:
    def __init__(self, name, price, price_per_kilogram, price_per_unit, unit):
        self.name = name
        self.price = float(price)  # Ensure price is stored as a float
        self.price_per_kilogram = float(price_per_kilogram)
        self.price_per_unit = float(price_per_unit)
        self.unit = str(unit)


    def __repr__(self):
        return f"FoodItem(name='{self.name}', price={self.price}, price per kg={self.price_per_kilogram}, price per unit={self.price_per_unit})"

    def __str__(self):
        return f"{self.name}: {self.price_per_unit} DKK per kg"

    def get_name(self):
        return self.name
    
    def get_price(self):
        return self.price
    
    def get_price_per_kilogram(self):
        return self.price_per_kilogram

    def get_price_per_unit(self):
        return self.price_per_unit

class SallingFood:
    salling_api = ""
    url = "https://api.sallinggroup.com/v1-beta/product-suggestions/relevant-products?query="
    headers = {
    'Authorization': "Bearer " + salling_api
    }
    def GetFood(self, food):
        encoded_string = urllib.parse.quote(food)
        url = self.url + encoded_string + "/"
        response = requests.get(url, headers=self.headers)
        print(response.json())


class RemaFood:
    web_url = "https://flwdn2189e-dsn.algolia.net/1/indexes/aws-prod-products/query?x-algolia-agent=Algolia%20for%20vanilla%20JavaScript%203.21.1&x-algolia-application-id=FLWDN2189E&x-algolia-api-key=fa20981a63df668e871a87a8fbd0caed"
    web_data = {"params":"query=k%C3%B8d&length=18&offset=0&clickAnalytics=true&facetFilters=%5B%5D&facets=%5B%22labels%22%5D"}

    def GetFood(self, food):
        # URL encode the string
        encoded_string = urllib.parse.quote(food)


        params = f"query={encoded_string}&length=18&offset=0&clickAnalytics=true&facetFilters=%5B%5D&facets=%5B%22labels%22%5D"
        self.web_data[params] = params
        response = requests.post(self.web_url, json = self.web_data)
        data = response.json()
        return data.get('hits', [])
    
    def GetFoodItems(self, food):
        foodItem_list = []
        for items in self.GetFood(food):
            price_per_unit = str(items['pricing']['price_per_unit'])
            price, unit_str = price_per_unit.split(" ", 1)
            item = FoodItem(items['name'], float(items['pricing']['price']), float(items['pricing']['price_per_kilogram']), float(price), unit_str)
            foodItem_list.append(item)

        return foodItem_list
    #def GetPrices(self, food):

    def GetBestPrice(self, food):
        food_list = self.GetFoodItems(food)
        cheapest_food = min(food_list, key=lambda x:x.get_price_per_unit())

        print(cheapest_food)





rema = RemaFood()
salling = SallingFood()


while True:
    food_item = input("find pris: ")
    salling.GetFood(food_item)



