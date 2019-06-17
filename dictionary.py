shopping_cart={
  "item_name":"speakers",
  "price":50,
  "supplier":"ashu and corporation"
}
print(shopping_cart["item_name"])
new_dict=dict(name="ashu",rollno="01220802716")
#new_dict.clear()
new_dict.update(shopping_cart)
new_dict.pop("name")
new_dict.popitem()
print(new_dict)