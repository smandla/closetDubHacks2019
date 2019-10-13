import json

# createDict method

# empty dictionary of closet items
closetItems = {

}

# dictionary for colors
color = {
    # white to blue, red, black
    "FFFFFF": ["0000FF", "FF0000", "000000"],
    # red to yellow, white,
    "FF0000": ["FFFF00", "FFFFFF"],
    # brown to cream, green
    "663300": ["FFFFCC", "006600"],
    # orange to blue, white, black
    "FFA500": ["0000FF", "FFFFFF", "000000"],
    # green to black, brown
    "006600": ["000000", "663300"]
}

# dictionary for items
items = {
    "2": "1",
    "1": "2"
}

"""adds to dictionary as items are added.
    key = color + value"""


def addDict(closetItems, key):
    closetItems[key] = createsValue(key)


def createsValue(key):
    value = key.split(', ')
    newColor = color.get(value[0])
    newItem = items.get(value[1])
    newValue = newColor[0] + ', ' + str(newItem)
    return newValue

#INPUT COLOR find closest value in closetItems dictionary


def main():
    print("Hello!")

userInputColor = str(input("What color (hex) is your item?"))
userInputItem = int(input("What item is it?"))
input = userInputColor + ', ' + str(userInputItem)
addDict(closetItems, input)
print(closetItems)
