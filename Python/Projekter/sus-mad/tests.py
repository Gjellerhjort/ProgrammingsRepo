from bs4 import BeautifulSoup
import requests
import urllib.parse
#class SallingFood:



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
    
    def GetFoodList(self, food):
        food_list = []
        for items in self.GetFood(food):
            item = {
                "name" : str(items["name"]), "price" : str(items["pricing"]["price_per_kilogram"])
            }
            food_list.append(item)

        return food_list
    #def GetPrices(self, food):

    def GetBestPrice(self, food):
        food_list = self.GetFoodList(food)
        print(food_list)
        cheapest_food = min(food_list, key=lambda x:x['price'])

        print(cheapest_food)





rema = RemaFood()
while True:
    food_item = input("find pris: ")
    rema.GetBestPrice(food_item)



