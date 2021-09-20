import requests
import math

while True:
    # pulling data from api
    data = requests.get("https://api.hypixel.net/skyblock/auctions").json()
    auctions = data["auctions"]
    # array for items from search to be appended into
    items = []
    finalAverage = int()
    averageGeneration = []
    auctionUUID = []
    item = input(str("Item:"))
    for auction in auctions:
        try:
            # makes sure auction in bin and string matches item name requested by user
            if auction["bin"] and str(auction["item_name"]).count(item.title().replace("'S", "'s")) > 0:
                # appends values such as name, starting price and tier.
                items.append([auction["item_name"].replace("'S", "'s"), auction["starting_bid"], auction["tier"]])
                # appends prices of same item requested in order to get the average later
                averageGeneration.append(([auction["starting_bid"]]))
        except KeyError:
            pass

    # sorts price in order to be shown the lowest
    items.sort(key=lambda x: x[1])
    newList = []
    for i in averageGeneration:
        try:
            # loops through list to change to integers
            newList.append(int(i[0]))
            actualAverage = sum(newList) / len(newList)
            # calculating average
            finalAverage = math.floor(actualAverage)
        except TypeError:
            # type error exception
            print("Type Error!")
            pass

    if not items:
        # if searched for item not present print error message and continue
        print(f"Could not find {item.title()}")
        continue

    for item in items:
        # loops round and prints formatted messages
        print("The name of this item is", item[0:1], ",the price of this item is", item[1:2], ",the rarity of this item is", item[2:3])
        print("The average price for this item is", finalAverage)
        break
        # breaks from loop after printing in order to stop infinite printing
