import models

from woocommerce import API as wooo_api

api_consumer_key = "ck_f65e9c5b696f93404da8cf79fdfd98fe5da293cc"
api_consumer_secret = "cs_92a2c541f735b0ac90000875194b6a961321b462"

wcapi = wooo_api(
                url="http://localhost",
                consumer_key = api_consumer_key,
                consumer_secret = api_consumer_secret,
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

