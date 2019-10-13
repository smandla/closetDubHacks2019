import json

# createDict method

# empty dictionary of closet items
closetItems = {
    "FFFFFF, 2": ["000000, 1"],
    "000000, 2": ["FFFFFF, 1"],
    "663300, 2": ["FFFFCC, 1"],
    "FFA500, 2": ["0000FF, 1"],
    "FF0000, 2": ["FFFF00, 1"],
    "006600, 2": ["000000, 1"],
    "FFFFFF, 1": ["000000, 2"],
    "000000, 1": ["FFFFFF, 2"],
    "663300, 1": ["FFFFCC, 2"],
    "FFA500, 1": ["0000FF, 2"],
    "FF0000, 1": ["FFFF00, 2"],
    "006600, 1": ["000000, 2"]
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

# def addArray(array[]):




def main():
    print("Hello!")

userInputColor = input("What color (hex) is your item?")
# userInputColorHex = str('#{:02x}{:02x}{:02x}'.format(userInputColor))
rgb = (255, 255, 255)
hex_result = "".join([format(val, '02X') for val in rgb])
userInputItem = int(input("What item is it?"))
input = hex_result + ', ' + str(userInputItem)
addDict(closetItems, input)
print(closetItems)
recommendation = closetItems.get(input)
