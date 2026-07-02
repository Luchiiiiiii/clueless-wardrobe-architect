import random

class ClothingItem:

    def __init__(self, name, category):
        self.name = name
        self.category = category

    def __str__(self):
        return f"{self.name} ({self.category})"
    
my_closet = [
    ClothingItem("Yellow dress", "Gowns"),
    ClothingItem("Black crew neck longsleeve shirt", "Shirts"),
    ClothingItem("Black Pants", "Pants"),
    ClothingItem("Purple Shorts", "Pants"),
    ClothingItem("Black Dress", "Gowns"),
    ClothingItem("white T-shirt", "Shirts"),
    ClothingItem("MIT Hoodie", "Shirts"),
    ClothingItem("Black body hug longsleeve shirt", "Shirts"),
    ClothingItem("Striped off shoulder top", "Shirts"),
    ]

def generate_outfit(wardrope):
    shirts = [item for item in wardrope if item.category == "Shirts"]
    pants = [item for item in wardrope if item.category == "Pants"]
    gowns = [item for item in wardrope if item.category == "Gowns"]

    # 1. Flip a coin! Let's say 1 means "Gown Day" and 0 means "Shirt & Pants Day"
    decision = random.randint(0, 1)

    if decision == 1:
        # Check if we actually have gowns before picking!
        if gowns:
            outfit = [random.choice(gowns)]
        else:
            # Backup plan if gowns list is empty
            outfit = [random.choice(shirts), random.choice(pants)]
    else:
        # Shirt and Pants day!
        if shirts and pants:
            outfit = [random.choice(shirts), random.choice(pants)]
        else:
            # Backup plan if shirts or pants are empty
            outfit = [random.choice(gowns)]

    return outfit
    
new_outfit = generate_outfit(my_closet)

if isinstance(new_outfit, str):
    print(new_outfit)
else:
    print("--your cher-approved outfit")
    for item in new_outfit:
        print(f"{item.name}")    

