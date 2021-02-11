def count_of_all_dishes(menu):
    count = 0
    for section_name in menu:
        section = menu[section_name]
        for dish_name in section:
            count += 1
    return count


def find_all_dish_names_starts_with_letter(menu, letter):
    names = []
    for section_name in menu:
        section = menu[section_name]
        for dish_name in section:
            if dish_name[0].lower() == letter:
                names.append(dish_name)
    return names


menu = {
    "first": {
        "chili soup": {
            "type": "combined",
            "price": 65,
            "count": 8,
            "main ingredients": {"meet", "broth", "red sauce", "chili"},
            "description": "SSSpicy soupez!!!"
        },
        "marshmello soup": {
            "type": "sugar",
            "price": 70,
            "count": 2,
            "main ingredients": {"marshmello", "carrot"},
            "description": "Are you crazy?",
            "revard": "medal honorary pervert"
        },
        "cheezy soup": {
            "type": "cheezy",
            "price": 95,
            "count": 4,
            "main ingredients": {"cheese", "carrot", "sugar", "vegetables", "cheeeeeeese", "white sauce"},
            "description": "Flavored cheezy niamka",
        },
    },
    "second": {
        "dorado": {
            "type": "fish",
            "price": 110,
            "count": 4,
            "main ingredients": {"fish", "steam", "white sauce", "lemon"},
            "description": "Deliiiicious dorado"
        },
        "beef steak": {
            "type": "meet",
            "price": 100,
            "count": 6,
            "main ingredients": {"meet", "red sauce", "spices"},
            "description": "Steaks for REAL men"
        },
        "delicate chicken": {
            "type": "meet",
            "price": 80,
            "count": 3,
            "main ingredients": {"meet", "white sauce", "lemon", "carrot"},
            "description": "Chicken for REAL BRUTAL girls"
        },
        "burger": {
            "type": "combined",
            "price": 65,
            "count": 23,
            "main ingredients": {"meet", "red sauce", "white sauce", "spices", "vegetables", "cheese"},
            "description": "Burgers for REAL madrid"
        },
    },
    "desserts": {
        "cheesecake": {
            "type": "cake",
            "price": 60,
            "count": 13,
            "main ingredients": {"cheese", "cake"},
            "description": "Flavored delicacy"
        },
        "sweet pig": {
            "type": "meet",
            "price": 85,
            "count": 1,
            "main ingredients": {"pig", "sugar", "Nokia"},
            "description": "Pig marinated with sugar syrop and Nokia (This shithead ate this telefone yestesrday...)",
            "revard": "New telephone... or telephone`s details"
        },
        "apple pie": {
            "type": "cake_",
            "price": 70,
            "count": 8,
            "main ingredients": {"lemon", "apples", "baton"},
            "description": "Flavored delicacy"
        },
    },
    "drinks": {
        "compot": {
            "type": "compot",
            "price": 5,
            "count": 133,
            "main ingredients": {"compot", "apples"},
            "description": "compot 5 hrvn",
        },
        "Red vine": {
            "type": "alcohol",
            "price": 205,
            "count": 10,
            "main ingredients": {"platinum", "red sauce"},
            "description": "Delicious discriminating taste"
        },
        "White vine": {
            "type": "alcohol",
            "price": 195,
            "count": 9,
            "main ingredients": {"meteorite uranium", "white sauce"},
            "description": "compot 5 hrvn"
        },
        "blood": {
            "type": "alcohol_",
            "price": 100,
            "count": 10,
            "main ingredients": {"just", "lemon"},
            "description": "-_-"
        },
    }
}


print(find_all_dish_names_starts_with_letter(menu, 'd'))
