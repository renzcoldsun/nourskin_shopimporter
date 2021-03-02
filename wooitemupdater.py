import models
from woocommerce import API as wooo_api
from config import Config

c = Config()
wcapi = wooo_api(
                url=c.woo_get_url(),
                consumer_key = c.woo_get_consumer_key(),
                consumer_secret = c.woo_get_consumer_secret(),
                version = "wc/v3"
                )

item = models.Item()
for one_item in item.getItems():
    print(one_item)

    # product_link = "products/" + str(item.id)
    # woo_item = wcapi.get(product_link)
    # if woo_item.status_code == 404:
    #     print("INSERT")
    # else:
    #     print("UPDATE")

