# --- Constants ---
SPRITE_SCALING_WASTE = 0.5

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 800
SCREEN_TITLE = "Reciclaje"
MAP_NAME = "background.png"

# Define the list of the waste
random_waste_list = list()
general_waste_list = ["plastic_bag.png", "carton_milk.png", "paint_brush.png"]
paper_waste_list = ["newspaper.png", "paper_roll.png", "cardboard_box.png"]
danger_waste_list = ["mobile.png", "battery.png", "lightbulb.png"]
glass_waste_list = ["broken_glass.png", "mirror.png", "glass_jar.png"]
organic_waste_list = ["apple.png", "leaves.png", "teabag.png"]
plastic_metal_waste_list = ["metal_can.png", "plastic_bottle.png", "aluminum_can.png"]

# Add the waste to the random list
random_waste_list.extend(general_waste_list)
random_waste_list.extend(paper_waste_list)
random_waste_list.extend(danger_waste_list)
random_waste_list.extend(glass_waste_list)
random_waste_list.extend(organic_waste_list)
random_waste_list.extend(plastic_metal_waste_list)
