from restaurant import restaurant


class restaurantmanger:
    # Declaration Function
    def __init__(self, filename: str) -> None:
        self.restaurantdict = {}
        self.startfile = filename
        self.restaurantlist = []
        self.GetRestaurantList()

    # This function takes the file that has all the restaurants with their individual linked files and creates individual 
    # dictionary entries with that name as the key and file as the value to be used by the sort restaurant function
    def GetRestaurantList(self)-> None:
        f = open(self.startfile, 'r')
        lines = f.readlines()
        f.close()
        nameswfiles = {}
        for i in range(len(lines) - 1):
            temp = lines[i]
            name, file = temp.split(':')
            name = name.strip()
            tempdict = {name : file}
            nameswfiles.update(tempdict)
        self.SortRestaurants(nameswfiles)

    # This Function Creates a list of restaurant objects getting the dictionary previously mentioned and insspecting the files
    # It then parses the input of each file to get the menue items containing the information of each item (cost, calories). It then appends
    # them to the list of restaurant objects.
    def SortRestaurants(self, nameswfiles: dict) -> None:
        for key in nameswfiles:
            a = restaurant()
            a.UpdateName(key)
            filename = nameswfiles[key]
            filename = filename.strip()
            filename.replace("\n", "")
            filename = "./restaurants/" + filename
            f = open(filename)
            lines = f.readlines()
            f.close()
            for i in range(len(lines)):
                item = lines[i]
                LinkIndex = item.find("Link:")
                Link = ""
                if LinkIndex != -1:
                    item = item[slice(LinkIndex + 5, len(item))]
                    Link = item.strip()
                    a.UpdateLink(Link)
                else:
                    nameindex = item.find("Item:", 0 , len(item)) + 5
                    costindex = item.find("Cost:")
                    itemname = item[slice(nameindex, costindex)]
                    itemname = itemname.strip()

                    costindex = costindex + 5
                    calindex = item.find("Calories:")
                    cost = item[slice(costindex, calindex)]
                    cost = cost.strip()
                    cost = cost.replace("$", "")
                    costint = int(cost)

                    calindex = calindex + 9
                    cals = item[slice(calindex, len(item) - 1)]
                    cals = cals.strip()
                    cals = cals.replace(".","")
                    calsint = int(cals)
        

                    a.AddMenueItem(itemname, costint, calsint)
            self.restaurantlist.append(a)

    # This function returns the restaurant list for use
    def ReturnRestaruantList(self) -> list:
        return self.restaurantlist





        
        



        


    

