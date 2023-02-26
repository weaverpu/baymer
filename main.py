from restaurant import restaurant
from restaurantmanager import restaurantmanger

a = restaurantmanger("./restaurants/AllRestuarants.txt")
list1 = a.ReturnRestaruantList()
a = list1[0]
dict1 = a.ReturnMenue()
print(dict1)
