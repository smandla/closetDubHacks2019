import json
import webcolors
import math
# createDict method

# empty dictionary of closet items
closetItems = {
    "FFFFFF, pant": ["000000, shirt"],
    "000000, pant": ["FFFFFF, shirt"],
    "663300, pant": ["FFFFCC, shirt"],
    "FFA500, pant": ["0000FF, shirt"],
    "FF0000, pant": ["FFFF00, shirt"],
    "006600, pant": ["000000, shirt"],
    "004D66, pant": ["000000, shirt"],
    "FFFFFF, shirt": ["000000, pant"],
    "000000, shirt": ["FFFFFF, pant"],
    "663300, shirt": ["FFFFCC, pant"],
    "FFA500, shirt": ["0000FF, pant"],
    "FF0000, shirt": ["FFFF00, pant"],
    "006600, shirt": ["000000, pant"],
    "004D66, shirt": ["000000, pant"]
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
    "pant": "shirt",
    "shirt": "pant"
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

def addArray(array):
    rgb = (array[0], array[1], array[2])
    hex = "".join([format(val, '02X') for val in rgb])
    input = hex_result + ', shirt'
    hex_result = getClosestColor(input)

    recommendation = closetItems.get(input)
    value = recommendation.split(', ')
    color = value[0]
    item = value[1]
    print("Wear a " + webcolors.hex_to_name('#' + color) + " " + item)

def getClosestColor(input):
    value = input.split(', ')
    color = tuple(int(value[0][i:i+2], 16) for i in (0, 2, 4))
    # color = webcolors.hex_to_rgb(value[0])
    item = value[1]
    (r1,g1,b1) = color
    (r2,g2,b2) = (255, 255, 255)
    min = math.sqrt((r1 - r2)**2 + (g1 - g2) ** 2 + (b1 - b2) **2)
    returnVal = input
    keys = closetItems.keys()
    for i in range(len(closetItems)):
        value1 = list(keys)
        value2 = value1[i].split(', ')
        color1 = value2[0]
        item1 = value2[1]
        (r2,g2,b2) = tuple(int(color1[i:i+2], 16) for i in (0, 2, 4))
        if (math.sqrt((r1 - r2)**2 + (g1 - g2) ** 2 + (b1 - b2) **2)) < min:
            min = math.sqrt((r1 - r2)**2 + (g1 - g2) ** 2 + (b1 - b2) **2)
            returnVal = closetItems[value1[i]]

    return returnVal

def main():
    print("Hello!")

print (getClosestColor('ffffff, shirt'))
# userInputColor = input("What color (hex) is your item?")
# # userInputColorHex = str('#{:02x}{:02x}{:02x}'.format(userInputColor))
# rgb = (255, 255, 255)
# hex_result = "".join([format(val, '02X') for val in rgb])
# userInputItem = str(input("What item is it?"))
# input = hex_result + ', ' + str(userInputItem)
# addDict(closetItems, input)
# print(closetItems)
# recommendation = closetItems.get(input)
# value = recommendation.split(', ')
# color = value[0]
# item = value[1]
#
# print("Wear a " + webcolors.hex_to_name('#' + color) + " " + item)
