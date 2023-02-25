

class restaurant:
    def __init__(self):
        self.menue = {}
        self.name = ""
        self.lat = 0
        self.lon = 0
    
    # This function will add menue items with items and costs to the objects menue variable
    def AddMenueItem(self, item: str, cost: int, cals: int) -> None:
        iteminfo = [cost, cals]
        itemcombination = {item : iteminfo}
        self.menue.update(itemcombination)

    # This function is meant to update the lat and longitude based on information read from the restaurant text file:
    def UpdateLatLon(self, lat: float, lon: float) -> None:
        self.lat = lat
        self.lon = lon
    
    # This function is meant to update the name of the restaurant from the restaurant text file
    def UpdateName(self, name : str) -> None:
        self.name = name
    
    # This function returns the name
    def ReturnName(self) -> str:
        return self.name

    # This function returns the lat and lon coordinates for the map object
    def ReturnLatLon(self) -> str:
        return self.lat, self.lon
    
    # This function returns the menue of the restaurat
    def ReturnMenue(self) -> dict:
        return self.menue
    # Given a budget cost, it returns any items in the menue list that match the criteria requested
    def MakeSuggestion(self, budgetcost: int, calories: int) -> dict:
        validentries = {}
        for key in self.menue():
            iteminfo = self.menue[key]
            if iteminfo[0] <= budgetcost:
                combo = {key : iteminfo}
                validentries.update(combo)
        return validentries



    
    
    