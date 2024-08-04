a = []
def hashf(fruitname):
    global a
    x = ord(fruitname[0])-65
    b = x*6
    count = a.count(fruitname[0])
    value = b+count
    a.append(fruitname[0])
    return value

def hashtable(s):
    hasht = [None]*156
    for i in range(len(s)):
        get = hashf(s[i])
        hasht[get] = s[i]

    for i in range(len(hasht)):   #checking
        print(i,hasht[i])



hashtable([
    "Apples",
    "Apricots",
    "Avocados",
    "Bananas",
    "Bing Cherry",
    "Blueberries",
    "Boysenberries",
    "Cantaloupe",
    "Cherries",
    "Clementine",
    "Crab apples",
    "Cucumbers",
    "Damson plum",
    "Dates",
    "Dewberries",
    "Dinosaur Eggs",
    "Dragon Fruit",
    "Eggfruit",
    "Elderberry",
    "Entawak",
    "Evergreen Huckleberry",
    "Farkleberry",
    "Fig",
    "Finger Lime",
    "Gooseberries",
    "Grapefruit",
    "Guava",
    "Hackberry",
    "Honeycrisp Apples",
    "Imbe",
    "Indonesian Lime",
    "Jackfruit",
    "Jambolan",
    "Java Apple",
    "Kaffir Lime",
    "Kiwi",
    "Kumquat",
    "Lime (Lemon)",
    "Longan",
    "Loquat",
    "Lychee",
    "Mango",
    "Melon",
    "Mulberry",
    "Nashi Pear",
    "Navel Orange",
    "Nectarine",
    "Ogeechee Limes",
    "Olive",
    "Oranges",
    "Oval Kumquat",
    "Papaya",
    "Paw Paw",
    "Peach",
    "Pineapple",
    "Pomegranate",
    "Prickly Pear",
    "Quararibea cordata",
    "Queen Anne Cherry",
    "Quince",
    "Rambutan",
    "Raspberries",
    "Star Fruit",
    "Strawberries",
    "Sugar Baby Watermelon",
    "Tamarind",
    "Tangerine",
    "Tart Cherries",
    "Tomato",
    "Ugni",
    "Uniq Fruit",
    "Vanilla Bean",
    "Velvet Pink Banana",
    "Voavanga",
    "Watermelon",
    "White Mulberry",
    "Wolfberry",
    "Xango Mangosteen",
    "Xigua",
    "Ximenia caffra fruit",
    "Yangmei",
    "Yellow Passion Fruit",
    "Yunnan Hackberry",
    "Zig Zag Vine fruit",
    "Zinfandel Grapes",
    "Zucchini"
])




