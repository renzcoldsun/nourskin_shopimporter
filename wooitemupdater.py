import models
from woocommerce import API as wooo_api
from config import Config

c = Config()
wcapi = wooo_api(
                url=c.woo_get_url(),
                consumer_key = c.woo_get_consumer_key(),
                consumer_secret = c.woo_get_consumer_secret(),
                wp_api = True,
                version = "wc/v3",
                query_string_auth = True
                )

#fUrl = "/index.php/wp-json/wc/v3/" #does not work
fUrl = ""
# create or update product categories
data = {
        "product_category" : {
            "name" : "Beauty Products"
            }
        }

category = wcapi.get(fUrl + "products/categories/9")
if category.status_code == 404:
    status = wcapi.post(fUrl + "products/categories", data)
    if status.status_code != 201:
        print("Unable to create product category, leave!")
        exit(1)
    print("Creating product category", status)
else:
    status = wcapi.post(fUrl + "products/categories/9", data)
    if status.status_code != 201:
        print("Unable to update product category, leave!")
        exit(1)
    print("Updating product category", status)


item = models.Item()
for one_item in item.getItems():
    product_link = "products/" + str(item.id)
    woo_item = wcapi.get(product_link)
    if woo_item.status_code == 404:
        data = {
            "product": {
                "title" : str(one_item.code) + "-" + str(one_item.name),
                "type" : "simple",
                "regular_price" : str(one_item.sale_price),
                "description" : one_item.description,
                "short_description" : one_item.description,
                "categories" : [ 9 ],
                }
            }
        response = wcapi.post(fUrl + "products", data)
        print("Created product: ", one_item.name, response)
    else:
        data = {
            "product": {
                "title" : str(one_item.code) + "-" + str(one_item.name),
                "type" : "simple",
                "regular_price" : str(one_item.sale_price),
                "description" : one_item.description,
                "short_description" : one_item.description,
                "categories" : [ 1 ],
                }
            }
        response = wcapi.put(fUrl + "products/" + str(one_item.id), data)
        print("Updated product: ", one_item.name, response)

